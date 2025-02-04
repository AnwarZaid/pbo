from django.contrib import admin
from django.urls import path
from .views import home, buat_proyek, cari_freelance, kelola_proyek, penilaian, create_project

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('buat_proyek/', buat_proyek, name='buat_proyek'),
    path('cari_freelancer.html', cari_freelance, name='cari_freelancer'), 
    path('kelola.html', kelola_proyek, name='kelola'),  
    path('penilaian.html', penilaian, name='penilaian'),  
    path('new/', create_project, name='create_project'),
]
