from asyncio.windows_events import NULL
from odoo import api, fields, models
import logging
class CrmCategoryInherit(models.Model):
    _inherit = 'crm.lead'

    sub_category = fields.Many2one('crm.sub.category')

    # @api.onchange('category')
    # def _onchange_category(self):
    #     for record in self:
    #         logging.info("TESTTTTTTTTTTTTTTTTTTTTTTTT")
    #         if record.category: 
    #             logging.info("TESTTTTTTTTTTTTTTTTTTTTTTTT")
    #             self.sub_category = NULL
        