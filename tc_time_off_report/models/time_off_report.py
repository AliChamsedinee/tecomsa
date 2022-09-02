import string
from typing_extensions import Required
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging

class ExportTimeOff(models.TransientModel):
    _name = "export.time.off"
    

    date_from = fields.Date(string="Date from", Required="True")
    date_to = fields.Date(string="Date to", Required="True")
    selected_employees = fields.Many2many('hr.employee',string="Employees")

    def button_pdf(self):
        names = []
        logging.info("TESTTTTTTTTTTTTTTTTTTTTTTTT")
        for r in self.selected_employees:
            # logging.info("%s",r.name)
            names.append(r.name)
        logging.info("TESTTTTTTTTTTTTTTTTTTTTTTTT")
        types = []
        test = self.env['hr.leave'].search([])
        for type in test.holiday_status_id:
            types.append(type.display_name)
        data = {
                'form' : self.read()[0],
                'employees' : self.selected_employees,
                # 'names' : self.env['hr.employee'].search([])
                'names' : names,
                'type' : types
            }
        logging.info("Emplyoee")
        for r in data["employees"]:
            logging.info(r.name)

        return self.env.ref('tc_time_off_report.report_time_off').report_action(self, data)

    def button_excel(self):
        return True