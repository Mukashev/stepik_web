from django.urls.conf import path
from django.urls.resolvers import URLPattern
from qa.views import test

urlpatterns = [
    path('', test, name='test'),
    path('<int:id>/', test, name='test'),
]