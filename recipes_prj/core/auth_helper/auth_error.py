from django.shortcuts import render


def error_403(request):
    return render(request, 'error_403.html', status=403)
