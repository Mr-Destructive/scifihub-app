from django.shortcuts import redirect, render

from .forms import AuthorCreationForm

def register(request):
    if request.method == 'POST':
        form = AuthorCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('login')
        else:
            return render(request, 'accounts/register.html', {'form': form})
    else:
        form = AuthorCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def profile(request):
    return render(request, 'accounts/profile.html')
