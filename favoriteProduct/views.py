from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import Favorite, Customer
from rest_framework import viewsets
from .data import fill_in_favorites
from .serializers import FavoriteSerializer, CustomerSerializer, FavoriteProductsSerializer


class CustomersViewSet(viewsets.ModelViewSet):
    '''
    API Cliente Luizalabs
    '''
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    @action(detail=True, methods=['GET'])
    def favorites(self, request, pk=None):
        try:
            get_object_or_404(Customer, pk=pk)

            # consulta os favoritos no banco e os preenche com
            # os dados do produto diretamente da api ou do cache
            favorites = Favorite.objects.filter(customer_id=pk)
            favorites_products = fill_in_favorites(favorites)

            # caso necessário, fatia o resultado em páginas
            page = self.paginate_queryset(favorites_products)
            if page is not None:
                serializer = FavoriteProductsSerializer(page, many=True)
                return self.get_paginated_response(serializer.data)

            # caso não haja paginação, retorna a lista inteira
            serializer = FavoriteProductsSerializer(favorites_products, many=True)
            return Response(status=200, data={'favorites': serializer.data})
        except ValidationError as err:
            return Response(status=400, data={'detail': str(err)})

class FavoritesViewSet(viewsets.ModelViewSet):
    '''
    API Favoritos Luizalabs
    '''
    queryset = Favorite.objects.all()
    serializer_class = FavoriteSerializer