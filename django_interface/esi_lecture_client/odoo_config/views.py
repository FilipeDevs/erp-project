from django.shortcuts import render, get_object_or_404
from .models import OdooConfiguration
from .forms import OdooConfigForm
from django.views.generic import ListView
from django.http import HttpResponseRedirect
from django.urls import reverse
from xmlrpc import client
from django.contrib import messages


class IndexView(ListView):
    model = OdooConfiguration
    template_name = "odoo_config/index.html"
    context_object_name = 'configuration'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['form'] = OdooConfigForm
        return context


def test_connect(request):
    form = OdooConfigForm(request.POST or None)

    if form.is_valid():
        odoo_config = form.cleaned_data

        common_proxy = client.ServerProxy(
            f"{odoo_config['odoo_url']}/xmlrpc/2/common")

        try:
            uid = common_proxy.authenticate(
                odoo_config['odoo_database'], odoo_config['odoo_username'], odoo_config['odoo_password'], {})

            if (uid == False):
                messages.error(request, "Authentification échouée !")
                return HttpResponseRedirect(reverse('odoo_config:index'))

             # Enregistrement des informations de connexion dans la session
            request.session['odoo_config'] = {
                'odoo_url': odoo_config['odoo_url'],
                'odoo_database': odoo_config['odoo_database'],
                'odoo_username': odoo_config['odoo_username'],
                'odoo_password': odoo_config['odoo_password'],
            }

            messages.success(
                request, "La connexion a réussi ! Vous etes connecté !")

        except Exception as e:
            messages.error(request, "La connexion a échoué !")

    else:
        messages.error(request, "Échec de la connexion : formulaire invalide")

    return HttpResponseRedirect(reverse('odoo_config:index'))
