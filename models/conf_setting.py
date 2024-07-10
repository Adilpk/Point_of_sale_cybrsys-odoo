from odoo import api, fields, models


class ConfSetting(models.TransientModel):
    _inherit = "res.config.settings"

    pos_discount_availability = fields.Boolean(
        related='pos_config_id.discount_availability',
        string='Discount Available', readonly=False)
    pos_limit_categ_ids = fields.Many2many('pos.category',
                                                 string='Available PoS Product Categories',
                                                 readonly=False,related='pos_config_id.limit_categ_ids')
    pos_discount_limit = fields.Float(related='pos_config_id.discount_limit',
                                      string='Discount Limit', readonly=False)


