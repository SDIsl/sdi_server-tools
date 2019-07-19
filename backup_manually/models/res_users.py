from odoo import api, fields, models


class ResUsers(models.Model):
    _inherit = 'res.users'

    @api.multi
    def backup_manually(self, ):
        self.ensure_one()
        report = self.env['ir.actions.window'].search(
            [('report_name', '=', report_name),
             ('report_type', '=', report_type)], limit=1)
        return report(self)


