from django.urls.conf import path
from django.urls.resolvers import URLPattern
from qa.views import test

urlpatterns = [
    path('<int:id>/', test, name='test'),
]