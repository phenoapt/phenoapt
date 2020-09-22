#  Copyright (c) 2018-2020 Beijing Ekitech Co., Ltd.
#  All rights reserved.

import logging
import re
from functools import lru_cache

from .httputil import RestAPI

__all__ = [
    'PhenoApt',
    'PhenoAptResult',
]

logger = logging.getLogger(__name__)


class PhenoAptResult(object):
    """ PhenoApt response wrapper """

    def __init__(self, response_or_data, rank_type):
        self.response = response_or_data
        self.rank_type = rank_type

    @property
    @lru_cache()
    def data(self):
        try:
            return self.response.json()
        except AttributeError:
            return self.response

    @property
    def rank_columns(self):
        if self.rank_type == 'gene':
            return ['rank', 'score', 'entrez_id', 'gene_symbol', 'known_disease', 'links']
        elif self.rank_type == 'disease':
            return ['rank', 'score', 'disease_id', 'disease_name', 'known_gene', 'links']
        else:
            raise RuntimeError('Unknown rank type, should not happen!')

    @property
    def rank(self):
        return self.data['data']['rank']

    @property
    def rank_frame(self):
        import pandas as pd
        return pd.DataFrame(self.rank, columns=self.rank_columns)

    @property
    def matched(self):
        return self.data['data']['matched']

    @property
    def unmatched(self):
        return self.data['data']['unmatched']

    def _repr_html_(self):
        display_text = ''
        if self.unmatched:
            display_text = '''
                <div>
                    <h3>Unmatched Phenotypes</h3>
                    <p>{}</p>
                </div>
            '''.format(', '.join(self.unmatched))

        return display_text + '''<div><h3>PhenoApt Rankings</h3></div>''' + self.rank_frame._repr_html_()


class PhenoApt(RestAPI):
    def __init__(self, base_url='https://phenoapt.org', token=None):
        """
        Returns a new PhenoApt Client.

        :param base_url: Alternative PhenoApt endpoint (optional)
        :param token: PhenoApt authorization token (optional)
        """
        super(PhenoApt, self).__init__(base_url)
        self.token = token

    @staticmethod
    def _get_error_message(response):
        try:
            return response.json()['message']
        except:
            return response.text

    @staticmethod
    def _normalize_csv_list_input(values):
        if isinstance(values, str):
            values = re.split(r'\s*[,|;]\s*', values)
        values = [str(x).strip() for x in values]
        return ','.join(x for x in values if x)

    def _request(self, func, rest_path, *args, **kwargs):
        headers = {}
        if self.token:
            headers['Authorization'] = f'Bearer {self.token}'

        custom_headers = kwargs.pop('headers', {})
        headers.update(custom_headers)

        response = func(self.base_url + rest_path, headers=headers, *args, **kwargs)
        try:
            response.raise_for_status()
        except:
            message = self._get_error_message(response)
            logger.exception(f'Error on PhenoApt request: {message}')
            raise
        else:
            return response

    def rank_gene(self, phenotype, weight=None, n=None):
        """
        Request gene rankings.

        :param phenotype: HPO phenotypes, comma or semicolon separated, or list-like object
        :param weight: Weights, comma or semicolon separated, or list-like object
        :param n: Number of results to return
        :return: Ranking result
        """
        data = dict(p=self._normalize_csv_list_input(phenotype))

        if weight:
            data['weights'] = self._normalize_csv_list_input(weight)

        if n:
            data['n'] = n

        return PhenoAptResult(self.get('phenoapt/api/v3/rank-gene', params=data), 'gene')

    def rank_disease(self, phenotype, weight=None, n=None):
        """
        Request disease rankings.

        :param phenotype: HPO phenotypes, comma or semicolon separated, or list-like object
        :param weight: Weights, comma or semicolon separated, or list-like object
        :param n: Number of results to return
        :return: Ranking result
        """
        data = dict(p=self._normalize_csv_list_input(phenotype))

        if weight:
            data['weights'] = self._normalize_csv_list_input(weight)

        if n:
            data['n'] = n
        return PhenoAptResult(self.get('phenoapt/api/v3/rank-disease', params=data), 'disease')
