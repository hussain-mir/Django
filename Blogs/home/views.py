from django.shortcuts import render, HttpResponse 
from home.models import Blog, Contect

# Create your views here.
def index(request):
    return render(request, "index.html")
def blog(request):
    blogs=Blog.objects.all()
    contex={"blogs":blogs}
    return render(request, "blog.html",contex)
    
def content(request):
    if request.method=="POST":
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        passwd=request.POST.get("passwd")
        desc=request.POST.get("desc")
        ins=Contect(name=name, phone=phone, email=email, passwd=passwd, desc=desc)
        ins.save()
        
    return render(request, "content.html")
def search(request):
    ast=0
    return render(request, "search.html")
    
def blogpost(request,slug):
    
    blog=Blog.objects.filter(slug=slug).first()
    contex={"blog":blog}
    print(blog.title)
    print(blog.content)
    return render(request, "blogpost.html", contex)