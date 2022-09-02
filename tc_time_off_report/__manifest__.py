{
    "name": "Time off report",
    "summary": "Time off report",
    "author": "Daniel Reis",
    "license": "AGPL-3",
    "website": "https://github.com/PacktPublishing"
               "/Odoo-15-Development-Essentials",
    "version": "15.0.1.0.0",
    "category": "Services/Library",
    "depends": ["base","hr_holidays"],
    "data": [
        # "views/time_off_report.xml",
        "views/hr_employee.xml",
         "views/time_off_export_view.xml",
        # "security/report_security.xml",
        # "security/ir.model.access.csv",
        # "wizard/export_time_off_wizard.xml",
        "reports/report.xml",
        "reports/time_off_report.xml",
    ],
}