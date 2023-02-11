import yaml

with open('/catalog/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# sanity checks
if 'client_id' not in config:
    raise Exception("no client_id in config. Quitting..")

if 'client_key' not in config or config['client_key'] == None:
    raise Exception("no client_key in config. Quitting..")
    
if 'tapis_base_url' not in config:
    raise Exception("no tapis_base_url in config. Quitting..")

if 'app_base_url' not in config:
    raise Exception("no app_base_url in config. Quitting..")
