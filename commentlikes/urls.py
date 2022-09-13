from django.urls import path
from commentlikes import views

urlpatterns = [
    path('commentlikes/', views.CommentLikeList.as_view()),
    path('commentlikes/<int:pk>/', views.CommentLikeDetail.as_view()),

]