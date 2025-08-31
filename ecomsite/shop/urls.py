from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns=[
    path('', views.index, name='index'),
    path('<int:id>/', views.detail, name='detail'),
    path('checkout/', views.checkout, name='checkout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
