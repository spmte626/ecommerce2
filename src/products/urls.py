from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

#from .views import product_detail_view_func # this is for function based views
from .views import ProductDetailView, ProductListView

urlpatterns = [
    # Examples:
    # url(r'^$', newsletter.views.home, name='home'),
    # url(r'^contact/$', newsletter.views.contact, name='contact'),
    # url(r'^about/$', ecommerce2.views.about, name='about'),
    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    # url(r'^products/', include('products.urls')),

    url(r'^$', ProductListView.as_view(), name='products'),
    url(r'^(?P<pk>\d+)/$', ProductDetailView.as_view(), name='product_detail'),
    # url(r'^(?P<id>\d+)', product_detail_view_func, name='product_detail_view'),

]

