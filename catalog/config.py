import os
import yaml

with open('/catalog/config.yaml', 'r') as f:
    config = yaml.safe_load(f)


# override with environment vars
if os.environ.get('client_id'):
    config['client_id'] = os.environ.get('client_id')

if os.environ.get('client_key'):
    config['client_key'] = os.environ.get('client_key')

if os.environ.get('tapis_base_url'):
    config['tapis_base_url'] = os.environ.get('tapis_base_url')

if os.environ.get('app_base_url'):
    config['app_base_url'] = os.environ.get('app_base_url')
