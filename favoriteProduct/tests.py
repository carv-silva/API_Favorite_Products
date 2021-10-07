from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Customer, Favorite

'''OBS: caso queria realizar o test, voltar as configuracoes do banco sqlite no src/settings.py que estao comentadas '''

class CustomerTests(APITestCase):
   def setUp(self):
      User.objects.create_superuser('root', '	root@gmail.com', 'root')
      self.customer = Customer.objects.create(
         name='cliente Teste do Case', email='clienteteste@gmail.com')
      url = reverse('token_obtain_pair')
      data = {"username": "root", "password": "root"}
      response = self.client.post(url, data, format='json')
      self.token = response.data['access']
      self.client.credentials(HTTP_AUTHORIZATION='Bearer' + self.token)

    def test_token_invalid_credentials(self):
        url = reverse('token_obtain_pair')
        data = {"username": "admin", "password": "admin"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_customer_create(self):
        url = reverse('customers-list')
        data = {"name": "cliente Teste do Case02",
                "email": "teste02@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_customer_create_duplicated_email(self):
        url = reverse('customers-list')
        data = {"name": "cliente Teste do Case",
                "email": "clienteteste@gmail.com"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_customer_details(self):
        url = reverse('customers-detail', kwargs={'pk': self.customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_details_invalid_id(self):
        url = reverse('customers-detail', kwargs={'pk': 'pedro'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_customer_update(self):
        data = {"name": "cliente Teste do Case ATUALIZADO",
                "email": "clienteteste@gmail.com"}
        url = reverse('customers-detail', kwargs={'pk': self.customer.id})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_update_invalid_id(self):
        data = {"name": "cliente Teste do Case ATUALIZADO",
                "email": "clienteteste@gmail.com"}
        url = reverse('customers-detail', kwargs={'pk': 'ana'})
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_customer_delete(self):
        url = reverse('customers-detail', kwargs={'pk': self.customer.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_customer_delete_invalid_id(self):
        url = reverse('customers-detail', kwargs={'pk': 'joao'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_favorite_create(self):
        url = reverse('favorites-list')
        data = {"product_id": "a96b5916-9109-5d2e-138a-7b656efe1f92",
                "customer": self.customer.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_favorite_create_duplicated_product(self):
        Favorite.objects.create(
            product_id="a96b5916-9109-5d2e-138a-7b656efe1f92", customer=self.customer)
        url = reverse('favorites-list')
        data = {"product_id": "a96b5916-9109-5d2e-138a-7b656efe1f92",
                "customer": self.customer.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_favorite_create_invalid_product(self):
        url = reverse('favorites-list')
        data = {"product_id": "00", "customer": self.customer.id}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_favorite_delete(self):
        fav = Favorite.objects.create(
            product_id="a96b5916-9109-5d2e-138a-7b656efe1f92", customer=self.customer)
        url = reverse('favorites-detail', kwargs={'pk': fav.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_favorite_delete_invalid_id(self):
        url = reverse('favorites-detail', kwargs={'pk': 'carlos'})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_customer_favorites(self):
        url = reverse('customers-favorites', kwargs={'pk': self.customer.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_customer_favorites_nonexistent_customer(self):
        url = reverse('customers-favorites', kwargs={'pk': '111111'})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
