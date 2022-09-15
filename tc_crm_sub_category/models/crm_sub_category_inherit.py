from asyncio.windows_events import NULL
from odoo import api, fields, models
import logging
class CrmSubCategoryInherit(models.Model):
    _inherit = 'crm.lead'

    sub_category = fields.Many2one('crm.sub.category')

    @api.onchange('category')
    def _onchange_lead_category(self):
        for record in self:
            record.sub_category = NULL
        