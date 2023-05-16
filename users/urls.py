from django.urls import path,include
from .views import *

urlpatterns = []
from users.urls import *
urlpatterns += [
    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-orders',GetOrdersView.as_view()),
]