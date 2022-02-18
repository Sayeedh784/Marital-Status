from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect,get_object_or_404
from .models import *
from .forms import *
from django.contrib import messages
from django.http import Http404
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.template.loader import get_template
from django.views.generic import ListView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
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

@login_required
def checkbridesNid(request):
  if request.method == "POST":
    form = BrideNidForm(request.POST)
    if form.is_valid():
      bridesNid = form.cleaned_data["bridesNid"]
      bridemobile=form.cleaned_data["bridemobile"]
      
      try:
        check=MarriageRegister.objects.get(bridesNid=bridesNid,bridemobile=bridemobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married','check':check})
        
  else:
    form =BrideNidForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)

@login_required
def checkbridesbc(request):
  if request.method == "POST":
    form = BrideBirthCertificateForm(request.POST)
    if form.is_valid():
      bridesBirthCertificate = form.cleaned_data["bridesBirthCertificate"]
      bridemobile = form.cleaned_data["bridemobile"]
      
      try:
        check=MarriageRegister.objects.get(bridesBirthCertificate=bridesBirthCertificate,bridemobile=bridemobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married'})
        
  else:
    form =BrideBirthCertificateForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)

@login_required
def checkbridespp(request):
  if request.method == "POST":
    form = BridePassportForm(request.POST)
    if form.is_valid():
      bridesPassport = form.cleaned_data["bridesPassport"]
      bridemobile = form.cleaned_data["bridemobile"]
      
      try:
        check=MarriageRegister.objects.get(bridesPassport=bridesPassport,bridemobile=bridemobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married','check':check})
        
  else:
    form =BridePassportForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'bridenid.html',context)

@login_required
#grooms status check
def checkgroomsNid(request):
  if request.method == "POST":
    form = GroomNidForm(request.POST)
    if form.is_valid():
      groomsNid = form.cleaned_data["groomsNid"]
      groommobile = form.cleaned_data["groommobile"]
      
      try:
        check=MarriageRegister.objects.get(groomsNid=groomsNid,groommobile=groommobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married','check':check})
        
  else:
    form =GroomNidForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'groomnid.html',context)

@login_required
def checkgroomsbc(request):
  if request.method == "POST":
    form = GroomBirthCertificateForm(request.POST)
    if form.is_valid():
      groomsBirthCertificate = form.cleaned_data["groomsBirthCertificate"]
      groommobile = form.cleaned_data["groommobile"]
      
      try:
        check=MarriageRegister.objects.get(groomsBirthCertificate=groomsBirthCertificate,groommobile=groommobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married','check':check})
        
  else:
    form = GroomBirthCertificateForm()
    # if 'submitted' in request.GET:
      # submitted = True
    context={'form':form}
  return render(request,'groomnid.html',context)


@login_required
def checkgroomspp(request):
  if request.method == "POST":
    form = GroomPassportForm(request.POST)
    if form.is_valid():
      groomsPassport = form.cleaned_data["groomsPassport"]
      groommobile = form.cleaned_data["groommobile"]
      
      try:
        check=MarriageRegister.objects.get(groomsPassport=groomsPassport,groommobile=groommobile)
        

        #return HttpResponseRedirect('/bridenid/success')
      except:
        check = None
      if check is not None:
        # return HttpResponseRedirect('/bridenid/success')
        return render(request,'bridenidshow.html',context={'msg':'This person is married','check':check})
        
      else:
        # return HttpResponseRedirect('/bridenid/fail')
        return render(request,'bridenidshow.html',context={'msg': 'This person is not married','check':check})
        
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

# class CustomerListview(LoginRequiredMixin,ListView):
#   model = MarriageRegister
#   template_name = 'bridenidshow.html'

@login_required
def customer_render_pdf_view(request, *args, **kwargs):
  pk = kwargs.get('pk')
  customer = get_object_or_404(MarriageRegister,pk=pk)
  template_path = 'pdf1.html'
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



