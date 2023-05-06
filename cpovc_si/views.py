from django.shortcuts import render

# Create your views here.
def test(request):
    return render(request, 'si/si.html')

def admission(request):
    return render(request, 'si/commonforms/admission.html')