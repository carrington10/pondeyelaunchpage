from django.shortcuts import render
from django.http import HttpResponse
from .models import Email


# Create your views here.

def email_list(response):
    emails = Email.objects.all()
    return render(response,'intro/test.html')
