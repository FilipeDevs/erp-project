from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    book_ids = fields.Many2many('esi_lecture.book', string='Books')
    is_author = fields.Boolean(string="Is Author")
