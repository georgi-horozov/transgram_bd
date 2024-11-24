from django.urls import path

from transgram.accounts.views import (LoginUserView, RegisterUserView,
                                      logout_user,
                                      ProfileDetailsView,
                                      ProfileUpdateView,
                                      ProfileDeleteView)

urlpatterns = (
    path('login/', LoginUserView.as_view(), name='login_user'),
    path('register/', RegisterUserView.as_view(), name='register_user'),
    path('logout/', logout_user, name='logout_user'),
    path('profile/<int:pk>/', ProfileDetailsView.as_view(), name='profile_details'),
    path('profile/<int:pk>/update/', ProfileUpdateView.as_view(), name='profile_update'),
    path('profile/<int:pk>/delete/', ProfileDeleteView.as_view(), name='profile_delete')
)