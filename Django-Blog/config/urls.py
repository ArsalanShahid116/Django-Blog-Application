from django.contrib import admin
from django.urls import path, include

import blog.urls 
import account.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls', namespace='blog')),
    path('account/', include('account.urls')),
]
