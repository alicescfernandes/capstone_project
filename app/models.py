from django.db import models
from django.utils import timezone

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['created_date']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def publish(self):
        self.status = 'published'
        self.published_date = timezone.now()
        self.save()

    def archive(self):
        self.status = 'archived'
        self.save()

    @property
    def is_published(self):
        return self.status == 'published'
