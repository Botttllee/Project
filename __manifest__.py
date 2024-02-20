# -*- coding: utf-8 -*-
{
    'name': "Hotel booking order",
    'version': '1.0.0',
    'category':"Hotel",
    'summary':"Book a hotel now",
    'description':"Booking a hotel",
    'author': "Hendrik",
    'sequence':-100,
    'website': "http://www.yourcompany.com",
    'application': True,
    'auto_install': False,
    'license': 'LGPL-3',
    # any module necessary for this one to work correctly
    'depends': ['base'],
    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/view.xml',
        'views/view_transaksi.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
