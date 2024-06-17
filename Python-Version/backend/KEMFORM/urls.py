from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('patientDetails/', views.patientDetails, name='patient-details'),
    path('patientScreening/', views.patientScreening, name='patient-screening'),
    path('demographicInfo/', views.demographicInfo, name='demographic'),
    path('currentIllnessInfo/', views.currentIllnessInfo, name='current-illness'),
    path('childrenInfo/', views.childrenInfo, name='children-info'),
    path('risksFactors/', views.risksFactors, name='risk-factors'),
]