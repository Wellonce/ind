from django.urls import path


from .views import HomePageView, MalibuView, GentraView, CobaltView, NexiaView, MalibuCreateView, Gentra_detailview, Cobalt_detailview, Nexia_detailview, UserRegisterView, LoginView
from django.views.generic import TemplateView

app_name = 'myapp'

urlpatterns = [
    path('', HomePageView.as_view(), name = 'home-page'),
    path('malibu/', MalibuView.as_view(), name = 'malibu'),
    path('gentra/', GentraView.as_view(), name = 'gentra'),
    path('cobalt/', CobaltView.as_view(), name = 'cobalt'),
    path('nexia/', NexiaView.as_view(), name = 'nexia'),
    path('malibu/sale', MalibuCreateView.as_view(), name= 'malibu-sale'),
    path('gentra/sale', Gentra_detailview.as_view(), name = 'gentra-sale'),
    path('cobalt/sale', Cobalt_detailview.as_view(), name = 'cobalt-sale'),
    path('nexia/sale', Nexia_detailview.as_view(), name = 'nexia-sale'),
    path('buy/', TemplateView.as_view(template_name='cars_on_sale.html'), name = 'all-sale'),
    path('register/', UserRegisterView.as_view(), name = 'register-page'),
    path('login/', LoginView.as_view(), name = 'login-page'),

]





