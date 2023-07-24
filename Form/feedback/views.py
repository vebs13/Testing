from django.shortcuts import render
from .models import student
# Create your views here.

def form_view(r):
    stud_list=student.objects.all()
    print(stud_list)
    my_dict={'stud_list':stud_list}
    return render(r,'feedback/feedback.html',context=my_dict)



