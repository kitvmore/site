from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.views.generic.base import View
from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
#from django.contrib.auth import login, logout
#from django.contrib import auth
# Create your views here.
class RegisterFormView(FormView):
    form_class = UserCreationForm
    success_url = "/accounts/login/"
    template_name = "register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)
def hello_world(request):
    #username = auth.get_user(request)
    #context = {"username": username}
    return  render(request, 'home.html', {})
