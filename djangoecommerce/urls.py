"""djangoecommerce URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from accounts.views import signup, show_profile
from products.views import product_list, product_detail
from cart.views import added_to_cart, view_cart, remove_from_cart



from django.views.static import serve
from django.conf import settings



urlpatterns = [
    path('media/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    path('admin/', admin.site.urls),
    path('',product_list, name="product_list"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/profile', show_profile, name="profile"),
    path('signup/', signup, name="signup"),
    path('product_detail/<int:id>',product_detail, name='product_detail'),
    path('cart/add/', added_to_cart, name="added_to_cart"),
    path('view_cart/', view_cart, name="view_cart"),
    path('cart/remove/', remove_from_cart, name="remove_from_cart")
]
