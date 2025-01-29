from django.shortcuts import render

# Create your views here.
from app.forms import *
from django.http import HttpResponse
def contact(request):
    ECFO=contactform()
    d={'ECFO':ECFO}
    if request.method=='POST':
        FDO=contactform(request.POST)
        if FDO.is_valid():
            return HttpResponse(str(FDO.cleaned_data))
        else:
            return HttpResponse('Invalid data')
    return render(request,'contact.html',d)
