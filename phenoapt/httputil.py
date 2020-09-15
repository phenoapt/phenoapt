#  Copyright (c) 2018-2020 Beijing Ekitech Co., Ltd.
#  All rights reserved.

from abc import ABC, abstractmethod

import requests


class RestAPI(ABC):
    def __init__(self, base_url):
        if not base_url.endswith('/'):
            base_url = base_url + '/'
        self.base_url = base_url

    @abstractmethod
    def _request(self, func, rest_path, *args, **kwargs):
        pass

    def get(self, rest_path, *args, **kwargs):
        return self._request(requests.get, rest_path, *args, **kwargs)

    def put(self, rest_path, *args, **kwargs):
        return self._request(requests.put, rest_path, *args, **kwargs)

    def post(self, rest_path, *args, **kwargs):
        return self._request(requests.post, rest_path, *args, **kwargs)

    def delete(self, rest_path, *args, **kwargs):
        return self._request(requests.delete, rest_path, *args, **kwargs)
