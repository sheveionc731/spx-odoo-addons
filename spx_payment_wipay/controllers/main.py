from odoo import http
from odoo.http import request
from werkzeug.utils import redirect

class WiPayController(http.Controller):

    @http.route('/payment/wipay/return', type='http', auth='public', csrf=False)
    def wipay_return(self, **data):
        request.env['payment.transaction'].sudo()._process('wipay', data)
        return redirect('/payment/status')
