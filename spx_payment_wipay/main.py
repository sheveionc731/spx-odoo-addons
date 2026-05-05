<?xml version="1.0" encoding="utf-8"?>
<odoo>
    <record id="payment_provider_form_wipay" model="ir.ui.view">
        <field name="name">payment.provider.form.wipay</field>
        <field name="model">payment.provider</field>
        <field name="inherit_id" ref="payment.payment_provider_form"/>
        <field name="arch" type="xml">
            <xpath expr="//sheet" position="inside">
                <group string="WiPay" invisible="code != 'wipay'">
                    <group string="Credentials">
                        <field name="wipay_region"/>
                        <field name="wipay_account_number" password="True"/>
                        <field name="wipay_api_key" password="True"/>
                    </group>
                    <group string="Configuration">
                        <field name="wipay_fee_structure"/>
                        <field name="wipay_origin"/>
                    </group>
                </group>
            </xpath>
        </field>
    </record>
</odoo>
