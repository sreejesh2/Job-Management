from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views

router=DefaultRouter()

router.register('job',views.JobViewSet,basename='job')
router.register('parts',views.PartFullFormViewSet,basename='parts')

urlpatterns = [
   
    #  path('jobs/create/', views.JobCreateView.as_view({'post': 'create'}), name='create_job'),
    # path('jobs/list/', views.JobListView.as_view({'get': 'list'}), name='list_jobs'),
]+router.urls
