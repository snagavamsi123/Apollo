from django.urls import path
from . import views

urlpatterns = [
    path('home/',views.home,name='home'),
    path('userlogin',views.UserLogin,name='userlogin'),
    path('adminlogin',views.AdminLogin,name='adminlogin'),
    path('signup',views.signuppage,name='signup'),
    path('newticket',views.newticket,name='newticket'),
    path('oldtickets',views.oldtickets,name='oldtickets'),
    path('alltickets',views.admin_all,name='admin_all'),
    path('editticket/<int:id>',views.editticket,name='editticket'),
    path('admin_editticket/<int:id>',views.AdminEditTicket,name='AdminEditTicket'),
]