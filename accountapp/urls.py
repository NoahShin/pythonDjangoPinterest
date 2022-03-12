from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

<<<<<<< HEAD
<<<<<<< HEAD
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
=======
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> 9974e96 (updateView)
=======
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> ab30486 (delete View and bug fix)

app_name = 'accountapp'

urlpatterns = [
    path('hello_world/', hello_world, name='hello_world'),
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
<<<<<<< HEAD
<<<<<<< HEAD
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
=======
>>>>>>> 9974e96 (updateView)
=======
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
>>>>>>> ab30486 (delete View and bug fix)
]