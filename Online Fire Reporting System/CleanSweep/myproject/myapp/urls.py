from django.contrib import admin
from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('signup/', signup_view, name='signup'),
                  path('login/', login_view, name='login'),
                  path('logout/', logout_view, name='logout'),
    path('admin/', admin.site.urls),
path('thankyou/', ThankYouView.as_view(), name='thankyou'),
    path('', index, name='index'),
path('about', about, name='about'),
path('service', service, name='service'),
path('feedback', feedback, name='feedback'),
path('feedbacklist', feedbacklist, name='feedbacklist'),
    path('reporting', reporting, name='reporting'),
    path('viewStatus', viewStatus, name='viewStatus'),
    path('viewStatusDetails/<int:pid>', viewStatusDetails, name='viewStatusDetails'),
    path('admin_login', admin_login, name='admin_login'),
    path('dashboard', dashboard, name='dashboard'),
    path('addTeam', addTeam, name='addTeam'),
    path('manageTeam', manageTeam, name='manageTeam'),
    path('editTeam/<int:pid>', editTeam, name='editTeam'),
    path('deleteTeam/<int:pid>', deleteTeam, name='deleteTeam'),
    path('newRequest', newRequest, name='newRequest'),
    path('assignRequest', assignRequest, name='assignRequest'),
    path('teamontheway', teamontheway, name='teamontheway'),
    path('workinprogress', workinprogress, name='workinprogress'),
    path('completeRequest', completeRequest, name='completeRequest'),
    path('allRequest', allRequest, name='allRequest'),
    path('deleteRequest/<int:pid>', deleteRequest, name='deleteRequest'),
    path('viewRequestDetails/<int:pid>', viewRequestDetails, name='viewRequestDetails'),
    path('dateReport', dateReport, name='dateReport'),
    path('search', search, name='search'),
    path('changePassword', changePassword, name='changePassword'),

    path('logout/', Logout, name='logout'),

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
