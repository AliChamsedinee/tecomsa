from typing_extensions import Required
from odoo import api, fields, models

class CrmCategory(models.Model):
    _name = "crm.category"

    name = fields.Char(string="Name",Required=True)
    code = fields.Char(string="Code",readonly=True)

    @api.model
    def create(self,values):


        new_record = super(CrmCategory,self).create(values)

        new_record.code = str(new_record.name).upper()
        new_record.code = str(new_record.code).replace(' ', '_')

        return new_record

