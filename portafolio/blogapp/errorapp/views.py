from django.shortcuts import render

def error_404(request, exception):
    return render(request, 'errorapp/404.html', status=404)
