{
    'name': "rpg_demo",

    'summary': "Generació de dades de demostració RPG",

    'description': """
        Mòdul de demostració de personatges RPG.
        Inclou imatges, referències, dates calculades
        i relacions Many2many.
    """,

    'author': "antuan",
    'website': "https://www.yourcompany.com",

    'category': 'Games',
    'version': '0.1',

    'depends': ['base'],

    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

    'installable': True,
    'application': True,
}
