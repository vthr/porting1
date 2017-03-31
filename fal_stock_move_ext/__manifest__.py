# -*- coding: utf-8 -*-
{
    "name": "STC-09_Stock Move Ext",

    "version": "1.0",

    'author': 'Falinwa Hans',

    "description": """
    Module to provided additional feature to stock move.
    """,

    "depends": ['sale_stock', 'stock', 'purchase'],
    'init_xml': [],
    'update_xml': [
        'views/stock_view.xml'
    ],
    'css': [],
    'js': [],
    'qweb': [],
    'installable': True,
    'active': False,
    'application': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
