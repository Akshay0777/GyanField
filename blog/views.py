from django.shortcuts import render , HttpResponse , redirect
from .models import Comment,ModernBlogs, News , UserIp
from django.db.models import Q

# Create your views here.
def index(request):
    # return HttpResponse("<h1>Hello Blog Site")
    blg = ModernBlogs.objects.filter(publist_status = "p").order_by('-date')
    news=News.objects.all().order_by('-date')
    pop = ModernBlogs.objects.filter(publist_status = "p").order_by('-views')
    allblg = ModernBlogs.objects.filter(publist_status = "p")
    return render(request , 'index.html',{'blogs':blg[:5] , 'allblog':allblg , 'news' : news , 'pop' : pop[:4]})

def search(request):
    # return HttpResponse("<h1>Hello Blog Site")
    blg = ModernBlogs.objects.filter(publist_status = "p").order_by('-date')
    news=News.objects.all().order_by('-date')
    pop = ModernBlogs.objects.filter(publist_status = "p").order_by('-views')
    allblg = ModernBlogs.objects.filter(publist_status = "p")
    if request.method == "POST":
        query = request.POST.get("query")
        allblg1 = ModernBlogs.objects.filter(publist_status = "p")
        blp = [item for item in allblg1 if query in item.btitle.lower() or query in item.desc.lower()]
        if len(blp) == 0:
            present = False
        else:
            present = True
        return render(request , 'index.html',{'blogs':blg[:5] , 'allblog':allblg , 'pop' : pop[:4] , 'allblog1':blp , 'present':present, 'news' : news})
    return render(request , 'index.html',{'blogs':blg[:5] , 'allblog':allblg , 'pop' : pop[:4], 'news' : news})


def blogpage(request,myid):
    blg = ModernBlogs.objects.filter(id=myid,publist_status = "p").first()
    comment = Comment.objects.filter(post=blg.id).order_by('-date')
    n = len(comment)
    if n > 5:
        a = n-5
    else:
        a = 0
    def get_ip(request):
        adress = request.META.get('HTTP_X_FORWARDED_FOR')
        if adress:
            ip = adress.split(',')[-1].strip()
        else:
            ip = request.META.get('REMOTE_ADDR')
        return ip
    ip = get_ip(request)
    print(ip)
    u = UserIp(blog=blg,user = ip)
    result = UserIp.objects.filter(blog = blg,user = ip)
    if len(result) >= 1:
        pass
    else:
        blg.views= blg.views +1
        blg.save()
        u.save()
        print(u)


    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        cmt = request.POST.get("comment")
        # cm = Comment(name=name,email=email,cmt=cmt,like=0)
        cm = Comment(post=blg,name=name,email=email,cmt=cmt,like=0)
        cm.save()
        if cm is not None:
            return redirect("/blogpage/"+str(myid))
        else:
            return render(request , 'blogpage.html',{'b':blg , 'comment': comment[a:]})
    return render(request , 'blogpage.html',{'b':blg , 'comment': comment[a:]})




# def likeadd(request,myid,cid,no):
#     blg = Blogs.objects.filter(id=myid).first()
#     comment = Comment.objects.get(post=blg.id,id=cid)
#     like1 = comment.like
#     comment.like = like1+1
#     comment.save()
#     return redirect("/blogpage/"+str(myid))


def dashboard(request):
    if request.user.is_authenticated:
        no_blogs=ModernBlogs.objects.all()
        no_view=UserIp.objects.all()
        no_blogs = len(no_blogs)
        viewers = len(no_view)
        news=News.objects.all().order_by('-date')
        cmts = Comment.objects.all().order_by('-date')
        blg = ModernBlogs.objects.all().order_by('-date')
        return render(request,'dashboard.html',{'nblogs':no_blogs, 'viewers':viewers , 'news':news, 'cmts':cmts, 'blogs':blg[:10]})
    else:
        return redirect("login")

def deletecmt(request,cmtid):
    print("deleting cmt",cmtid)
    Comment.objects.filter(id = cmtid).first().delete()
    return redirect("dev")


from django.contrib.auth import authenticate,logout,login
def loginpage(request):
    if request.method == "POST":
        name = request.POST.get("name")
        passw = request.POST.get("pass")
        user = authenticate(username=name, password=passw)
        if user is not None:
            login(request, user)
            return redirect("dev")
        else:
            return redirect("home")   
    return render(request,'login.html')

def logoutpage(request):
    logout(request)
    return redirect("home")   


def addblog(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            title = request.POST.get("title")
            img = request.FILES.get("coverimg")
            email = request.POST.get("email")
            desc = request.POST.get("desc")
            print(title,email,desc,img)
        return render(request,'addblog.html')
    else:
        return redirect("home")

def addnews(request):
    if request.user.is_authenticated:
        return render(request,'addnews.html')
    else:
        return redirect("home")

