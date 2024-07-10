from odoo import fields, models


class PosCategory(models.Model):
    _inherit = 'pos.category'

    limit_amount = fields.Float()




