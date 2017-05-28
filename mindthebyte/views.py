from django.shortcuts import render

def molecule_list(request):
    return render(request, 'mindthebyte/molecule_list.html', {})