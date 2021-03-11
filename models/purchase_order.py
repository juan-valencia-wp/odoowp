# -*- coding: utf-8 -*-
from odoo import models, fields, api

class PurchaseOrder(models.Model):
    _inherit = "purchase.order"

    wp_proyecto = fields.Selection(
        string="Proyecto",
        selection=[('nuevo_laminador_hsm_amlc',"Nuevo Laminador HSM AMLC"),]
    )
