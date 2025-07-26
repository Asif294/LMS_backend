from django.urls import path 
from .views import Category_list_create,Course_list_create,course_details,Meterial_list_create,Enrollment_list_create,QuastionAnswer_list_create,Lessone_list_create

urlpatterns = [
    path('categories/',Category_list_create,name='Category_list_create'),
    path('courses/',Course_list_create,name='Course_list_create'),
    path('courses/<int:pk>/',course_details,name='course_details'),
    path('lessones/',Lessone_list_create,name='Lessone_list_create'),
    path('meterials/',Meterial_list_create,name='Meterial_list_create'),
    path('enrollments/',Enrollment_list_create,name='Enrollment_list_create'),
    path('questions/',QuastionAnswer_list_create,name='QuastionAnswer_list_create'),
]
