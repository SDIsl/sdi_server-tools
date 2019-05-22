from odoo import api, fields, models


class ResPartner(models.Model):
    _inherit = 'res.partner'

    @api.multi
    def update_geonames(self):
        for record in self:
            try:
                if record.zip:
                    objts = self.env['res.better.zip'].search([
                                        ('name', 'ilike', record.zip)
                                    ])
                    record.zip_id = objts[0] or False
            except:
                print("##### err init:")
                print(record.zip)
                print(record.name)
                print("##### err end")
