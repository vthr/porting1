# -*- coding: utf-8 -*-

from odoo import fields, models


class account_analytic_account(models.Model):
    _inherit = 'account.analytic.account'

    fal_is_business = fields.Boolean('Is Business?')

#end of account_analytic_account()

class sale_order(models.Model):
    _inherit = 'sale.order'

    project_fal_is_business = fields.Boolean(related='project_id.fal_is_business', string='Is Business?')

    def fal_refresh(self, cr, uid, ids, context=None):
        return True

#end of sale_order()
