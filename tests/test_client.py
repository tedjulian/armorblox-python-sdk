# -*- coding: utf-8 -*-


from armorblox.client import Client


class TestClient:
    def test_sdk_version(self, sdk_version):
        assert Client.sdk_version() == sdk_version
