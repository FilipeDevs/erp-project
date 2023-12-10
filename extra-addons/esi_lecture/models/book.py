# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError
from datetime import date


class Book(models.Model):
    _name = "esi_lecture.book"

    name = fields.Char(string='Title', required=True)
    description = fields.Html(string='Description')
    cover_image = fields.Binary(string='Cover Image')
    publication_date = fields.Date(
        string='Publication Date', default=fields.Date.today, required=True)
    page_count = fields.Integer(string='Page Number', required=True)
    authors = fields.Many2many('res.partner', string='Authors')

    likes_count = fields.Integer(
        string='Likes', compute='_compute_likes_count', store=True)

    likes = fields.Many2many('res.users', string='Likes')

    liked_book = fields.Boolean(string='Liked', compute='_compute_liked_book')

    like_message = fields.Char(
        string='Like Message', compute='_compute_like_message', store=True)

    # Méthode qui check si l'utilisateur a aimé le livre ou non
    @api.depends('likes')
    def _compute_liked_book(self):
        for book in self:
            user = self.env.user
            book.liked_book = user in book.likes

    # Méthode qui affiche un message si l'utilisateur a aimé le livre ou non
    @api.depends('liked_book')
    def _compute_like_message(self):
        for book in self:
            if book.liked_book:
                book.like_message = "Vous avez aimé ce livre"
            else:
                book.like_message = ""

    # Methode qui gere le "like/unlike" d'un livre
    def toggle_like(self):
        for book in self:
            user = self.env.user
            if user in book.likes:
                book.likes -= user
            else:
                book.likes += user

    # Méthode qui calcule le nombre de likes
    @api.depends('likes')
    def _compute_likes_count(self):
        for book in self:
            book.likes_count = len(book.likes)

    # ===== Contraintes =====

    @api.constrains('publication_date')
    def _check_publication_date(self):
        for book in self:
            if book.publication_date >= date.today():
                raise ValidationError(
                    "Date de publication doit être inférieure à la date d'aujourd'hui !")

    @api.constrains('page_count')
    def _check_page_count(self):
        for book in self:
            if book.page_count <= 0:
                raise ValidationError(
                    "Nombre de pages doit être supérieur à 0 !")

    _sql_constraints = [
        ('unique_name', 'UNIQUE(name)', 'Titre doit être unique !'),
    ]
