from odoo import fields, models, api

class business_contact(models.Model): 
    _inherit = "res.partner"

    customer_line_of_business = fields.Many2one('line.of.business')
    Supplier_line_of_business = fields.Many2one('line.of.business')
