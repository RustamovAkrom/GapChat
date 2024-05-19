from django.shortcuts import render, redirect


def landing_page(request):
    if request.user.is_authenticated:
        return render(request, "index.html")
    return redirect("users:login")
