from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^$', home, name="home"),
    url(r'^signup/', signup, name="signup"),
    url(r'^login/', login, name="login"),
    url(r'^info_signup/', info_signup, name='info_signup'),
    url(r'^info_login/', info_login, name='info_login'),
    url(r'^active/', active, name='active'),
    # url(r'^game/', game, name='game'),
    url(r'^move/', move, name='move'),
]
