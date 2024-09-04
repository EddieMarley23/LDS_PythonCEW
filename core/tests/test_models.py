from django.test import TestCase # type: ignore
from ..models import Car


class CarTestCase(TestCase):
    def test_can_create_car_with_valid_data(self):
        vmodel = 'test'
        vbrand = 'test'
        vplate = 'test'
        vname = 'test'
        vowner = 1
        # Assumindo que o caminho da imagem é relativo à pasta media
        photo_path = 'images/test_image.jpg'
        carTest = Car(model=vmodel, brand=vbrand, plate=vplate, name=vname, photo=photo_path, createdby=vowner, like=0)
        carTest.save()
        self.assertEqual(carTest.model, 'test')

    # Cria o objeto Car e associa a imagem
      