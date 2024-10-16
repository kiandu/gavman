from django.shortcuts import render

# Create your views here.
def checklist(request):
  return render(request, 'checklist.html')  # Display a success message after form submission