# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name' : 'Requisiciones',
    'version' : '1.1',
    'summary': 'Es el primer módulo para probar',
    'description': """
Solo es el primer módulo para probar las cosas que puedo hacer en localhost
""",
    'autor':'Nacho',
    'category': 'Prueba',
    'depends' : ['purchase'],

    'data': ['views/purchase_order_form.xml'],
    'installable': True,
    'application': True,
    'auto_install': False,
    #'post_init_hook': '_account_post_init',
}
