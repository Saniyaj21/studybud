from configparser import SafeConfigParser
from django.shortcuts import render, redirect
from .models import Linklist
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from .forms import RegisterUserForm
from django.contrib.auth.forms import UserCreationForm
from django.db.models import Q




# Super user
# username = Sani and passward = saniyaj12345







# Create your views here.
def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == "POST":
        username = request.POST.get('username').lower()
        password = request.POST.get('password').lower()

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User does not exists')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Username or passward does not exxists')

    context = {'page': page}
    return render(request, 'linkapp/login_register.html', context)


def logoutUser(request):
    logout(request)
    return redirect('home')

def registerUser(request):
    page = 'register'
    form = RegisterUserForm()
    


    if request.method == "POST":
        form = RegisterUserForm(request.POST)
    
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()
            login(request, user)
            
            return redirect('home')
            
        
            
        else:
            messages.error(request, 'Something error happend,Try again!')

    return render(request, 'linkapp/login_register.html', {'form': form})

@login_required(login_url='login')
def home(request):

    # search method
    if request.method == "GET":
        q = request.GET.get('q')
        if q!= None and q != "":
            q_list = Linklist.objects.filter(Q(title__contains=q))
            print(q_list)
            
        else:
            q_list = Linklist.objects.filter(Q(title__contains="nothing_to_display_in_search_result"))
    
    # getting all links
    links = Linklist.objects.all()

    context={'links':links, 'q_list':q_list}
    
    return render (request, 'linkapp/home.html', context)


@login_required(login_url='login')
def createlink(request):

    # creating links    
    if request.method == "POST":
        title = request.POST['title']
        link = request.POST['link']
        desc = request.POST['desc']
        host = request.user
        
        if title != "" and link != "":
            valid_link = link.startswith("https://")
            if valid_link == True:
                links = Linklist.objects.create(host=host,title=title,desc=desc,link=link)
            else:
                link = "https://"+link
                links = Linklist.objects.create(host=host,title=title,desc=desc,link=link)
        return redirect('home')
    return render (request, 'linkapp/createlink.html')


@login_required(login_url='login')
def delete(request,id):

    link = Linklist.objects.get(id =id )
    link.delete()
    return redirect('home')

@login_required(login_url='login')
def edit(request,id):
    linklist = Linklist.objects.get(id =id)
    context = {'title':linklist.title, 'link':linklist.link, 'desc':linklist.desc}
    if request.method == "POST":
        linklist.title = request.POST['title']
        linklist.desc = request.POST['desc']
        
        linklist.link = request.POST['link']
        print(linklist.title, linklist.link, linklist.desc)
        linklist.save()
        return redirect('home')

    return render(request,'linkapp/edit_page.html',context)