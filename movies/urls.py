from django.urls import path
from .views import home_page, create, edit


urlpatterns = [
    path('', home_page, name='home_page'),
    path('create/', create, name='create'),
    # Here <str:movie_id> tell us about the movie id
    # Here name attribute is the friendly name what I will use in the template
    path('edit/<str:movie_id>', edit, name='edit')
]
