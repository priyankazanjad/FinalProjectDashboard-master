from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/',views.dashboardView),
    path('addcus/',views.addcustomerview,name='add_cus'),
    path('detail/',views.customerdetailview)
]
