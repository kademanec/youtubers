from django.shortcuts import render,redirect,get_object_or_404
from youtubers.models import Youtuber
from hiretuber.models import Hiretuber
from django.contrib import messages

# # Create your views here.
# first_name= models.CharField(max_length=255)
#     last_name= models.CharField(max_length=255)
#     tuber_id= models.IntegerField()
#     tuber_name= models.CharField(max_length=255)
#     city= models.CharField(max_length=255)
#     phone= models.CharField(max_length=255)
#     user_id = models.IntegerField(blank=True)
#     state = models.CharField(max_length=255)
#     message = models.TextField(blank=True)
    
def hiretuber(request):
    if request.method =="POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        email=request.POST['email']
        state=request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']

        hiretuber=Hiretuber(first_name=first_name,last_name=last_name,tuber_id=tuber_id,tuber_name=tuber_name, city=city,phone=phone,email=email,state=state,message=message,user_id=user_id)
        hiretuber.save()
        messages.success(request,'Thanks for reaching out!')
        return redirect('youtubers')


def youtubers_detail(request, id):
    print("hellooo")
    tuber = get_object_or_404(Youtuber,pk=id)
    data = {
        'tuber':tuber
    }
    
    return render(request,'youtubers/youtuber_detail.html',data)
      

