from flask import Flask, render_template
import yaml 
app = Flask(__name__)


DATASET = '/catalog/components-data.yaml'

def get_components():
    """
    Proof of concept funtion that returns all components in the catalog.
    """
    with open(DATASET, 'r') as f:
        components = yaml.safe_load(f)
    return components['components']


@app.route('/data', methods=['GET'])
def get_data():
    components = get_components()
    return render_template('data.html', components=components)

    


# run the development server when started from the command line
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')