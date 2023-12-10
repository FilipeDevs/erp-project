from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from xmlrpc import client


class IndexView(TemplateView):
    template_name = "books/index.html"


def search_books(request):
    if 'odoo_config' not in request.session:
        messages.error(request, "Veuillez d'abord vous connecter à ODOO !")
        return redirect('odoo_config:index')

    odoo_config = request.session['odoo_config']
    common_proxy = client.ServerProxy(
        f"{odoo_config['odoo_url']}/xmlrpc/2/common")

    try:
        uid = common_proxy.authenticate(
            odoo_config['odoo_database'], odoo_config['odoo_username'], odoo_config['odoo_password'], {})
    except Exception as e:
        messages.error(request, "Authentification échouée !")
        return redirect('odoo_config:index')

    # Récupération du nom de recherche de livres depuis les paramètres de la requête GET
    book_records = request.GET.get('name', '')
    books = []

    if book_records:
        models_proxy = client.ServerProxy(
            f"{odoo_config['odoo_url']}/xmlrpc/2/object")

        # Recherche des IDs de livres correspondant au terme de recherche
        book_ids = models_proxy.execute_kw(
            odoo_config['odoo_database'],
            uid,
            odoo_config['odoo_password'],
            'esi_lecture.book',
            'search',
            [[['name', 'ilike', book_records]]],
            # Tri par ordre décroissant
            {'order': 'likes_count DESC'}
        )

        # Récupération des données des livres
        books_data = models_proxy.execute_kw(
            odoo_config['odoo_database'],
            uid,
            odoo_config['odoo_password'],
            'esi_lecture.book',
            'read',
            [book_ids],
            {'fields': ['name', 'likes_count']}
        )

        # Construction de la liste de livres avec les données récupérées
        books = [{'title': book_data['name'], 'likes_count': book_data['likes_count']}
                 for book_data in books_data]

    return render(request, 'books/index.html', {'books': books})
