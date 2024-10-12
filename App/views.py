from django.shortcuts import render



def home(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def resume(request):
    return render(request, 'resume.html')
def about(request):
    return render(request, 'about.html')
def portfolio_details(request):
    return render(request, 'portfolio-details.html')
def portfolio(request):
    return render(request, 'portfolio.html')
def service_details(request):
    return render(request, 'service-details.html')
def starter_page(request):
    return render(request, 'starter-page.html')
def services(request):
    return render(request, 'services.html')
# Create your views here.
