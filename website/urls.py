from django.urls import path, re_path, include
from . import views
from django.views.static import serve
from django.conf import settings
from django.contrib.auth.mixins import LoginRequiredMixin


from .views import ServiceDetailView

urlpatterns = [
    path('', views.index, name='index'),
    path('about_us/', views.about_us, name='about_us'),
    path('contact_us/', views.contact_us, name='contact_us'),
    path('blog/', views.blog, name='blog'),
    path('service_list/', views.ServiceListView.as_view(), name='service_list'),
    path('service_detail/<int:pk>', views.ServiceDetailView.as_view(), name='service_detail'),
    path('service/create/', views.ServiceCreate.as_view(), name='service_create'),
    path('invoice/create', views.InvoiceCreate.as_view(), name='invoice_create'),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('accounts/', include('django.contrib.auth.urls')),
    path('service/<int:pk>/', ServiceDetailView.as_view(), name='service_detail'),
    path('accounts/logged', include('django.contrib.auth.urls')),
    path('review/create/', views.ReviewCreate.as_view(), name='review_create'),
    path('blog/', views.blog, name='blog'),
    path('blog/create/', views.BlogCreateView.as_view(), name='blog_create'),  # URL for creating new blog posts
]
