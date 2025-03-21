# Working with Django Models

This guide explains how to work with Django models, from basic concepts to advanced features.

## Table of Contents
1. [Basic Concepts](#basic-concepts)
2. [Creating Models](#creating-models)
3. [Model Fields](#model-fields)
4. [Model Methods](#model-methods)
5. [Model Relationships](#model-relationships)
6. [Model Meta Options](#model-meta-options)
7. [Working with Models](#working-with-models)
8. [Admin Integration](#admin-integration)
9. [Best Practices](#best-practices)

## Basic Concepts

Models in Django are Python classes that represent database tables. They:
- Define the structure of your data
- Handle data validation
- Provide methods for database operations
- Enable relationships between data

## Creating Models

### Basic Model Structure

```python
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
```

### Model Fields

Common field types:

1. **Text Fields**:
```python
# Short text
title = models.CharField(max_length=200)

# Long text
content = models.TextField()

# Rich text
description = models.TextField(blank=True)
```

2. **Numeric Fields**:
```python
# Integer
age = models.IntegerField()

# Decimal
price = models.DecimalField(max_digits=10, decimal_places=2)

# Float
rating = models.FloatField()
```

3. **Date/Time Fields**:
```python
# Date only
birth_date = models.DateField()

# Date and time
created_at = models.DateTimeField()

# Auto-updating timestamp
updated_at = models.DateTimeField(auto_now=True)

# Date when created
created_date = models.DateTimeField(auto_now_add=True)
```

4. **Boolean Fields**:
```python
is_active = models.BooleanField(default=True)
is_published = models.BooleanField(default=False)
```

5. **Choice Fields**:
```python
STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
    ('archived', 'Archived'),
]

status = models.CharField(max_length=10, choices=STATUS_CHOICES)
```

## Model Methods

### Instance Methods

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    def publish(self):
        """Publish the post."""
        self.status = 'published'
        self.save()

    def get_absolute_url(self):
        """Return the URL for the post."""
        return reverse('post_detail', args=[str(self.id)])

    def __str__(self):
        """String representation of the model."""
        return self.title
```

### Class Methods

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def get_recent_posts(cls, count=5):
        """Get the most recent posts."""
        return cls.objects.order_by('-created_date')[:count]
```

## Model Relationships

### One-to-Many (ForeignKey)

```python
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
```

### Many-to-Many (ManyToManyField)

```python
class Category(models.Model):
    name = models.CharField(max_length=100)
    posts = models.ManyToManyField(Post)
```

### One-to-One (OneToOneField)

```python
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
```

## Model Meta Options

```python
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_date']
        verbose_name = 'Blog Post'
        verbose_name_plural = 'Blog Posts'
        indexes = [
            models.Index(fields=['created_date']),
        ]
```

## Working with Models

### Creating Objects

```python
# Create a single object
post = Post.objects.create(
    title='My First Post',
    content='This is the content'
)

# Create multiple objects
Post.objects.bulk_create([
    Post(title='Post 1', content='Content 1'),
    Post(title='Post 2', content='Content 2'),
])
```

### Querying Objects

```python
# Get all objects
all_posts = Post.objects.all()

# Filter objects
published_posts = Post.objects.filter(status='published')

# Get a single object
post = Post.objects.get(id=1)

# Order objects
recent_posts = Post.objects.order_by('-created_date')

# Limit results
latest_posts = Post.objects.all()[:5]
```

### Updating Objects

```python
# Update a single object
post = Post.objects.get(id=1)
post.title = 'New Title'
post.save()

# Update multiple objects
Post.objects.filter(status='draft').update(status='published')
```

### Deleting Objects

```python
# Delete a single object
post = Post.objects.get(id=1)
post.delete()

# Delete multiple objects
Post.objects.filter(status='draft').delete()
```

## Admin Integration

```python
from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'created_date')
    list_filter = ('status', 'created_date')
    search_fields = ('title', 'content')
    date_hierarchy = 'created_date'
```

## Best Practices

1. **Model Naming**:
   - Use singular, PascalCase names
   - Be descriptive but concise
   - Use nouns (e.g., `Post`, `User`, `Comment`)

2. **Field Naming**:
   - Use lowercase with underscores
   - Be descriptive
   - Use verbs for boolean fields (e.g., `is_active`, `has_published`)

3. **Relationships**:
   - Use appropriate relationship types
   - Consider `on_delete` behavior
   - Use related_name for clarity

4. **Validation**:
   - Use field validators
   - Implement clean methods
   - Add custom validation

5. **Performance**:
   - Use appropriate field types
   - Add indexes for frequently queried fields
   - Use select_related and prefetch_related

6. **Documentation**:
   - Add docstrings to models
   - Document complex methods
   - Include examples in comments

## Example: Complete Model

```python
from django.db import models
from django.utils import timezone
from django.urls import reverse

class Post(models.Model):
    STATUS_CHOICES = [
        ('draft', 'Draft'),
        ('published', 'Published'),
        ('archived', 'Archived'),
    ]

    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    categories = models.ManyToManyField('Category')
    featured_image = models.ImageField(upload_to='blog/', blank=True)

    class Meta:
        ordering = ['-created_date']
        indexes = [
            models.Index(fields=['created_date']),
            models.Index(fields=['status']),
        ]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

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

    @classmethod
    def get_recent_posts(cls, count=5):
        return cls.objects.filter(status='published').order_by('-created_date')[:count]
``` 