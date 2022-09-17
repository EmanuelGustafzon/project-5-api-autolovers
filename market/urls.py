from django.urls import path
from market import views
 
urlpatterns = [
    path('market/', views.MarketList.as_view()),
    path('market/<int:pk>/', views.MarketDetail.as_view()),
]
