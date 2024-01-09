from django.shortcuts import render, redirect
from subscribe.forms import SubscribeForm
from subscribe.models import Subscribe
from django.urls import reverse


# Create your views here.
def subscribe(request):
    subscribe_form = SubscribeForm()
    email_error_empty=''
    print('1')
    if request.POST:
        subscribe_form = SubscribeForm(request.POST)
        if subscribe_form.is_valid():
           #in response to modern form
           subscribe_form.save()
           return redirect(reverse('thank_you'))




            # print('valid form')
            # print(subscribe_form.cleaned_data)
            # email = subscribe_form.cleaned_data['email']
            # # first_name = subscribe_form.clean_first_name
            # first_name = subscribe_form.cleaned_data['first_name']
            # last_name = subscribe_form.cleaned_data['last_name']
            # print(email)
            # subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
            # subscribe.save()
            # return redirect(reverse('thank_you'))
    # if request.POST:
    #     #first_name here is from javascript
    #     first_name = request.POST['firstname']
    #     last_name = request.POST['lastname']
    #     email = request.POST['email']
    #     print("post", email)
    #     if email=="":
    #         email_error_empty="No email entered"
    #     subscribe = Subscribe(first_name=first_name, last_name=last_name, email=email)
    #     subscribe.save()
    context = {"form": subscribe_form, "email_error_empty": email_error_empty}
    return render(request, 'subscribe/subscribe.html', context)
def thank_you(request):
    context={}
    return render(request, 'subscribe/thank_you.html', context)