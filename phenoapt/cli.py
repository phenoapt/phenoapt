#  Copyright (c) 2018-2020 Beijing Ekitech Co., Ltd.
#  All rights reserved.

import json

import click
import sys

from phenoapt import PhenoApt

pass_client = click.make_pass_decorator(PhenoApt)


@click.group()
@click.option('--endpoint', required=True, default='https://phenoapt.org')
@click.option('--token', required=False)
@click.pass_context
def main(ctx, endpoint, token):
    """ Phenotype-based Gene Prioritization, modelled using Graph Embedding techniques """
    ctx.obj = PhenoApt(endpoint, token=token)


@main.command()
@click.option('-p', '--phenotype', required=True, help='HPO phenotypes, comma or semicolon separated')
@click.option('-w', '--weight', required=False, help='Weights, comma or semicolon separated')
@click.option('-m', '--model', required=False, help='Optional model id, default is latest on the server')
@click.option('-n', '--num', required=True, default=100, help='Number of results to return')
@click.option('-f', '--format', required=True, default='simple', type=click.Choice(['simple', 'json']), help='Output format, default is simple')
@pass_client
def rank_gene(client: PhenoApt, phenotype, weight, model, num, format):
    """ Show gene rankings """
    phenotype = phenotype.replace('：', ':').replace('，', ',')
    weight = weight.replace('，', ',')
    res = client.rank_gene(phenotype, weight=weight, n=num)
    rank = res.rank
    if format == 'simple':
        import tabulate
        columns = ['rank', 'score', 'entrez_id', 'gene_symbol']
        data = [tuple(row[x] for x in columns) for row in rank]
        click.echo(tabulate.tabulate(data, headers=columns))
    elif format == 'json':
        click.echo(json.dumps(rank, indent=2))

    # CSV
    # from io import StringIO
    # import pandas as pd
    #
    # output = StringIO()
    # df = pd.DataFrame(rank)
    # df.to_csv(output, index=False)
    # click.echo(output.getvalue())


@main.command()
@click.option('-p', '--phenotype', required=True, help='HPO phenotypes, comma or semicolon separated')
@click.option('-w', '--weight', required=False, help='Weights, comma or semicolon separated')
@click.option('-m', '--model', required=False, help='Optional model id, default is latest on the server')
@click.option('-n', '--num', required=True, default=100, help='Number of results to return')
@click.option('-f', '--format', required=True, default='simple', type=click.Choice(['simple', 'json']), help='Output format, default is simple')
@pass_client
def rank_disease(client, phenotype, weight, model, num, format):
    """ Show disease rankings """
    phenotype = phenotype.replace('：', ':').replace('，', ',')
    weight = weight.replace('，', ',')
    res = client.rank_disease(phenotype, weight=weight, n=num)
    rank = res.rank
    if format == 'simple':
        import tabulate
        columns = ['rank', 'score', 'disease_id', 'disease_name']
        data = [tuple(row[x] for x in columns) for row in rank]
        click.echo(tabulate.tabulate(data, headers=columns))
    elif format == 'json':
        click.echo(json.dumps(rank, indent=2))


@main.command()
def version():
    """ Show PhenoApt client version """
    from phenoapt import __version__ as phenoapt_version
    click.echo(f'PhenoApt client version {phenoapt_version}, The PhenoApt Team <info@phenoapt.org>')


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
