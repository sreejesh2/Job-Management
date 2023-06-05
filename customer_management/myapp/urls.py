from django.urls import path
from  . import views

urlpatterns = [
   # path('part-number/add/',views.PartCreateView.as_view(),name='part-number'),
   path('job/add/',views.create_job,name='add-job'),
   path('part/add/',views.create_part,name='part-add'),
]
