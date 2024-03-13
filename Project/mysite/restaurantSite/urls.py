from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("menuPage/" or "menupage/", include("menuPage.urls")),
    path("", include("menuPage.urls")),
    path("admin/", admin.site.urls),
]