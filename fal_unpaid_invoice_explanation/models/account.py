# -*- coding: utf-8 -*-
from odoo import fields, models


class account_invoice(models.Model):
    _inherit = "account.invoice"

    fal_unpaid_invoice_explanation_date = fields.Date('Unpaid Invoice Explanation Date',track_visibility='onchange')
    fal_unpaid_invoice_next_action_date = fields.Date('Unpaid Invoice Next Date',track_visibility='onchange')
    fal_unpaid_invoice_explanation = fields.Text('Unpaid Invoice Explanation',track_visibility='onchange')
    fal_unpaid_invoice_next_action = fields.Text('Unpaid Invoice Next Explanation',track_visibility='onchange')

# end of account_invoice()
