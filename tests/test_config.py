# -*- coding: utf-8 -*-


from armorblox.config import Config
import pytest


class TestConfig:
    @pytest.fixture
    def create_config(self, api_key, instance_name, instance_url, sdk_version):
        config_params = {
            'api_key': api_key,
            'instance_name': instance_name,
            'instance_url': instance_url,
            'sdk_version': sdk_version
        }

        def _create_config(exclude_params=[]):
            for p in exclude_params:
                config_params.pop(p, None)
            return Config(**config_params)

        return _create_config

    @pytest.fixture
    def full_config(self, create_config):
        return create_config()

    def test_sdk_version(self, full_config, sdk_version):
        assert full_config.sdk_version == sdk_version

    def test_unspecified_sdk_version(self, create_config):
        c = create_config(exclude_params=['sdk_version'])
        assert c.sdk_version == 'Unspecified'

    def test_api_key(self, full_config, api_key):
        assert full_config.api_key == api_key

    def test_instance_name(self, full_config, instance_name):
        assert full_config.instance_name == instance_name

    def test_only_instance_name_given(self, create_config, instance_url):
        c = create_config(exclude_params=['instance_url'])
        assert c.instance_url == instance_url + '/'

    def test_instance_url(self, full_config, instance_url):
        assert full_config.instance_url == instance_url + '/'

    def test_only_instance_url_given(self, create_config, instance_name):
        c = create_config(exclude_params=['instance_name'])
        assert c.instance_name == instance_name

    def test_no_instance_given(self, create_config):
        with pytest.raises(Exception):
            create_config(exclude_params=['instance_name', 'instance_url'])

    def test_base_api_url(self, full_config, instance_url, instance_name):
        assert full_config.base_api_url == instance_url + '/api/{}/organizations/' + instance_name + '/'
