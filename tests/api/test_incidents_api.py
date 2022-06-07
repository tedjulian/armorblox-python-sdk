# -*- coding: utf-8 -*-


from armorblox.api.incidents_api import IncidentsApi, ThreatsApi, DLPIncidentsApi, AbuseIncidentsApi
from armorblox.config import Config
import pytest
import responses


class TestIncidentsApi:
    @pytest.fixture(autouse=True)
    def set_incidents_api(self, config_params):
        self.config = Config(**config_params)
        self.base_api_url = self.config.base_api_url.format('v1beta1')
        self.incidents_api = IncidentsApi(self.config)

    def test_list(self, mocked_responses):
        mocked_responses.add(
            responses.GET, self.base_api_url + IncidentsApi.PATH,
            json={
                'next_page_token': '50',
                'incidents': [{'a': 1}]
            },
            status=200,
            content_type='application/json')
        response = self.incidents_api.list()
        assert response['total_count'] == 150
        assert response['next_page_token'] == '50'
