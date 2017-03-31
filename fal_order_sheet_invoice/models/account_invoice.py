# -*- coding: utf-8 -*-

from odoo import fields, models


class account_invoice(models.Model):
    _inherit = 'account.invoice'

    purchase_ids = fields.Many2many('purchase.order', 'purchase_invoice_rel', 'invoice_id', 'purchase_id', 'Purchases', readonly=True, help="Purchase Orders That related to Invoice")
    sale_ids = fields.Many2many('sale.order', 'sale_order_invoice_rel', 'invoice_id', 'order_id', 'Sales', readonly=True, help="This is the list of sale that related to this Invoice")

#end of account_invoice()
