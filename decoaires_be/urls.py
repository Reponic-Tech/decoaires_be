"""decoaires_be URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.http import HttpResponse
from smtplib import SMTPException

from rest_framework import routers, serializers, viewsets

from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from decoaire_products.urls import ProductViewSet

# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url', 'username', 'email', 'is_staff')

# ViewSets define the view behavior.
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


def sendBudget(request):

	try:
		send_mail(
                    'Testing budget',
               					'Your budget is.',
               					'arcela34@gmail.com',
               					['decoairesbe@yopmail.com'],
               					fail_silently=False,
                )

	except SMTPException as e:
		HttpResponse('There was an error sending an email: ', e)

	return HttpResponse('Budget')

# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'products', ProductViewSet)


urlpatterns = [
   url(r'^', include(router.urls)),
	url(r'^admin/', admin.site.urls),
   url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),	
	url(r'^sendBudget/$', sendBudget, name='sendBudget'),
]
