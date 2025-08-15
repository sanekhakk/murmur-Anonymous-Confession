from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),  # make sure this matches your view
    path('recent/', views.recent_confessions, name='recent_confessions'),
    path('post/', views.post_confession, name='post_confession'),
    path('upvote/<int:confession_id>/', views.upvote_confession, name='upvote_confession'),
    path('reply/<int:confession_id>/', views.add_reply, name='add_reply'),  # ✅ new line
    path('contact/', views.contact, name='contact')

]
