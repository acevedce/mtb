from django.shortcuts import render,redirect
from django.conf import settings
import json
import requests
from xml.etree import ElementTree
from .models import molecule
from .forms import PostForm
import compute



def molecule_list(request):
    molecules = molecule.objects.all()
    return render(request, 'mindthebyte/molecule_list.html', {'molecules':molecules})

def molecule_create(request):
    if request.method == 'POST':
        
        idmol=request.POST.get('ChemblID')
        
        molc=compute.get_moleculas(idmol)

        form = PostForm(data=request.POST)
        if form.is_valid():

            molecule = form.save(commit=False)
            molecule.save()
            form.save_m2m()
            return redirect('molecula_list',
                ChemblID=molecule.ChemblID)
    else:
        form = PostForm()
    context = {'form': form, 'create': True}
    return render(request, 'mindthebyte/form.html', context)