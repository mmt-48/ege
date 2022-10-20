from django.db import models

class Topic(models.Model):
    name_topic = models.CharField(max_length=200, db_index=True)
    number_in_order = models.IntegerField(default=0)
    mett = models.IntegerField(default=0)
    tip_top = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return self.name_topic

class Probl(models.Model):
    condition_txt = models.TextField(blank=True, null=True, default='')
    solution_txt = models.TextField(blank=True, null=True, default='')
    hint_txt = models.CharField(max_length=1000, blank=True, null=True, default='')
    complexity = models.IntegerField(blank=True, null=True, default=0)
    topic = models.ForeignKey('topic', on_delete=models.PROTECT, default='')
    result = models.CharField(max_length=200, blank=True, null=True, default='')
    result_full = models.CharField(max_length=200, blank=True, null=True, default='')
    ege = models.IntegerField(blank=True, null=True, default=0)
    place_ege = models.CharField(max_length=100, blank=True, null=True, default='')
    tip_ege = models.IntegerField(blank=True, null=True, default=0)
    gkey = models.CharField(max_length=20, blank=True, null=True, default='')
    number_task = models.IntegerField(blank=True, null=True, default=0)
    variant = models.IntegerField(blank=True, null=True, default=0)
    source = models.CharField(max_length=100, blank=True, null=True, default='')
    name_potok = models.CharField(max_length=50, blank=True, null=True, default='')
    date = models.DateTimeField(blank=True, null=True)
    school_class = models.IntegerField(blank=True, null=True, default=0)
    nopor = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(self.pk)+'_'+self.gkey.strip()+'_'+str(self.number_task)+'klass '+str(self.school_class)+'comp'+str(self.complexity )

    class Meta:
        verbose_name = 'probl'
        verbose_name_plural = 'probls'

class Exam(models.Model):
    date = models.DateTimeField(blank=True, null=True)
    tip_ege = models.IntegerField(blank=True, null=True, default=0)
    year = models.IntegerField(blank=True, null=True, default=0)

    def __str__(self):
        return str(10*self.year+self.tip_ege)

class Bimg(models.Model):
    name = models.CharField(max_length=200, db_index=True)
    img1 = models.ImageField(upload_to='condition', default='', blank=True, null=True)
    img2 = models.ImageField(upload_to='condition', default='', blank=True, null=True)

    def __str__(self):
        return self.name

    # def get_absolute_url(self):
    #    return reverse('index', kwargs={'probl_id': self.pk})







