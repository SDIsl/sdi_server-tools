# © 2019 SDi Soluciones Informáticas
# Author: Oscar Soto <osoto@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
{
    'name': 'SDi-Server-Tools: Backups Manually',
    'version': '11.0.1.0.1',
    'category': 'server-tools',
    'summary': """
            Do backups from the backend manually.
        """,
    'author': 'Oscar Soto',
    'license': 'AGPL-3',
    "website": "http://www.sdi.es",
    'depends': [
        'base',
    ],
    'data': [
        'security/ir.model.access.csv',
        'wizards/backup.xml',
    ],
    'installable': True,
    'application': False,
}