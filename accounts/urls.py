from django.urls import path
from . import views
from . import api
from django.contrib.auth import views as auth_views
from project import settings


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(next_page=settings.LOGOUT_REDIRECT_URL), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('settings/change_password/', auth_views.PasswordChangeView.as_view(template_name='change_password.html'),
         name='password_change'),
    path('settings/change_password/done', auth_views.PasswordChangeDoneView.as_view(template_name='change_password_done.html'),
         name='password_change_done'),
    path('account/', views.UserUpdateView.as_view(), name='my_account'),


    ## api class based view
    path('api/Customer', api.CustomerApi.as_view(), name='CustomerApi'),
    path('api/Customer/<int:id>', api.CustomerDetailApi.as_view(), name='CustomerDetailApi'),

]



