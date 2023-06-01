from django.urls import path,include
from .views import *

urlpatterns = []
from users.urls import *
urlpatterns += [
    path('get-all-students',GetStudentsView.as_view()),
    path('get-and-save-orders',GetOrdersView.as_view()),
    path('delete-students/<int:pk>',DeleteStudentView.as_view()),
    path('students-details-address/<int:pk>',StudentDetailsAddressView.as_view()),
    path('delete-address/<int:pk>',StudentAddressDeleteView.as_view()),
]