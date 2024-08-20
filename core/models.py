from django.db import models

# Create your models here.

class Tag(models.Model):
    name = models.CharField(max_length=50, unique=True)
    color = models.CharField(max_length=7, default='#000000')
    

    def __str__(self):
        return self.name

class Projects(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
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
    