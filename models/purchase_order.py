# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    wp_proyecto = fields.Selection([('nuevo_laminador_hsm_amlc','Nuevo Laminador HSM AMLC')])
