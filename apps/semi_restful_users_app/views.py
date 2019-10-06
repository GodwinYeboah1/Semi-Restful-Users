from django.shortcuts import render, redirect

from  .models import User

# Create your views here.
def index(req):
    allUser = User.objects.all()    
    context = {'users': allUser }
    return render(req, "display_user.html", context)

def new(req):
    return render(req, "add_user.html")

def show(req,id):
    specfic_user = User.objects.get(pk=id)
    context = {'spec_user':specfic_user}
    return render(req, "show_user.html",context)
    
def create(req):
    newUser =  User(
        first_name=req.POST['first_name'],
        last_name=req.POST['last_name'],
        email=req.POST['email']
    )
    newUser.save()
    return redirect('/users')
    
def destory(req,id):
    del_user = User.objects.get(pk=id)
    del_user.delete()
    return redirect('/users/'+id)
    
def edit(req,id):
    spec_user = User.objects.get(pk=id)
    # req.session['spec_user'] = spec_user
    print("Edit obj: ", req.session['user'])
    context= {'user': spec_user }
    return render(req,'edit_user.html',context)

def update(req):
    # should get the id from session 
    update_user = req.session['user']
    update.first_name = req.POST['first_name']
    update.last_name = req.POST['last_name']
    update.email = req.POST['email']
    update_user.save()
    return redirect('/users/'+id)