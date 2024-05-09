from django.urls import path
from .views import SignupView, LoginView
from .views import UserDetailsView, NonStaffUserListView, StaffUserListView, UserDeleteView
from .views import NewsCreateView, NewsListView, NewsDeleteView
from .views import TeamCreateView, TeamListView, TeamDetailView
from .views import StadiumCreateView, StadiumListView, StadiumDetailView
from .views import MatchCreateView, MatchListView

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
    path('teams/', TeamCreateView.as_view(), name='create-team'),
    path('teams/list/', TeamListView.as_view(), name='team-list'),
    path('teams/<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('stadiums/', StadiumListView.as_view(), name='stadium-list'),
    path('stadiums/add/', StadiumCreateView.as_view(), name='stadium-add'),
    path('stadiums/<int:pk>/', StadiumDetailView.as_view(), name='stadium-detail'),
    path('matches/create/', MatchCreateView.as_view(), name='match-create'),
    path('matches/', MatchListView.as_view(), name='match-list'),
]