# -*- coding: utf-8 -*-
from odoo import fields, models


class ProductProduct(models.Model):
    """inherit the product template model and add brand field in there"""
    _inherit = 'product.product'

    brand = fields.Char(string='Brand')
