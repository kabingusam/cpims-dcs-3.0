from django.shortcuts import render
from cpovc_si.forms import DocumentsManager, AFCForm1A
from django.contrib import messages
from django.shortcuts import render, redirect

# Create your views here.
def test(request):
    return render(request, 'si/si.html')

def admission(request):
    form = DocumentsManager()
    return render(request, 'si/commonforms/admission.html', {'form': form})

def biodata(request):
    if request.method == 'POST':
        form = AFCForm1A(request.POST)
        if form.is_valid():
            # Save the form data
            form.save()
            # Set success message
            messages.success(request, 'Form submitted successfully')
            # Redirect to success page
            return redirect('success_page')
    else:
        form = AFCForm1A()
    return render(request, 'si/commonforms/biodata.html', {'form': form})