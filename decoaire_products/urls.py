from django.conf.urls import url, include
# import views
from decoaire_products.models import Product

# """ REST """
from rest_framework import routers, serializers, viewsets
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

# Serializers
class ProductSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Product
		fields = ('id', 'name', 'description', 'cloth_type', 'size', 'created_at', 'updated_at')

# ViewSets
class ProductViewSet(viewsets.ModelViewSet):
	queryset = Product.objects.all()
	serializer_class = ProductSerializer

# Routers
router = routers.DefaultRouter()
router.register(r'products', ProductViewSet)

# URL
urlpatterns = [
    url(r'^', include(router.urls)),
]
