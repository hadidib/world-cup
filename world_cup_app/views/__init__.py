from .signup import SignupView
from .login import LoginView
from .user_details import UserDetailsView
from .users_list import NonStaffUserListView
from .admins_list import StaffUserListView
from .delete_admin import UserDeleteView
from .add_news import NewsCreateView
from .list_news import NewsListView
from .delete_news import NewsDeleteView
from .add_team import TeamCreateView
from .list_teams import TeamListView
from .edit_teams import TeamDetailView
from .add_stadiums import StadiumCreateView
from .list_stadiums import StadiumListView
from .edit_stadiums import StadiumDetailView
from .create_match import MatchCreateView
from .list_matches import MatchListView
from .match_detail import MatchDetailView
from .match_detail import MatchUpdateView
from .match_detail import MatchDeleteView
from .create_reservation import ReservationCreate
from .reserved_seats import ReservedSeatsView
from .reservations import UserReservationsView
from .list_reservations import ReservationListView