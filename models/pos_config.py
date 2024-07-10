from odoo import fields, models


class PosConfig(models.Model):
    _inherit = 'pos.config'

    discount_availability = fields.Boolean()
    limit_categ_ids = fields.Many2many('pos.category','pos_limit_rel','pos_categ_id','limit_ids',)
    discount_limit = fields.Float()



