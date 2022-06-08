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

c = client.Client(api_key='your-api-key-here', instance_name='yourtenantname')
threat_incidents = c.threats.list()
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
