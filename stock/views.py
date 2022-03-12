from django.shortcuts import render
from .forms import RegistrationFormDemantForm
# Create your views here.
def home(request):
    template = 'stock/home.html'
    reg = RegistrationFormDemantForm
    if request.method == 'POST':
        form = RegistrationFormDemantForm(request.POST)
        if form.is_valid():

            u = form.save()
            return render(request, 'stock/display.html')

    else:
        reg = RegistrationFormDemantForm
        print(request)
    context = {
        'reg':reg
    }
    return render(request,template,context)

def dashboard(request):
    template = 'stock/dashboard.html'
    context = {}
    return render(request, template, context)