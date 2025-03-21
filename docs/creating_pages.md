# Creating New Pages

This guide explains how to create new pages in the Django project.

## Overview

The project uses a single app called `app` that contains all the pages. Each page requires:
1. A template file
2. A view function
3. A URL pattern

## Step-by-Step Guide

### 1. Create the Template

Create a new HTML template in `app/templates/app/`:

```html
{% extends "app/base.html" %}

{% block content %}
<div class="container">
    <h1>Your Page Title</h1>
    <p>Your content here...</p>
</div>
{% endblock %}
```

### 2. Add the View

Add a new view function in `app/views.py`:

```python
from django.shortcuts import render

def your_page(request):
    return render(request, 'app/your_page.html')
```

### 3. Add the URL Pattern

Add a new URL pattern in `app/urls.py`:

```python
from django.urls import path
from . import views

urlpatterns = [
    # ... existing patterns ...
    path('your-page/', views.your_page, name='your_page'),
]
```

## Example: Creating an About Page

1. Create `app/templates/app/about.html`:
```html
{% extends "app/base.html" %}

{% block content %}
<div class="container">
    <h1>About Us</h1>
    <p>Learn more about our company...</p>
</div>
{% endblock %}
```

2. Add to `app/views.py`:
```python
def about(request):
    return render(request, 'app/about.html')
```

3. Add to `app/urls.py`:
```python
path('about/', views.about, name='about'),
```

## Best Practices

1. **Template Organization**:
   - Keep all templates in `app/templates/app/`
   - Use descriptive filenames
   - Extend the base template

2. **View Functions**:
   - Use clear, descriptive function names
   - Keep views simple and focused
   - Use appropriate HTTP methods

3. **URL Patterns**:
   - Use descriptive URL patterns
   - Include trailing slashes
   - Use meaningful names for URL patterns

4. **Template Inheritance**:
   - Always extend the base template
   - Use blocks for content sections
   - Keep common elements in the base template

## Common Issues

1. **Template Not Found**:
   - Check template path in view
   - Verify template directory structure
   - Ensure app is in INSTALLED_APPS

2. **URL Not Working**:
   - Check URL pattern syntax
   - Verify view function name
   - Ensure URL pattern is included in main urls.py

3. **Template Inheritance Issues**:
   - Verify base template exists
   - Check block names match
   - Ensure proper template loading

## Testing Your Page

1. Start the development server:
```bash
python manage.py runserver
```

2. Visit your page at:
```
http://127.0.0.1:8000/your-page/
```

3. Check for:
   - Correct URL routing
   - Template rendering
   - Styling and layout
   - Responsive design 