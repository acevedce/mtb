from django.db import models
from django.utils.encoding import python_2_unicode_compatible



@python_2_unicode_compatible
class molecule(models.Model):
    
    
    
    ChemblID = models.CharField(max_length=256) #String ChemBL id
    Smile = models.CharField(max_length=256) # String Field smiles from molecule_structures
    mw_freebase = models.FloatField() # Float Field from molecule properties
    rtb = models.IntegerField() #Integer Field from molecule properties
    Result = models.FloatField() # float Result of applying f(X,Y)
    Drug = models.BooleanField('Drug',default=True) #True if indication_class field is None or not defined
    TAG = models.CharField(max_length=1) #Char Checking mw_freebase value: A < 300 < B 500 < C
    URL = models.URLField() #String URL from Chembl API
    imageURL = models.URLField() #String URL from Chembl API

 #   objects = models.Manager()
  #  molAttriv = mtbManager()
    


    def __str__(self):
        return '%s' % (self.ChemblID)

    def publish(self):
        self.save()