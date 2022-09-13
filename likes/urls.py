from django.urls import path
from likes import views

urlpatterns = [
    path('likes/', views.ReviewLikeList.as_view()), # like a review
    path('likes/<int:pk>/', views.ReviewLikeDetail.as_view()), # Edit, delete review like

]