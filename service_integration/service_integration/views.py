from django.shortcuts import render

def index(request):
    return render(request,'global/index.html',{'title':'Hacklahoma 2021','index':'active'})
