# Armorblox Python SDK (Alpha)

This is an alpha version of the SDK with limited documentation and no support.

## Requirements

Python 3.5+

## Installation

```
pip install git+https://github.com/armorblox/armorblox-python-sdk
```

## Usage

```
from armorblox import client

# Create an API client for your tenant
c = client.Client(api_key='your-api-key-here', instance_name='yourtenantname')

# Fetch a list of threats
threat_incidents = c.threats.list()

# Fetch a specific threat
incident = c.threats.get(44006)


# Fetch a list of abuse incidents
abuse_incidents = c.abuse_incidents.list()

# Fetch a specific abuse incident
abuse_incident = c.abuse_incidents.get(44200)


# Fetch a list of DLP incidents
dlp_incidents = c.dlp_incidents.list()

# Fetch a specific DLP incident
dlp_incident = c.dlp_incidents.get(44010)
```

## Contributing

* Install [Poetry](https://python-poetry.org)
* Clone the SDK repo & `cd` into it
```
git clone https://github.com/armorblox/armorblox-python-sdk
cd armorblox-python-sdk
```
* Run `poetry install` to install the dependencies
* Run `tox` to run the tests
