from django.urls import path
from . views import HomeView
from . views import AboutView
from . views import OfferView
from . views import ContactView
from django.conf import settings
from django.conf.urls.static import static
from . import views
# my urls

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('about', AboutView.as_view(), name='about'),
    path('contact', ContactView.as_view(), name='contact'),
    path('offers', OfferView.as_view(), name='offers'),
    path('register_user', views.register_user, name='register_user'),
    path('login_user', views.login_user, name='login_user'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)