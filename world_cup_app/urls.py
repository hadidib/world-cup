from django.urls import path
from .views import SignupView, LoginView
from .views import UserDetailsView, NonStaffUserListView, StaffUserListView, UserDeleteView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-details/', UserDetailsView.as_view(), name='user-details'),
    path('non-staff-users/', NonStaffUserListView.as_view(), name='non-staff-users'),
    path('staff-users/', StaffUserListView.as_view(), name='staff-users'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
]