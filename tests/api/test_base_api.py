# -*- coding: utf-8 -*-


from armorblox.api.base_api import BaseApi
from armorblox.config import Config
import pytest


class TestBaseApi:
    @pytest.fixture(autouse=True)
    def set_base_api(self, config_params):
        self.base_api = BaseApi(Config(**config_params))

    def test_version(self):
        assert self.base_api.version == 'v1beta1'

    def test_headers(self, config_params):
        dh = self.base_api.headers()
        assert dh['X-Ab-Authorization'] == config_params['api_key']
        assert dh['Content-Type'] == 'application/json'
        assert dh['User-Agent'] == 'Armorblox-Python-SDK/' + config_params['sdk_version']

    def test_endpoint(self, config_params):
        u = config_params['instance_url'] + '/api/'
        p = '/organizations/' + config_params['instance_name'] + '/path_value'
        assert self.base_api.endpoint('path_value') == u + 'v1beta1' + p
        assert self.base_api.endpoint('path_value', 'v3') == u + 'v3' + p

    def test_list_params(self):
        p = self.base_api.list_params()
        assert p['page_size'] == BaseApi.PAGE_SIZE
        assert p['page_token'] == '0'
