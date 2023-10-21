from django.shortcuts import render

from projapp1.models import department, Doctortable


def homeview(request):

    return render(request,'home.html')

def aboutview(request):

    return render(request,'about.html')
def bookingview(request):

    return render(request,'booking.html')

def doctorsview(request):
    dict_doct = {'doct': Doctortable.objects.all()}

    return render(request,'doctors.html',dict_doct)

def departmentview(request):
    dict_dept={'dept':department.objects.all()}

    return render(request,'department.html',dict_dept)

def contactview(request):

    return render(request,'contact.html')

def detailsviews(request,myid):
    dict =  Doctortable.objects.filter(id=myid).first()

    return render(request,'details.html',{"dict":dict})