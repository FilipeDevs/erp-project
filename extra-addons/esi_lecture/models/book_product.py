from odoo import models, fields, api


class BookProduct(models.Model):
    _inherit = 'product.template'

    book_ids = fields.Many2many(
        'esi_lecture.book', string='Books', ondelete='cascade')

    # Ce field controle la visibilité des infos de stock du produit sur la vue.
    # Il est mis à True, pour s'assurer que les infos de stock seront
    # bien visibles sur la vue herité...
    show_on_hand_qty_status_button = fields.Boolean(
        default=True, readonly=True)
