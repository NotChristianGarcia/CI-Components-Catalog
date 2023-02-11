import yaml

# Path to the dataset file.
DATASET = '/catalog/components-data.yaml'


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


