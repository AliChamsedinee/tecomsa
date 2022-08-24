from odoo import fields, models, api

class business(models.Model): 
    _name = "line.of.business"
    _description = "Library Member"

    name = fields.Char("Name",required=True)
    code = fields.Char("Code",readonly=True)
    # contact_code = fields.Many2one('line.of.business.code')

    @api.model
    def create(self,values):


        new_record = super(business,self).create(values)

        new_record.code = str(new_record.name).upper()
        new_record.code = str(new_record.code).replace(' ', '_')

        return new_record
