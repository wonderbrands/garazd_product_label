# Copyright © 2018 Garazd Creation (<https://garazd.biz>)
# @author: Yurii Razumovskyi (<support@garazd.biz>)
# @author: Iryna Razumovska (<support@garazd.biz>)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.html).

# flake8: noqa: E501

{
    'name': 'Custom Product Labels in Purchases',
    'version': '15.0.1.0.0',
    'category': 'Extra Tools',
    'author': 'Garazd Creation',
    'website': 'https://garazd.biz/shop',
    'license': 'LGPL-3',
    'summary': 'Print custom product barcode labels for purchase orders',
    'images': ['static/description/banner.png', 'static/description/icon.png'],
    'live_test_url': 'https://garazd.biz/r/7Tf',
    'depends': [
        'garazd_product_label',
        'purchase',
    ],
    'data': [
        'wizard/print_product_label_views.xml',
    ],
    'external_dependencies': {
    },
    'price': 15.0,
    'currency': 'EUR',
    'support': 'support@garazd.biz',
    'application': False,
    'installable': True,
    'auto_install': False,
}
