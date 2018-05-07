from django.db import models

class Blog(models.Model):
  
  title     = models.CharField(max_length=255)
  pub_date  = models.DateTimeField()
  body      = models.TextField()
  image     = models.ImageField(upload_to='images/')
  
  # this will change the generic title from admin to the actual title
  def __str__(self):
    return self.title
  
  # to limit the chars shown 
  def summary(self):
    return self.body[:100]
  
  # format the date  
  def pub_date_pretty(self):
    return self.pub_date.strftime('%b %e, %Y')