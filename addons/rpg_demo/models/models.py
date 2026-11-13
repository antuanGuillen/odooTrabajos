# from odoo import models, fields, api


# class rpg_demo(models.Model):
#     _name = 'rpg_demo.rpg_demo'
#     _description = 'rpg_demo.rpg_demo'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100



from odoo import models, fields


class RPGHabilitat(models.Model):
    _name = 'rpg.habilitat'
    _description = 'Habilitats RPG'

    name = fields.Char(string='Nom', required=True)
    descripcio = fields.Text(string='Descripció')
    nivell = fields.Integer(string='Nivell')


class RPGFaccio(models.Model):
    _name = 'rpg.faccio'
    _description = 'Faccions RPG'

    name = fields.Char(string='Nom', required=True)


class RPGHeroi(models.Model):
    _name = 'rpg.heroi'
    _description = 'Herois RPG'

    name = fields.Char(string='Nom del personatge', required=True)

    imatge = fields.Image(string='Imatge')

    data_creacio = fields.Date(string='Data de creació')

    faccio_id = fields.Many2one(
        'rpg.faccio',
        string='Facció'
    )

    habilitat_ids = fields.Many2many(
        'rpg.habilitat',
        string='Habilitats'
    )


class RPGAvaluador(models.Model):
    _name = 'rpg.avaluador'
    _description = 'Avaluador RPG'

    nom_model = fields.Char(
        string='Nom del model',
        required=True
    )

    ext_id = fields.Char(
        string='External ID',
        required=True
    )

    requisit = fields.Selection(
        [
            ('img', 'Imatge'),
            ('ref', 'Referència'),
            ('dat', 'Data Calculada'),
            ('m2m', 'Relació Many2many'),
        ],
        string='Requisit',
        required=True
    )


