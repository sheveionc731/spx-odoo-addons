from odoo import fields, models

class PaymentProvider(models.Model):
    _inherit = 'payment.provider'

    code = fields.Selection(selection_add=[('wipay', 'WiPay')], ondelete={'wipay': 'set default'})

    wipay_region = fields.Selection([
        ('TT','Trinidad and Tobago'),
        ('BB','Barbados'),
        ('GY','Guyana'),
        ('JM','Jamaica')
    ], string='Region', default='TT')

    wipay_account_number = fields.Char(string='Account Number')
    wipay_api_key = fields.Char(string='API Key')

    def _get_default_payment_method_codes(self):
        if self.code == 'wipay':
            return {'wipay'}
        return super()._get_default_payment_method_codes()
