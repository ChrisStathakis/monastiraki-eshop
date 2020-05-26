"""myeshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    # path('paypal/', include('paypal.standard.ipn.urls')),

    # admin  dashboard
    path('', include('frontend.urls')),
    path('dashboard-catalogue/', include('catalogue.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('dashboard-pos/', include('point_of_sale.urls')),
    path('dashboard-cart/', include('cart.urls')),
    path('dashboard-voucher/', include('voucher.urls')),
    path('dashboard-settings/', include('site_settings.urls')),
    path('dashboard-newsletter/', include('newsletter.urls')),
    path('dashboard-contact/', include('contact.urls')),
    path('dashboard-size-chart/', include('chartsize.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
