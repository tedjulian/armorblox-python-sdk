<img src="https://assets.armorblox.com/f/52352/775x159/8fa6246e47/logo_color.svg" width=387 alt="Armorblox logo">

# Armorblox Python SDK (Alpha)

[![PyPI version](https://badge.fury.io/py/armorblox-sdk.svg)](https://badge.fury.io/py/armorblox-sdk)
[![Apache-2 License](https://img.shields.io/badge/license-Apache2-blueviolet)](https://www.apache.org/licenses/LICENSE-2.0)

This is an alpha version of the SDK with limited documentation and no support.

## Requirements

Python 3.5+

## Installation

```
pip install armorblox-sdk
```

## Usage

```
from armorblox import client

# Create an API client for your tenant
c = client.Client(api_key='your-api-key-here', instance_name='yourtenantname')

# Fetch a list of threats
threat_incidents, next_page_token, total_incident_count = c.threats.list()

# Fetch a specific threat
incident = c.threats.get(44006)


# Fetch a list of abuse incidents
abuse_incidents, next_page_token, total_incident_count = c.abuse_incidents.list()

# Fetch a specific abuse incident
abuse_incident = c.abuse_incidents.get(44200)


# Fetch a list of DLP incidents
dlp_incidents, next_page_token, total_incident_count = c.dlp_incidents.list()

# Fetch a specific DLP incident
dlp_incident = c.dlp_incidents.get(44010)


# Example to fetch all threats using next_page_token
c = client.Client(api_key='your-api-key-here', instance_name='yourtenantname')
next_page_token = None
incidents = []
threats, next_page_token, total_incident_count = c.threats.list(page_token=next_page_token)
incidents.append(threats)
while next_page_token != None:
    threats, next_page_token, total_incident_count = client.threats.list(page_token=next_page_token)
    incidents.append(threats)

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

## Publishing

#### TestPyPI

One-time setup
```
poetry config repositories.test-pypi https://test.pypi.org/legacy/
poetry config pypi-token.test-pypi <your-TestPyPI-token>
```

Publishing
```
poetry publish --build -r test-pypi
```

Use
```
pip install --index-url https://test.pypi.org/simple/ --no-deps armorblox-sdk
```
to make sure the installation works correctly.

#### PyPI

One-time setup
```
poetry config pypi-token.pypi <your-PyPI-token>
```

Publishing
```
poetry publish --build
```
