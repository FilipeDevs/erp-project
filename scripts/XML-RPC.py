import xmlrpc.client


def authenticate_user(url, odoo_db, username, password):
    common_endpoint = f'{url}/xmlrpc/2/common'
    common_proxy = xmlrpc.client.ServerProxy(common_endpoint)
    user_id = common_proxy.authenticate(odoo_db, username, password, {})
    return user_id


url = "http://localhost:8069"
odoo_db = 'odoo'  # A modifier selon le cas

while True:
    odoo_username = input('Entrez votre login Odoo : ')
    odoo_password = input('Entrez votre mot de passe Odoo : ')

    user_id = authenticate_user(url, odoo_db, odoo_username, odoo_password)

    if user_id:
        print('Authentification réussi !')
        print('Vous pouvez chercher un livre maintenant.')
        break
    else:
        print('Authentification échoué !')

while True:
    book_title = input(
        'Entrez un nom de livre (tapez Enter pour sortir): ')

    if not book_title:
        print("Fermeture....")
        break

    models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

    book_ids = models.execute_kw(
        odoo_db,
        user_id,
        odoo_password,
        'esi_lecture.book',
        'search',
        [[['name', 'ilike', book_title]]]
    )

    if not book_ids:
        print(f'Aucun livre trouvé avec le titre : {book_title}')
    else:
        print('Livre(s) trouvé(s):')
        for book_id in book_ids:
            book_data = models.execute_kw(
                odoo_db,
                user_id,
                odoo_password,
                'esi_lecture.book',
                'read',
                [book_id],
                {'fields': ['name', 'publication_date']}
            )
            print(book_data)
