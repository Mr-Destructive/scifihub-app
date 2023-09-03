

def list_projects(request):
    authot = request.user
    projects = Project.objects.filter(author=authot)
    return render(request, 'projects/list_projects.html', {'projects': projects})
