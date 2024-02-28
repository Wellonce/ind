from django.shortcuts import render, redirect
from django.views import View
from .models import MalibuModel, GentraModel, CobaltModel, NexiaModel
from .forms import LoginForm, MalibuCreateForm, GentraCreateForm, CobaltCreateForm, NexiaCreateForm, UserCreateForm
from django.contrib import messages
from django.contrib.auth import authenticate, login


# Create your views here.


class HomePageView(View):
    def get(self, request):
        return render (request, 'home.html')
    
class UserRegisterView(View):
    def get(self, request):
        form = UserCreateForm
        return render (request, 'register.html', context = {"form":form})
    
    def post(self, request):
        form = UserCreateForm(data = request.POST)
        if form.is_valid:
            form.save(commit =False)
            messages.success(request, "User successfully registered!")
            return redirect ('login-page')
        else:
            return render (request, 'register.html', context = {"form":form})
    
class LoginView(View):
    def get(self, request):
        form = LoginForm
        return render (request, 'login.html', context = {"form":form})
    
    def post(self, request):
        form = LoginForm(data = request.POST)
        if form.is_valid:
            username = form.cleaned_data("username")
            password = form.cleaned_data("password")
            user = authenticate(request, username, password)
            if user is not None:
                login(request, user)
                messages.success(request, "User succesfully logged in")
                return redirect ("home-page")
            else:
                messages.error (request, "Username or Password is wrong. Please try again")
                return render (request, 'login.html')
        else:
            return render (request, 'login.html', context = {"form":form})

class MalibuView(View):
    def get(self, request):
        return render (request, 'malibu.html')
    
class MalibuCreateView(View):
    def get(self, request):
        malibus = MalibuModel.objects.all()
        form = MalibuCreateForm
        context={
            'malibus':malibus
        }
        return render (request, 'malibu_onsale.html', context=context)
    
    def post(self, request):
        malibus = MalibuModel.objects.all()
        form = MalibuCreateForm(data = request.POST)
        context={
            'malibus':malibus
        }
        if form.is_valid():
            form.save()
            return redirect('myapp: malibu', context=context)
        else:
            messages.error(request, 'Failed to create a new car')
            return render('myapp: malibu_onsale.html', context=context)

    
class GentraView(View):
    def get(self, request):
        return render (request, 'gentra.html')
    

class Gentra_detailview(View):
    def get(self, request):
        gentras = GentraModel.objects.all()
        context = {
            'gentras': gentras
        }
        return render(request, 'gentra_onsale.html', context = context)
    

class CobaltView(View):
    def get(self, request):
        return render (request, 'cobalt.html')
    
class Cobalt_detailview(View):
    def get(self, request):
        cobalts = CobaltModel.objects.all()
        context = {
            'cobalts':cobalts
        }
        return render(request, 'cobalt_onsale.html', context = context)
    

class NexiaView(View):
    def get(self, request):
        return render (request, 'nexia.html')
    

class Nexia_detailview(View):
    def get(self, request):
        nexias = NexiaModel.objects.all()
        context = {
            'nexias': nexias
        }
        return render (request, 'nexia_onsale.html', context=context)