from odoo import fields, models, api

class ProjectInherit(models.Model): 
    _inherit = 'project.project'

    # release_note = fields.Many2one('release.notes',string="Release Note")
    release_notes = fields.One2many('release.notes', 'project')