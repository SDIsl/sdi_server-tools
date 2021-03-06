# © 2019 SDi Soluciones Informáticas
# Author: Oscar Soto <osoto@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from odoo import http
from odoo import api, fields, models


class Backup(models.TransientModel):
    _name = 'backup.manually.backup'
    _description = 'Do backup manually'

    def _default_bbdd(self):
        bbdd = []
        for bd in http.db_list(True, None):
            bbdd.append((bd, bd))
        return bbdd

    bbdd = fields.Selection(
        string='Select a database',
        selection=_default_bbdd,)
    compression_format = fields.Selection(
        string='Compression format',
        selection=[('zip', 'zip')],
        default="zip")

    @api.multi
    def create_request(self):
        url = '/web/binary/download_db?name=%s&backup_format=%s' % (
            self.bbdd, self.compression_format)
        res = dict(type='ir.actions.act_url', url=url, target='new')
        return res
