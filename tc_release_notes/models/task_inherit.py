from odoo import fields, models, api

class TaskInherit(models.Model): 
    _inherit = 'project.task'

    # release_note = fields.Many2one('release.notes',string="Release Note")
    release_notes = fields.One2many('release.notes', 'task')