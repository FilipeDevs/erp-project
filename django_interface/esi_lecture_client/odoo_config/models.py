from django.db import models


class OdooConfiguration(models.Model):
    odoo_username = models.CharField(max_length=255)
    odoo_password = models.CharField(max_length=255)
    odoo_url = models.URLField()
    odoo_database = models.CharField(max_length=255)

    def __str__(self):
        return self.name
