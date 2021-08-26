from django.urls.conf import path
from django.urls.resolvers import URLPattern
from qa.views import login, signup, ask, popular, new, test, main, question


urlpatterns = [
    path('', main, name='home'),
    path('login/', test),
    path('signup/', test),
    path('question/<int:question_id>/', question, name='urls_question'),
    path('ask/', test),
    path('popular/', popular, name='urls_popular'),
    path('new/', new),
]