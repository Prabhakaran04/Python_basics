from django.urls import path
from book_api.views import book_list, book_create, book_get_pk, book_put_pk, book_delete_pk

urlpatterns = [
    path('list/', book_list),
    path('add/', book_create),
    path('<int:pk>', book_get_pk),
    path('put/<int:pk>', book_put_pk),
    path('delete/<int:pk>', book_delete_pk)

]
