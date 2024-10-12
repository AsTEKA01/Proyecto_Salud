from django.shortcuts import render

# views.py
def name_sal(request):
    if request.user.is_authenticated:
        context = {'user': request.user}
        return render(request, 'home.html', context)