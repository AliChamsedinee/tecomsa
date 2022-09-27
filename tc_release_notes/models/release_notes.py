from odoo import fields, models

class ReleaseNotes(models.Model): 


    _name = "release.notes"
    _inherit = ["mail.thread","mail.activity.mixin"]

    name = fields.Char("Name",required=True)
    date = fields.Date("Date",required=True)
    project = fields.Many2one("project.project",required=True)
    task = fields.Many2one("project.task",required=True)
    state = fields.Selection(
        [("dev","Dev"),
         ("stage","Stage"),
         ("production","Production")]
         ,default="dev"
        ,required=True
    )
    description = fields.Html("Description")


    def to_dev(self,records):
        for record in records:
            record.state = 'dev'


    def to_stage(self,records):
        for record in records:
            record.state = 'stage'


    def to_production(self,records):
        for record in records:
            record.state = 'production'
