
from django.contrib import admin
from django.urls import path

from MyApp import views

urlpatterns = [
    path('login/',views.login),
    path('add_category/',views.category),
    path('adminview_category/',views.categoryview),
    path('editcategory/',views.editcategory),
    path('delete_category/',views.deletecategory),
    path('view_complaints/',views.viewcomplaint),
    path('send_reply/',views.sendreply),
    path('change_password/',views.changepassword),
    path('view_registerdUsers/', views.registerduserview),
    path('feedback_view/', views.viewfeedback),

    path('register/',views.registor),
    path('set_reminder/',views.reminderset),
    path('deletesubcategory/',views.deletesubcategory),
    path('view_history/',views.ViewHistory),
    path('user_send_complaints/',views.SendComplaints),
    path('user_view_complaints/', views.viewComplaints),
    path('SendFeedback/', views.SendFeedback),
    path('AddSubCategory/', views.AddSubCategory),
    path('ViewSubCategory/', views.viewSubcategory),
    path('viewSubcategorySel/', views.viewSubcategorySel),
    path('userview_category/',views.categoryview),
    path('Editsub_category/',views.categoryview),
    path('profile/',views.profile),
    path('edit_profile/',views.edit_profile),
    path('viewNotification/',views.viewNotification),
    path('forgot_pass_post/',views.forgot_pass_post),
    path('updaterem/',views.updaterem),
]
