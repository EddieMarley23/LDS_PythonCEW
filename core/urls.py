from django.urls import path # type: ignore
from .views import home, save, update, updating, delete,register,login
from django.conf import settings # type: ignore
from django.conf.urls.static import static # type: ignore

urlpatterns = [
    path('home', home, name='home'),
    path('save', save, name='save'),
    path('update/<int:id>', update, name='update'),
    path('updating/<int:id>', updating, name='updating'),
    path('delete/<int:id>', delete, name='delete'),
    path('register/', register, name='register'),
    path('login/', login ,name = 'login'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
