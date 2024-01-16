from django.shortcuts import render , redirect
from .models import Room,Message
from django.http import HttpResponse , JsonResponse ,HttpResponseRedirect
from django.contrib.auth.models import User,auth
from django.contrib import messages


# Create your views here.
def index(request):
    usernames = request.GET.get('usernames', None)
    return render(request, "index.html", {"usernames": usernames})

def room(request,room):
    User = request.GET.get('username') # This is coming from the url which has the name username
    Room_name = Room.objects.get(name= room)
    return render(request, "room.html", {"User": User,"room": room,"Room_name": Room_name})

def VerifyData(request):
    Room_name = request.POST['Room']
    User = request.POST['User']

    if Room.objects.filter(name = Room_name).exists(): # name is coming from Room model and rooom is the variable defined above
        return redirect("/"+Room_name+"/?username="+User)
    else:
        new_room = Room.objects.create(name = Room_name)
        new_room.save()
        return redirect("/" + Room_name + "/?username=" + User)

def storage(request):
    message = request.POST['message']
    Room_name = request.POST['Room_name']
    User = request.POST['User']
    new_message = Message.objects.create(value=message, user = User, room= Room_name)
    new_message.save()
    return HttpResponse("Message Sent Successfully")

def getMessages(request,room):
    room_details = Room.objects.get(name= room)
    messages = Message.objects.filter(room = room_details)
    return JsonResponse({"messages":list(messages.values())})

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        verify_password = request.POST["password2"]
        if password == verify_password:
            if User.objects.filter(email = email, username = username).exists():
                messages.info(request,"Username already exists")
                messages.info(request, "Email already exists")
                return redirect("register")
            elif User.objects.filter(email= email)  .exists():
                messages.info(request,"Email already exists")
                return redirect("register")
            elif User.objects.filter(username = username).exists():
                messages.info(request,"Username already exists")
                return redirect("register")

            else:
                user = User.objects.create_user(username = username, email= email, password=password)
                user.save();
                return redirect("login")
        else:
            messages.info(request, " Password does not match")
            return redirect("register")
    else:
        return render(request, "register.html")

def login(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = auth.authenticate(username = username, password=password)
        if user is not None:
            auth.login(request,user)
            return HttpResponseRedirect(f"/?usernames={username}")
        else:
            messages.info(request, " Not Registered!")
            return redirect("login")
    else:
        return render(request, "login.html")

def logout(request):
    auth.logout(request)

    return redirect("/")

def newlogout(request,variable):
    auth.logout(request)

    return redirect("/")