from django.urls import include, path
from rest_framework import routers
from .views import *

router = routers.DefaultRouter()

router.register(r'user',UserViewSet,basename='user')
router.register(r'details',UserDetailsViewSet,basename='userdetails')

urlpatterns = [
	path('', include(router.urls)),
	path('api-auth/', include('rest_framework.urls'))
]
