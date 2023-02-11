from flask import Flask, render_template, redirect, request
import json
import requests
import yaml 


import auth
from config import config


app = Flask(__name__)

# Set the secret key to some random bytes. 
# TODO: this key should be updated
app.secret_key = b'dsckj32487sj238193626%^#$'

DATASET = '/catalog/components-data.yaml'


@app.route('/logout', methods=['GET'])
def logout():
    auth.clear_session()
    return redirect('/data', code=302)


@app.route('/login', methods=['GET'])
def login():
    """
    Check for the existence of a login session, and if none exists, start the OAuth2 flow.
    """
    authenticated, _ = auth.is_logged_in()
    # if already authenticated, redirect to the main data table
    if authenticated:
        return redirect("/data", code=302)
    # otherwise, start the OAuth flow
    callback_url = f"{config['app_base_url']}/oauth2/callback"
    tapis_url = f"{config['tapis_base_url']}/v3/oauth2/authorize?client_id={config['client_id']}&redirect_uri={callback_url}&response_type=code"
    return redirect(tapis_url, code=302)


@app.route('/oauth2/callback', methods=['GET'])
def callback():
    """
    Process a callback from a Tapis authorization server:
      1) Get the authorization code from the query parameters.
      2) Exchange the code for a token
      3) Add the user and token to the session
      4) Redirect to the /data endpoint. 
    """
    code = request.args.get('code')
    if not code:
        raise Exception(f"Error: No code in request; debug: {request.args}")
    url = f"{config['tapis_base_url']}/v3/oauth2/tokens"
    data = {
        "code": code, 
        "redirect_uri": f"{config['app_base_url']}/oauth2/callback", 
        "grant_type": "authorization_code",
    }
    try:
        response = requests.post(url, data=data, auth=(config['client_id'], config['client_key']))
        response.raise_for_status()
        json_resp = json.loads(response.text)
        token = json_resp['result']['access_token']['access_token']
    except Exception as e:
        raise Exception(f"Error generating Tapis token; debug: {e}")

    username = get_username(token)
    app.logger.info(f"Got username for token; username: {username}")
    auth.add_user_to_session(username, token)
    return redirect("/data", code=302)    


def get_username(token):
    """
    Validate a Tapis JWT, `token`, and resolve it to a username.
    """
    headers = {'Content-Type': 'text/html'}
    # call the userinfo endpoint
    url = f"{config['tapis_base_url']}/v3/oauth2/userinfo"
    headers = {'X-Tapis-Token': token}
    try:
        rsp = requests.get(url, headers=headers)
        rsp.raise_for_status()
        username = rsp.json()['result']['username']
    except Exception as e:
        raise Exception(f"Error looking up token info; debug: {e}")
    return username


def get_components():
    """
    Proof of concept function that returns all components in the catalog.
    """
    with open(DATASET, 'r') as f:
        components = yaml.safe_load(f)
    return components['components']


def get_public_components():
    """
    Returns only the components for which publicAccess is true
    """
    return [c for c in get_components() if c['publicAccess']]


@app.route('/data', methods=['GET'])
def get_data():
    authenticated, user = auth.is_logged_in()
    if not authenticated:
        logged_in = False
        message = 'NOTE: Only displaying public components.'
        components = get_public_components()
    else:
        logged_in = True
        message = f"Username: {user}"
        components = get_components()
    total = len(components)
    return render_template('data.html', 
        components=components,
        total=total, 
        message=message, 
        logged_in=logged_in)


# run the development server when started from the command line
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')