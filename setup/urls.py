from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
#from tarefas.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tarefas/', include('tarefas.urls')),
    path('usuarios/', include('usuarios.urls')),
    path('', RedirectView.as_view(url='/usuarios/'), name='login')
]
