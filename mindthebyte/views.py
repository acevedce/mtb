from django.shortcuts import render
from .models import molecule

def molecule_list(request):
    molecules = molecule.objects.all()
    return render(request, 'mindthebyte/molecule_list.html', {'molecules':molecules})