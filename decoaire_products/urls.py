from django.conf.urls import url, include
from . import views
from decoaire_products.models import Product,Image

""" REST """
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name','description', 'quantity', 'created_at', 'updated_at')

class ImageSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Image
        fields = ('product','route','image', 'created_at', 'updated_at')

# ViewSets
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all()
    serializer_class = ImageSerializer

# Routers
router = routers.DefaultRouter()
router.register(r'^', ProductViewSet)
router.register(r'^', ImageViewSet)

# URL

urlpatterns = [
    url(r'^', include(router.urls)),    
]