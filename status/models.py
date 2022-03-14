from django.db import models
from django.contrib.auth.models import User



# Create your models here.
class MarriageRegister(models.Model):
  serialNo=models.CharField(max_length=10,null=True,blank=True)
  brideName=models.CharField(max_length=50,blank=True,null=True)
  bridesNid=models.CharField(max_length=100,null=True,blank=True)
  bridesBirthCertificate=models.CharField(max_length=100,null=True,blank=True)
  bridemobile=models.CharField(max_length=20,blank=True,null=True)
  bridesPassport=models.CharField(max_length=100,null=True,blank=True)
  bridesFathersname=models.CharField(max_length=50,null=True,blank=True)
  bridesFathersNid=models.CharField(max_length=50,null=True,blank=True)
  bridesMothersname= models.CharField(max_length=50,null=True,blank=True)
  bridesMothersNid = models.CharField(max_length=50,null=True,blank=True)
  bridesOccupation = models.CharField(max_length=50,null=True,blank=True)
  bridesWorkplace = models.CharField(max_length=50,null=True,blank=True)
  brideImages = models.ImageField(upload_to='images/',null=True,blank=True)
  brideSignature = models.ImageField(upload_to='images/',null=True,blank=True)
  groomsName=models.CharField(max_length=50,blank=True,null=True)
  groomsNid=models.CharField(max_length=100,null=True,blank=True)
  groomsBirthCertificate=models.CharField(max_length=100,null=True,blank=True)
  groomsPassport=models.CharField(max_length=100,null=True,blank=True)
  groommobile=models.CharField(max_length=20,blank=True,null=True)
  groomsFathersname=models.CharField(max_length=50,null=True,blank=True)
  groomsFathersNid=models.CharField(max_length=50,null=True,blank=True)
  groomsMothersname= models.CharField(max_length=50,null=True,blank=True)
  groomsMothersNid = models.CharField(max_length=50,null=True,blank=True)
  groomsOccupation = models.CharField(max_length=50,null=True,blank=True)
  groomsWorkplace = models.CharField(max_length=50,null=True,blank=True)
  groomImages = models.ImageField(upload_to='images/',null=True,blank=True)
  groomSignature = models.ImageField(upload_to='images/',null=True,blank=True)
  firstAttestor=models.CharField(max_length=50,null=True,blank=True)
  firstAttestorNid=models.CharField(max_length=50,null=True,blank=True)
  secondAttestor=models.CharField(max_length=50,null=True,blank=True)
  secondAttestorNid=models.CharField(max_length=50,null=True,blank=True)
  thirdAttestor=models.CharField(max_length=50,null=True,blank=True)
  thirdAttestorNid=models.CharField(max_length=50,null=True,blank=True)
  marrige_place = models.CharField(max_length=50,null=True,blank=True)
  marriage_date= models.DateTimeField()


  def __str__(self):
    return str(self.id)
  
  


# class Customuser(models.Model):
  # user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)