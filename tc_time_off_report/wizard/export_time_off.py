from typing_extensions import Required
from odoo.exceptions import ValidationError
from odoo import api, fields, models

class wizard(models.TransientModel):
    _name = "time.off.export.wizard"

    start_date = fields.Date(string="Start Date", Required="True")
    end_date = fields.Date(string="End Date", Required="True")

    def button_pdf(self, records):
        # if not self.start_date and not self.end_date:
        #     raise ValidationError("Choose a start date and end date.")
        # elif not self.start_date:
        #     raise ValidationError("Choose a start date.")
        # elif not self.end_date:
        #     raise ValidationError("Choose a end date.")
        # else:
            selected_ids = self.env.context.get('active_ids', [])
            selected_records = self.env['hr.leave.allocation'].browse(selected_ids)
            ids = self.env['hr.leave.allocation'].search_read([('active','=',True)])
            # employees = ids['employee_id']
            data = {
                'form' : self.read()[0],
                'records' : records
            }
            return self.env.ref('tc_time_off_report.report_time_off').report_action(self, data=data)
            # return True

    def button_excel(self):
        if not self.start_date and self.end_date:
            raise ValidationError("Choose a start date and end date.")
        elif not self.start_date:
            raise ValidationError("Choose a start date.")
        elif not self.end_date:
            raise ValidationError("Choose a end date.")
        else:
            return True
