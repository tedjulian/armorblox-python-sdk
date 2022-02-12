# -*- coding: utf-8 -*-


import pytest


@pytest.fixture
def api_key():
    return 'wMUW/RSenk1xkJ7kGc6np/Ckpyi38+3CWFsI03d5Id4='


@pytest.fixture
def instance_name():
    return 'test-instance'


@pytest.fixture
def instance_url():
    return 'https://test-instance.armorblox.io'


@pytest.fixture
def sdk_version():
    return '0.1.0.20220201'


@pytest.fixture
def config_params(api_key, instance_name, instance_url, sdk_version):
    return {
        'api_key': api_key,
        'instance_name': instance_name,
        'instance_url': instance_url,
        'sdk_version': sdk_version
    }
