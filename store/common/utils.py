import json
from typing import Dict


def log(details: Dict):
    """
    this is a global logging function
    Potentially will be extended with more advanced logging function
    """

    print(json.dumps(details, indent=4))

    if details['level'] == 'error':
        pass
