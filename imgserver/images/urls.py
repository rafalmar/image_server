from django.urls import include, path
from .views import image_mixin_view
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', image_mixin_view),
    path('<int:pk>/', image_mixin_view)
]