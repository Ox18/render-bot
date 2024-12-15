from django.urls import path, include

urlpatterns = [
    path('', include('web.urls')),
    path('', include('api.urls')),
]
