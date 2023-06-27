from django.contrib import admin
from django.urls import path, include, reverse_lazy
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic.base import RedirectView


urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('admin:index'))),
    path('api/products/', include('products.urls')),
    path('api/accounts/', include('useraccounts.urls')),
    path('admin/', admin.site.urls),
] 

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


