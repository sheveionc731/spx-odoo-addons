{
    'name': 'SPX WiPay Payment Provider',
    'version': '1.0.0',
    'category': 'Accounting/Payment Providers',
    'summary': 'WiPay Caribbean integration for Odoo 19',
    'author': 'Spxcorp Limited',
    'depends': ['payment', 'website_sale', 'sale', 'account'],
    'data': [
        'views/payment_wipay_templates.xml',
        'views/payment_provider_views.xml',
        'data/payment_method_data.xml',
        'data/payment_provider_data.xml'
    ],
    'installable': True,
    'application': False
}