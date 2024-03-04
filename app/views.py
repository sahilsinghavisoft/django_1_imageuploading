from django.shortcuts import render,redirect
from .models import*
#index file view
def indexpage(request):
    return render(request,'app/index.html')
#upload image view
def uploadimage(request):
    if request.method=='POST':
        imagename=request.POST['imgname']
        pics=request.FILES['image']

        newimg=imagedata.objects.create(imagename=imagename,image=pics)
        return redirect('show')
def imagefetch(request):
    all_img=imagedata.objects.all()
    return render(request,'app/show.html',{'key1':all_img})