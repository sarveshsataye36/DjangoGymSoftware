from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('index', views.index, name="index"),
    path('about', views.about, name="about"),
    path('classes', views.classes, name="classes"),
    path('contact', views.contact, name="contact"),
    path('services', views.services, name="services"),
    path('team', views.team, name="team"),
    path('faq', views.faq, name="faq"),
    path('privacy', views.privacy, name="privacy"),
    path('membership', views.membership, name="membership"),
    path('loginpopup', views.loginpopup, name="loginpopup"),
    path('registerUser', views.registerUser, name="registerUser"),
    path('loginUser', views.loginUser, name="loginUser"),
    path('logoutUser', views.logoutUser, name="logoutUser"),
    path('customerList', views.customerList, name="customerList"),
    path('visitorList', views.visitorList, name="visitorList"),
    path('UpdateOperation', views.UpdateOperation, name="UpdateOperation"),
    path('Trainees', views.Trainees, name="Trainees"),
    path('curdAdmin', views.curdAdmin, name="curdAdmin"),
    path('curdTrainerInsert', views.curdTrainerInsert, name="curdTrainerInsert"),
    path('adminSetting', views.adminSetting, name="adminSetting"),
    path('curdOperation/<str:person_type>/<int:person_id>', views.curdOperation, name="curdOperation"),
    path('adminUpdatePopup/<int:id>', views.adminUpdatePopup, name="adminUpdatePopup"),
    path('TrainerCurd/<int:id>', views.TrainerCurd, name="TrainerCurd"),
]