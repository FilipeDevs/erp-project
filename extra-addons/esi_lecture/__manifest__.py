# -*- coding: utf-8 -*-
{
    'name': "esi_lecture",

    'summary': """
        Management Book Aplication
    """,

    'description': """
        Management Book Aplication.
    """,

    'author': "Filipe Pereira - 58093",
    'website': "https://he2b.be/etudiant/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'point_of_sale', 'stock'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/book_menu.xml',
        'views/book_view.xml',
        'views/author_view.xml'
    ],
    'images': [
        'static/description_images/dune1.jpg',
        'static/description_images/harryPotter1.jpg',
        'static/description_images/harryPotter2.jpg',
        'static/description_images/harryPotter3.jpg',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
        'demo/stock_demo.xml'
    ],

    'application': True
}
