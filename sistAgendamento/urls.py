from django.contrib import admin
from django.urls import path
from app.views import login, index, agdequipamento

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', login),
    path('index/', index, name="index"),
    path('agdequipamento/', agdequipamento, name="agdequipamento"),
]
