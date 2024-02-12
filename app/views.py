from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from app.forms import *
# Create your views here.


#Returning HTTP Response Through Function based views
def fbv_response(request):
    return HttpResponse('<center><h1>FUNCTION BASED VIEWS RESPONSE</h1></center>')

#Returning HTTP Response Through Function based views
class Cbv_response(View):
    def get(self,request):
        return HttpResponse('<center><h1>CLASS BASED VIEWS RESPONSE</h1></center>')
    

#Renderning Html page through FBv
    
def fbvhtml(request):
    return render(request,'fbvhtml.html')


#Renderning Html page through CBV

class cbvhtml(View):
    def get(self,request):
        return render(request,'cbvhtml.html')

#insert data through Functional based view modelform
    
def insert_fbvm(request):
    FBMF=Profileform()
    d={'FBMF':FBMF}
    if request.method=='POST':
        EFBO=Profileform(request.POST)
        if EFBO.is_valid():
            EFBO.save()
            return HttpResponse('data is inserted successfully')
    return render(request,'insert_fbvm.html',d)

#insert data through Class based view modelform

class insert_cbvm(View):
    def get(self,request):
        CBMF=Profileform()
        d={'CBMF':CBMF}
        return render(request,'insert_cbvm.html',d)
    
    def post(self,request):
        CBMFO=Profileform(request.POST)
        if CBMFO.is_valid():
            CBMFO.save()
            return HttpResponse('Inserted cvmf is created')
        else:
            return HttpResponse('not valid')
    
    
    
















    