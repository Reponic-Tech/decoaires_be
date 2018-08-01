from django.conf.urls import url, include
from . import views
from decoaire_products.models import Product

""" REST """
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# urlpatterns = [
#     url(r'^$', views.index, name='index'),
# ]

# Serializers
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name',)

# ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

# Routers
router = routers.DefaultRouter()
router.register(r'^', ProductViewSet)

# URL

urlpatterns = [
    url(r'^', include(router.urls)),
]