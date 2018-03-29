from django.db import models
from django.db.models import permalink
from image_cropping import ImageCropField, ImageRatioField


authors = (('ADAM WALLCE', 'Adam Wallace'), ('MORGAN HUNTER', 'Morgan Hunter'))

class Guide(models.Model):
    title = models.CharField(max_length=100, unique=True)
    author = models.CharField(max_length=20, unique=True, choices=authors)
    slug = models.SlugField(max_length=20, unique=True)
    header = models.CharField(max_length=100)
    short_description = models.TextField(max_length=150, unique=True)
    body = models.TextField()
    body_2 = models.TextField()
    website = models.URLField(blank=True)
    cost = models.CharField(max_length=30)
    address = models.CharField(max_length=100)
    favorite_quote = models.CharField(max_length=100)
    posted = models.DateTimeField(db_index=True, auto_now_add=True)
    image = models.ImageField(upload_to='Guide_image')
    cropping = ImageRatioField('image', '960 x 540')


    def __unicode__(self):
        return '%s' % self.title

    def __str__(self):
        return str(self.posted.date()) + ':   ' + self.title + ' '

    @permalink
    def get_absolute_url(self):
        return ('view_blog_post', None, {'slug': self.slug})

    def remove(self):
        return '<input type="button" value="Delete" onclick="location.href=\'%s/delete/\'" />' \
               % (self.pk)