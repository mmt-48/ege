from django.test import TestCase

# Create your tests here.
class bimg(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    img1 = models.ImageField(upload_to='condition', default='', blank=True, null=True)
    img2 = models.ImageField(upload_to='condition', default='', blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #    return reverse('index', kwargs={'probl_id': self.pk})
