
from django.urls import path
from validation import views

urlpatterns = [
   
    path('validation/',views.validation),
    path('Forms/',views.ShowFormData),
    path('serial/<int:inp>',views.student_detail),
    path('serial1/',views.student_detail1),
    path('success/',views.thankyou),
]
