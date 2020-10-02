from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic

from .forms import ContactForm

def contactView(request):
    if request.method == 'GET':
        form = ContactForm()
    else:
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            message = 'Nombre: ' + name + '\nEmail: ' + email + '\nMensaje: \n\n' + message
            try:
                send_mail('Contacto: ' + subject, message,
                          'revistasomos@glm.edu.co', ['revistasomoss@gmail.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('contact:success')
    return render(request, "contact/contact.html", {'form': form})

class SuccessView(generic.TemplateView):
    template_name = "contact/success.html"
