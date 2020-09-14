# © 2019 SDi Soluciones Informáticas
# Author: Oscar Soto <osoto@sdi.es>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

{
    'name': 'SDi-Tools: Backup Manually',
    'version': '11.0.1.0.1',
    'category': 'server-tools',
    'summary': """
            Do backups, from the backend, manually.
        """,
    'author': 'Oscar Soto',
    'license': 'AGPL-3',
    "website": "http://www.sdi.es",
    'depends': [
        'web',
    ],
    'data': [
        'security/backup_manually_security.xml',
        'security/ir.model.access.csv',
        #'wizards/backup.xml',
        'views/web_client_menu.xml',
    ],
    'qweb':[
        'static/src/xml/backup_manually_user_menu.xml',
    ],
    'installable': True,
    'application': False,
}
