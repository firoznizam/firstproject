from django.urls import path
from projapp1 import views
#app_name = "projapp1"
urlpatterns = [
    path('',views.homeview,name='home'),
    path('aboutview/',views.aboutview,name='aboutview'),
    path('bookingview',views.bookingview,name='bookingview'),
    path('doctorsview',views.doctorsview,name='doctorsview'),
    path('departmentview',views.departmentview,name='departmentview'),
    path('contactview',views.contactview,name='contactview'),
    path('detailsview/<int:myid>/',views.detailsviews,name='detailsview'),
    ]