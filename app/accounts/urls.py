from django.urls import path
from .views import LoginView, LogoutView, RegisterView, ProfileView, ProfileUpdateView, PasswordChangeView, OrderDetailView


app_name = 'accounts'
urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("profile/", ProfileView.as_view(), name="profile"),
    path('order-detail/<uuid:uuid>/', OrderDetailView.as_view(), name='order_detail'),
    path("profile/edit/", ProfileUpdateView.as_view(), name="profile-edit"),
    path('password-change/', PasswordChangeView.as_view(), name='password_change'),
]
