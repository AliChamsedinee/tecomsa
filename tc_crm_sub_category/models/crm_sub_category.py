from typing_extensions import Required
from odoo import api, fields, models

class CrmSubCategory(models.Model):
    _name = "crm.sub.category"

    name = fields.Char(string="Name",Required=True)
    code = fields.Char(string="Code",readonly=True)
    category = fields.Many2one('crm.category',Required=True)

    @api.model
    def create(self,values):

        new_record = super(CrmSubCategory,self).create(values)

        new_record.code = str(new_record.name).upper()
        new_record.code = str(new_record.code).replace(' ', '_')

        return new_record

        

