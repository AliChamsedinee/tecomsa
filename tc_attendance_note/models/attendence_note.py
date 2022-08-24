from odoo import fields, models, api

class business(models.Model): 
    _inherit = "hr.attendance"

    note = fields.Char()