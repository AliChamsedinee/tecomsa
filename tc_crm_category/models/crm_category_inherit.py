from typing_extensions import Required
from odoo import api, fields, models

class CrmCategoryInherit(models.Model):
    _inherit = 'crm.lead'

    category = fields.Many2one('crm.category')