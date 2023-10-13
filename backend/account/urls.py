from django.urls import path
from .views import RegisterView, LoginView, LogoutView, PasswordChangeView,ClientProfileView, UserUpdateView,RoleListView

urlpatterns = [
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('api/user/<int:pk>/update/',
         UserUpdateView.as_view(), name='client-update'),
    path('password/change/', PasswordChangeView.as_view(), name='password-change'),
    path('api/profile/', ClientProfileView.as_view(), name='client-profile'),
    path('role/', RoleListView.as_view(), name='role'),

]
