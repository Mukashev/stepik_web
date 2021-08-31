from django.urls.conf import path
from django.urls.resolvers import URLPattern
from qa.views import user_login, user_logout, user_signup, ask, popular, new, test, main, question


urlpatterns = [
    path('', main, name='urls_home'),
    path('login/', user_login, name='urls_login'),
    path('logout/', user_logout, name='urls_logout'),
    path('signup/', user_signup, name='urls_signup'),
    path('question/<int:question_id>/', question, name='urls_question'),
    path('ask/', ask, name='urls_ask'),
    path('popular/', popular, name='urls_popular'),
    path('new/', new),
]