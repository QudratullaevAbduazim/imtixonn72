from django.urls import path
from .views import HomeView, PhoneDetailView, PhoneCreateView, PhoneUpdateView, PhoneDeleteView, CategoryDetailView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('category/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('phone/<int:pk>/', PhoneDetailView.as_view(), name='phone_detail'),
    path('phone/create/', PhoneCreateView.as_view(), name='phone_create'),
    path('phone/<int:pk>/update/', PhoneUpdateView.as_view(), name='phone_update'),
    path('phone/<int:pk>/delete/', PhoneDeleteView.as_view(), name='phone_delete'),
]
