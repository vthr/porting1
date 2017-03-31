# -*- coding: utf-8 -*-

from odoo import fields, models, api


class quotation_follower_wizard(models.TransientModel):
    _name = "quotation.follower.wizard"

    action_description = fields.Text('Action')

    @api.multi
    def confirm(self):
        if self.env.context.get('active_id', False):
            sale_obj = self.env['sale.order']
            active_id = self._context.get('active_id', False)
            sale_ids = sale_obj.browse(active_id)

            value = sale_ids.fal_action_counter + 1
            sale_ids.message_post(
                body=self.action_description
            )
            sale_ids.write(
                {'fal_action_counter': value}
            )
        return {'type': 'ir.actions.act_window_close'}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
