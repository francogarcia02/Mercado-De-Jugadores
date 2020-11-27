from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from config import settings




urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('jet/', include('jet.urls', 'jet')),
]




