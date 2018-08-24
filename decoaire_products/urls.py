from django.conf.urls import url, include
# import views
from decoaire_products.models import Product, Image

# """ REST """
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers


class ProductSerializer(serializers.HyperlinkedModelSerializer):
	"""Product Selializer"""
	class Meta:
		model = Product
		fields = ('name', 'description', 'quantity', 'size', 'cloth_type',
                  'image_ppal', 'created_at', 'updated_at')


class ImageSerializer(serializers.HyperlinkedModelSerializer):
	"""Image Selializer"""
	class Meta:	
		model = Image
		fields = ('product', 'route', 'image', 'created_at', 'updated_at')

# ViewSets


class ProductViewSet(viewsets.ModelViewSet):
	"""Product view"""
	queryset = Product.objects.all()
	serializer_class = ProductSerializer


class ImageViewSet(viewsets.ModelViewSet):
	"""Image view"""
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
