# -*- coding: utf-8 -*-
from odoo import fields, models


class stock_move(models.Model):
    _inherit = "stock.move"

    date = fields.Datetime(string="Move Date")

# end of stock_move()
