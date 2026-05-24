{
    'name': 'Sales Team Shared Access',
    'version': '16.0.1.0.0',
    'summary': 'Allow users to see quotations/orders of their sales team only',
    'category': 'Sales',
    'author': 'EISAC AUTOMATION',
    'website': 'https://www.eisac-automation.com/',
    'license': 'LGPL-3',
    'images': ['static/description/icon.png'], 
    'depends': ['crm', 'sale'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
    ],
    'installable': True,
    'application': False,
}
