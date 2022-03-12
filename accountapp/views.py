from django.http import HttpResponse, HttpResponseForbidden, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from accountapp.forms import AccountUpdateForm
from accountapp.models import HelloWorld
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def hello_world(request):
  if request.user.is_authenticated:
    if request.method == 'POST':

      temp = request.POST.get('hello_world_input')

      new_hello_world = HelloWorld()
      new_hello_world.text = temp
      new_hello_world.save()

      return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
      hello_world_list = HelloWorld.objects.all()
      return render(request, 'accountapp/helloworld.html', context={'hello_world_list': hello_world_list})
  else:
    return HttpResponseRedirect(reverse('accountapp:login'))

class AccountCreateView(CreateView):
  model = User
  form_class = UserCreationForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
  model = User
  context_object_name = 'target_user'
  template_name = 'accountapp/detail.html'

class AccountUpdateView(UpdateView):
  model = User
  context_object_name = 'target_user'
  form_class = AccountUpdateForm
  success_url = reverse_lazy('accountapp:hello_world')
  template_name = 'accountapp/update.html'

<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 075e965 (authentication)
  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()

  def post(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()
<<<<<<< HEAD
=======
>>>>>>> 2765aab (delete View and bug fix)
=======
>>>>>>> 075e965 (authentication)
class AccountDeleteView(DeleteView):
  model = User
  context_object_name = 'target_user'
  success_url = reverse_lazy('accountapp:login')
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> 075e965 (authentication)
  template_name = 'accountapp/delete.html'

  def get(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
      return HttpResponseForbidden()

  def post(self, *args, **kwargs):
    if self.request.user.is_authenticated and self.get_object() == self.request.user:
      return super().get(*args, **kwargs)
    else:
<<<<<<< HEAD
      return HttpResponseForbidden()
=======
  template_name = 'accountapp/delete.html'
>>>>>>> 2765aab (delete View and bug fix)
=======
      return HttpResponseForbidden()
>>>>>>> 075e965 (authentication)
