from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
=======
from accountapp.views import AccountCreateView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> 9974e96 (updateView)
=======
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> ab30486 (delete View and bug fix)
=======
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> 2765aab (delete View and bug fix)
=======
from accountapp.views import AccountCreateView, AccountDeleteView, AccountDetailView, AccountUpdateView, hello_world
>>>>>>> 43b223aeda573772788f425f29f2ef48aad8db19

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
<<<<<<< HEAD
<<<<<<< HEAD
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
=======
>>>>>>> 9974e96 (updateView)
=======
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
>>>>>>> ab30486 (delete View and bug fix)
=======
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
>>>>>>> 2765aab (delete View and bug fix)
=======
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
>>>>>>> 43b223aeda573772788f425f29f2ef48aad8db19
]