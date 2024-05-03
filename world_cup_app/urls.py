from django.urls import path
from .views import SignupView, LoginView
from .views import UserDetailsView, NonStaffUserListView, StaffUserListView, UserDeleteView
from .views import NewsCreateView, NewsListView, NewsDeleteView

urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('user-details/', UserDetailsView.as_view(), name='user-details'),
    path('non-staff-users/', NonStaffUserListView.as_view(), name='non-staff-users'),
    path('staff-users/', StaffUserListView.as_view(), name='staff-users'),
    path('delete-user/<int:pk>/', UserDeleteView.as_view(), name='delete-user'),
    path('news/create/', NewsCreateView.as_view(), name='create-news'),
    path('news/', NewsListView.as_view(), name='news-list'),
    path('news/<int:pk>/', NewsDeleteView.as_view(), name='delete-news'),
]