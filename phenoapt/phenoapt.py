#  Copyright (c) 2018-2020 Beijing Ekitech Co., Ltd.
#  All rights reserved.

import logging
from functools import lru_cache

from phenoapt.httputil import RestAPI

logger = logging.getLogger(__name__)


class PhenoAptResult(object):
    def __init__(self, response_or_data):
        self.response = response_or_data

    @property
    @lru_cache()
    def data(self):
        try:
            return self.response.json()
        except AttributeError:
            return self.response

    @property
    def rank(self):
        return self.data['data']['rank']

    @property
    def matched(self):
        return self.data['data']['matched']

    @property
    def unmatched(self):
        return self.data['data']['unmatched']


class PhenoApt(RestAPI):
    def __init__(self, base_url, token=None):
        super(PhenoApt, self).__init__(base_url)
        self.token = token

    def _request(self, func, rest_path, *args, **kwargs):
        headers = {}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'

        custom_headers = kwargs.pop('headers', {})
        headers.update(custom_headers)

        try:
            r = func(self.base_url + rest_path, headers=headers, *args, **kwargs)
            r.raise_for_status()
            return r
        except:
            logger.exception('Error on PhenoApt request')
            raise

    def rank_gene(self, phenotype, weight=None, n=None):
        data = dict(p=phenotype)

        if weight:
            data['weights'] = weight

        if n:
            data['n'] = n

        return PhenoAptResult(self.get('phenoapt/api/v3/rank-gene', params=data))

    def rank_disease(self, phenotype, weight=None, n=None):
        data = dict(p=phenotype)

        if weight:
            data['weights'] = weight

        if n:
            data['n'] = n
        return PhenoAptResult(self.get('phenoapt/api/v3/rank-disease', params=data))
