from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('index/', views.IndexView.as_view()),
    path('index/products/<int:product_id>/', views.ProductDetailView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
