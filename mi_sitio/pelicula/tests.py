from django.test import TestCase
from django.urls import reverse


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
        resp = self.client.post("/genero/crear/", {"codigo":1, "descripcion":
                                                   "anime"})
        self.assertEqual(resp.status_code, 302)
        self.assertRedirects(resp, "/genero/")





