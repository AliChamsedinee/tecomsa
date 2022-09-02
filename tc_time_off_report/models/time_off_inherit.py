from odoo import api, fields, models
from odoo.exceptions import ValidationError

class HrEmployeeInherited(models.Model):
    _inherit = "hr.employee"

    def to_view(self, records):

        # view_id = self.env.ref('view_form_time_off').id
        return {
            'type': 'ir.actions.act_window',
            'name' : 'Export employee time off',
            'res_model': 'export.time.off',
            'target': 'new',
            'view_mode' : 'form',
            # 'view_id' : view_id,
            'context' : {'default_selected_employees':[(6,0,records.ids)]}
        }