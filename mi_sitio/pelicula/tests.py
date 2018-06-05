from django.test import TestCase
from django.urls import reverse

from faker import Faker


from . import models
from . import views

# Create your tests here.


class Test(TestCase):
    def test_IndexView(self):
        url = reverse("Index")
        resp = self.client.get(url)

        self.assertEqual(resp.status_code, 200)


# Creamos algunos generos

    def test_crear_generos(self):
        fake = Faker()
        max = 10
        for index in range(max):
            resp = self.client.post(
                "/genero/crear/", {"codigo": index, "descripcion": fake.name()})
            self.assertEqual(resp.status_code, 302)
            self.assertRedirects(resp, "/genero/")
