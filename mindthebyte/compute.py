#!/usr/bin/env python

from django.conf import settings
import json
import requests

from xml.etree import ElementTree
from .models import molecule
    
    
def compute(mw_freebase,rtb):
    res = mw_freebase/(abs(rtb)+1)
    return res


def get_moleculas(moleculaSearch):
   # headers = {'Accept': 'application/json'}   
    mol = molecule
    url = 'https://www.ebi.ac.uk/chembl/api/data/molecule/'+moleculaSearch
   
    r = requests.get(url)
    
    
    moleculaTrato= ElementTree.fromstring(r.content)
    
    
    mol.ChemblID= moleculaTrato.find('molecule_chembl_id').text
    mol.Smile= moleculaTrato.find('molecule_structures').find('canonical_smiles').text
    mol.mw_freebase=float(moleculaTrato.find('molecule_properties').find('mw_freebase').text)
    mol.rtb=int(moleculaTrato.find('molecule_properties').find('rtb').text)
    mol.Result = compute(mol.mw_freebase,mol.rtb)
    if moleculaTrato.find('indication_class').text == 1:
        mol.Drug = 1
    if moleculaTrato.find('indication_class').text == 0:
        mol.Drug = 0 
    if  float(moleculaTrato.find('molecule_properties').find('mw_freebase').text) < 300:
        mol.TAG='A'
    if  float(moleculaTrato.find('molecule_properties').find('mw_freebase').text) < 500:
        mol.TAG='B'
    if  float(moleculaTrato.find('molecule_properties').find('mw_freebase').text) > 500:
        mol.TAG='C'
    mol.URL = url
    mol.imageURL = url

    
    
    return mol

   