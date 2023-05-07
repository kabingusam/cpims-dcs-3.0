from django.shortcuts import render
from cpovc_si.forms import DocumentsManager

# Create your views here.
def test(request):
    return render(request, 'si/si.html')

def admission(request):
    form = DocumentsManager()
    return render(request, 'si/commonforms/admission.html', {'form': form})

