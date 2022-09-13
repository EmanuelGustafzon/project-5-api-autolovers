from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.ReviewLikeList.as_view()),
    path('likes/<int:pk>/', views.ReviewLikeDetail.as_view()),
]