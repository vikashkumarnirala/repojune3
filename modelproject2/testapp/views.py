from django.shortcuts import render
from testapp.models import employee
# Create your views here.
def empdata_view(request):
    emp_list=employee.objects.all()
    my_dict={'emp_list':emp_list}
    return render(request,'testapp/emp.html',my_dict)