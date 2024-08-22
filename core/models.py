from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

""" model to tags""" 
class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#000000')
    

    def __str__(self):
        return self.name

""" model to projects""" 
class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = RichTextField()
    tags = models.ManyToManyField(Tag, related_name='projects')
    image = models.ImageField(upload_to='projects/')
    demo = models.URLField(blank=True, max_length=180)
    github = models.URLField(blank=True, max_length=180)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Project'
        verbose_name_plural = 'Projects'
        ordering = ['-created_at']


    def __str__(self):
        return self.title
    
""" model to experience """   
class Experience(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True, default='currenctly')
    description = RichTextField()
    tags = models.ManyToManyField(Tag, related_name='experiences')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Experience'
        verbose_name_plural = 'Experiences'
        ordering = ['-created_at']

    def __str__(self):
        return self.company + ' - ' + self.position
    
class About(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='about/')
    down_resume = models.URLField(blank=True, max_length=180)
    see_resume = models.URLField(blank=True, max_length=180)
    active = models.BooleanField(default=False)  # Nuevo campo para activar el perfil
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'About'
        ordering = ['-created_at']

    def save(self, *args, **kwargs):
        if self.active:
            # Desactivar todos los otros perfiles
            About.objects.filter(active=True).update(active=False)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name