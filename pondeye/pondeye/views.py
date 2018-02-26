from django.shortcuts import render
from django.views.generic import View
from intro.models import Email
from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import  reverse
from django.http import HttpResponseRedirect
class welcome(View):
	 def get(self,request):
		 return render(request,'advent.html')
	 def post(self,request):
		 email_test= request.POST.get('email')
		 #new_email = Email(email = email_test)
		 new_email, created = Email.objects.get_or_create(email=email_test)
		 if created:
			 messages.info(request,"Already Entered Your Email")
		 else:
			 messages.success(request,"thanks")

		 return  render(request,'advent.html')
