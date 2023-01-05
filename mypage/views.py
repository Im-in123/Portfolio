from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.views.generic import View
from .forms import ContactForm
from django.contrib import messages
from django.conf import settings
from .models import ContactUser, Visitor
from django_user_agents.utils import get_user_agent
# Create your views here.


class Home(View):
    def viser(self, *args, **kwargs):
        visitor = Visitor()
        visitor.visitor += 1

    # Let's assume that the visitor uses an iPhone...

        if self.request.user_agent.is_mobile:  # returns True
            visitor.mobile = True

        if self.request.user_agent.is_tablet:  # returns False
            visitor.tablet = True

        if self.request.user_agent.is_touch_capable:  # returns True
            visitor.touch_capable = True

        if self.request.user_agent.is_pc:  # returns False
            visitor.pc = True

        if self.request.user_agent.is_bot:  # returns False
            visitor.bot = True

        # Accessing user agent's browser attributes
        # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
        if self.request.user_agent.browser:
            visitor.browser = self.request.user_agent.browser

        # Operating System properties
        # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')
        if self.request.user_agent.os:
            visitor.os = self.request.user_agent.os

        # Device properties
        if self.request.user_agent.device:   # returns Device(family='iPhone')
            visitor.device = self.request.user_agent.device

        visitor.save()

    def get(self, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }

        if self.request.COOKIES.get('visit'):
            return render(self.request, "index.html", context)

        else:
            aa = self.viser()
            response = render(self.request, "index.html", context)
            response.set_cookie('visit', 'welcome')
            return response

    def post(self, *args, **kwargs):
        form = ContactForm(self.request.POST)
        print(self.request.POST)

        try:
            if form.is_valid():
                fullname = form.cleaned_data.get('fullname')
                emailinfo = form.cleaned_data.get('email')
                message = form.cleaned_data.get('message')
                subject = form.cleaned_data.get('subject')
            #
                if emailinfo == "" or fullname == "" or message == "":
                    messages.warning(
                        self.request, "Please fill out form!!!")
                    return redirect('home')

                email = settings.EMAIL_HOST_USER
                recipient = [settings.EMAIL_HOST_USER, ]

                rawf = message+" ....:"+"from"+" "+emailinfo+" "+"Fullname:"+fullname

                user = ContactUser()
                user.email = emailinfo
                user.fullname = fullname
                user.message = message
                user.subject = subject

                send_mail(
                    subject,
                    rawf,
                    email,
                    recipient,
                    fail_silently=False,
                )

                user.delivered = "True"
                user.success = "True"
                user.save()
                messages.info(
                    self.request, "Your message has been sent successfully. I will contact you soon!")
                return redirect('home')
            else:
                print(form.errors)
                user.success = "False"
                user.delivered = "False"
                user.save()
                messages.warning(
                    self.request, "The form is invalid, please try again!!!")
                return redirect('home')

        except Exception as e:
            messages.warning(
                self.request, "Error, Check your internet connection or email address!!!")
            return redirect('home')
