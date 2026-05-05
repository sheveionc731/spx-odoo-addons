<?xml version="1.0" encoding="utf-8"?>
<odoo noupdate="1">
    <record id="payment_provider_wipay" model="payment.provider">
        <field name="name">WiPay</field>
        <field name="code">wipay</field>
        <field name="state">disabled</field>
        <field name="company_id" ref="base.main_company"/>
        <field name="wipay_region">TT</field>
        <field name="wipay_account_number">1234567890</field>
        <field name="wipay_api_key">123</field>
        <field name="wipay_fee_structure">customer_pay</field>
        <field name="payment_method_ids" eval="[(6, 0, [ref('spx_payment_wipay.payment_method_wipay')])]"/>
    </record>
</odoo>
