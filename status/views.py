from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.http import Http404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.views.generic import ListView
# Create your views here.
def home(request):
  return render(request,'home.html')

def marriageregister(request):
  if request.method == "POST":
    form = ResgisterForm(request.POST)
    if form.is_valid():
      form.save()
      form = ResgisterForm()
      messages.success(request,"Registration is successfully done!!!")
  else:
    form = ResgisterForm()
  context={'form':form}
  return render(request,'register.html',context)
      
def register(request):
  if request.method == "POST":
    form=UserRegistrationForm(request.POST)
    if form.is_valid():
      form.save()
      username = form.cleaned_data.get('username')
      messages.success(request,f'Account Created for {username}!!')
      form = UserRegistrationForm()
      return redirect('login')
  else: 
    form = UserRegistrationForm()
  context = {
    'form':form
  }
  return render(request,'registers.html',context)


def checkbridesNid(request):
  if request.method == "POST":
    form = BrideNidForm(request.POST)
    if form.is_valid():
      bridesNid = form.cleaned_data["bridesNid"]
      
      try:
        check=MarriageRegister.objects.get(bridesNid=bridesNid)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form =BrideNidForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)


def checkbridesbc(request):
  if request.method == "POST":
    form = BrideBirthCertificateForm(request.POST)
    if form.is_valid():
      bridesBirthCertificate = form.cleaned_data["bridesBirthCertificate"]
      
      try:
        check=MarriageRegister.objects.get(bridesBirthCertificate=bridesBirthCertificate)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form =BrideBirthCertificateForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)


def checkbridespp(request):
  if request.method == "POST":
    form = BridePassportForm(request.POST)
    if form.is_valid():
      bridesPassport = form.cleaned_data["bridesPassport"]
      
      try:
        check=MarriageRegister.objects.get(bridesPassport=bridesPassport)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form =BridePassportForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)


#grooms status check
def checkgroomsNid(request):
  if request.method == "POST":
    form = GroomNidForm(request.POST)
    if form.is_valid():
      groomsNid = form.cleaned_data["groomsNid"]
      
      try:
        check=MarriageRegister.objects.get(groomsNid=groomsNid)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form =GroomNidForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'groomnid.html',context)


def checkgroomsbc(request):
  if request.method == "POST":
    form = GroomBirthCertificateForm(request.POST)
    if form.is_valid():
      groomsBirthCertificate = form.cleaned_data["groomsBirthCertificate"]
      
      try:
        check=MarriageRegister.objects.get(groomsBirthCertificate=groomsBirthCertificate)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form = GroomBirthCertificateForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'groomnid.html',context)



def checkgroomspp(request):
  if request.method == "POST":
    form = GroomPassportForm(request.POST)
    if form.is_valid():
      groomsPassport = form.cleaned_data["groomsPassport"]
      
      try:
        check=MarriageRegister.objects.get(groomsPassport=groomsPassport)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married'})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form = GroomPassportForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'groomnid.html',context)



  
# def success(request):
  # return render(request,'bridenid.html',context={'msg': 'This person is married'})
# 
# def fail(request):
  # return render(request,'bridenid.html',context={'msg':'This person is not married'})

class CustomerListview(ListView):
  model = MarriageRegister
  template_name = 'main.html'

def customer_render_pdf_view(request, *args, **kwargs):
  pk = kwargs.get('pk')
  customer = get_object_or_404(MarriageRegister,pk=pk)
  template_path = 'pdf2.html'
  context = {'customer':customer}
  # Create a Django response object, and specify content_type as pdf
  response = HttpResponse(content_type='application/pdf')
  response['Content-Disposition'] = 'filename="report.pdf"'
  # find the template and render it.
  template = get_template(template_path)
  html = template.render(context)
  # create a pdf
  pisa_status = pisa.CreatePDF(
    html, dest=response)
  # if error then show some funy view
  if pisa_status.err:
    return HttpResponse('We had some errors <pre>' + html + '</pre>')
  return response

def render_pdf_view(request):
    template_path = 'pdf1.html'
    context = {'myvar': 'this is your template context'}
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'filename="report.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)

    # create a pdf
    pisa_status = pisa.CreatePDF(
       html, dest=response)
    # if error then show some funy view
    if pisa_status.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response