========
phenoapt
========


.. image:: https://img.shields.io/pypi/v/phenoapt.svg
        :target: https://pypi.python.org/pypi/phenoapt

.. image:: https://img.shields.io/travis/phenoapt/phenoapt.svg
        :target: https://travis-ci.com/phenoapt/phenoapt


Phenotype-based Gene Prioritization, modelled using Graph Embedding techniques

This project contains the python client API library.

Installation
------------

You install phenoapt with pip:

    pip install phenoapt

Or, if you prefer, clone the git repo and install from source::

    git clone https://github.com/phenoapt/phenoapt.git
    cd phenoapt
    python setup.py install

Features
--------

* Rank by genes or diseases
* Optional phenotype weights can be supplied

Command line usage
------------------

An example of top 10 gene rankings given phenotypes and weights::

    $ phenoapt rank-gene -p 'HP:0001193,HP:0001231,HP:0002999,HP:0003621' -w '1,2,2,1' -n 10
      rank    score  entrez_id    gene_symbol
    ------  -------  -----------  -------------
         1  72.5097  EZ:8200      GDF5
         2  73.8103  EZ:2697      GJA1
         3  79.5231  EZ:51360     MBTPS2
         4  85.5202  EZ:2316      FLNA
         5  86.5767  EZ:10682     EBP
         6  86.7231  EZ:8481      OFD1
         7  86.9275  EZ:4010      LMX1B
         8  87.2089  EZ:3930      LBR
         9  91.1848  EZ:4000      LMNA
        10  92.2059  EZ:2273      FHL1

and similarly, disease rankings can be obtained like this::

    $ phenoapt rank-disease -p 'HP:0001193,HP:0001231,HP:0002999,HP:0003621' -w '1,2,2,1' -n 10
      rank    score  disease_id    disease_name
    ------  -------  ------------  -------------------------------------------------------------------------------
         1  63.2341  OMD:228900    FIBULAR HYPOPLASIA AND COMPLEX BRACHYDACTYLY
         2  66.2116  OMD:215140    GREENBERG DYSPLASIA; GRBGD
         3  66.3988  OMD:161200    NAIL-PATELLA SYNDROME; NPS
         4  71.6026  OMD:308205    IFAP SYNDROME WITH OR WITHOUT BRESHECK SYNDROME
         5  73.3633  OMD:302960    CHONDRODYSPLASIA PUNCTATA 2, X-LINKED DOMINANT; CDPX2
         6  73.3904  OMD:135900    COFFIN-SIRIS SYNDROME 1; CSS1
         7  74.5251  OMD:228930    FIBULAR APLASIA OR HYPOPLASIA, FEMORAL BOWING AND POLY-, SYN-, AND OLIGODACTYLY
         8  75.0786  OMD:611816    TEMPLE-BARAITSER SYNDROME; TMBTS
         9  75.1829  OMD:228520    FIBROCHONDROGENESIS 1; FBCG1
        10  78.0241  OMD:609945    OMD:609945

For more information about tool usage, run phenoapt with --help.

Code usage
------------------

See `jupyter notebook example <https://github.com/phenoapt/phenoapt/blob/master/notebooks/phenoapt-example.ipynb>`_
