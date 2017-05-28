from django.db import models
from django.utils.encoding import python_2_unicode_compatible


class mtbManager(models.Manager):
    def get_queryset(self):
        qs = super(mtbManager, self).get_queryset()
        return qs


@python_2_unicode_compatible
class molecule(models.Model):
    
    
    
    ChemblID = models.CharField(max_length=256) #String ChemBL id
    Smile = models.CharField(max_length=256) # String Field smiles from molecule_structures
    mw_freebase = models.FloatField() # Float Field from molecule properties
    rtb = models.IntegerField() #Integer Field from molecule properties
    Result = models.FloatField() # float Result of applying f(X,Y)
    Drug = models.BooleanField() #True if indication_class field is None or not defined
    TAG = models.CharField(max_length=1) #Char Checking mw_freebase value: A < 300 < B 500 < C
    URL = models.URLField() #String URL from Chembl API
    imageURL = models.URLField() #String URL from Chembl API

    objects = models.Manager()
    molAttriv = mtbManager()
    


    def __str__(self):
        return '%s %s %f %i %f %b %s %s %s ' % (self.ChemblID, self.Smile, self.mw_freebase, self.rtb, self.Result, self.Drug, self.TAG, self.URL, self.imageURL)

    def save(self, *args, **kwargs):
        if not self.ChemblID:
            super(molecule, self).save(*args, **kwargs)