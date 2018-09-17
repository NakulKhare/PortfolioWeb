from django.db import models

# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    image = models.ImageField(upload_to="images/")

    # we make functions to handle verious operations

    # showing the title in admin blog list
    def __str__(self):
        return self.title

    # shortcut of our body
    def getBody(self):
        return self.body[:100]

    # preety datetime
    def pub_date_preety(self):
        return self.pub_date.strftime("%b %e %Y")