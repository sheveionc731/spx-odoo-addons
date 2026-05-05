<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <template id="redirect_form">
        <form t-att-action="api_url" method="get">
            <t t-foreach="wipay_payload or {}" t-as="key">
                <input type="hidden" t-att-name="key" t-att-value="wipay_payload[key]"/>
            </t>
            <button type="submit" class="btn btn-primary">Continue to WiPay</button>
        </form>
    </template>
</odoo>
