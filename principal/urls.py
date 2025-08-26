from django.urls import path
from . import views

app_name = 'casas'

urlpatterns = [
    path('', views.principal, name='Principal'),
    path('listas/', views.lista_casas, name='lista_casas'),
    path('admin/', views.admin_lista_casas, name='admin_lista_casas'),
    path('crear/', views.crear_casa, name='crear_casa'),
    path('detalles/<int:pk>/', views.detalles_casa, name='detalles_casa'),  
    path('editar/<int:pk>/', views.editar_casa, name='editar_casa'),
    path('eliminar/<int:pk>/', views.eliminar_casa, name='eliminar_casa'),
    path('contacto/', views.contacto, name="Contacto"),
    path('blog/', views.blog, name="Blog"),
    path('opiniones/', views.todas_opiniones, name='todas_opiniones'),
    path("promociones/", views.lista_promociones, name="lista_promociones"),
    path("promociones/crear/", views.crear_promocion, name="crear_promocion"),
    path("promociones/eliminar/<int:promocion_id>/", views.eliminar_promocion, name="eliminar_promocion"),
]
