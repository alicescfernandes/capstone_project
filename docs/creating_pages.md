# Creating New Pages

This guide will walk you through the process of creating a new page in your Django project using the existing `pages` app.

## Step-by-Step Guide

### 1. Create a View
In `pages/views.py`, add your new view function:
```python
from django.shortcuts import render

def your_page(request):
    return render(request, 'pages/your_page.html')
```

### 2. Create a Template
Create your template file in the existing pages templates directory:
```bash
# The directory structure already exists at pages/templates/pages/
```

Create your template file `pages/templates/pages/your_page.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Your Page Title</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            line-height: 1.6;
            margin: 0;
            padding: 0;
            background-color: #f5f5f5;
        }
        .container {
            max-width: 1200px;
            margin: 0 auto;
            padding: 2rem;
        }
        .header {
            background-color: #2c3e50;
            color: white;
            padding: 2rem 0;
            text-align: center;
        }
        .content {
            background-color: white;
            padding: 2rem;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
            margin-top: 2rem;
        }
        .nav {
            margin-bottom: 1rem;
        }
        .nav a {
            color: white;
            text-decoration: none;
            margin: 0 1rem;
            padding: 0.5rem 1rem;
            border-radius: 4px;
            transition: background-color 0.3s;
        }
        .nav a:hover {
            background-color: #34495e;
        }
    </style>
</head>
<body>
    <div class="header">
        <h1>Your Page Title</h1>
        <div class="nav">
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'about' %}">About</a>
            <!-- Add your new page to navigation -->
        </div>
    </div>
    <div class="content">
        <!-- Your page content -->
    </div>
</body>
</html>
```

### 3. Add URL Pattern
In `pages/urls.py`, add your new URL pattern:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('your-url/', views.your_page, name='your_page'),  # Add this line
]
```

## Best Practices

1. **URL Naming**
   - Use descriptive URL patterns
   - Use hyphens for multi-word URLs
   - Example: `about-us/`, `contact-form/`

2. **Template Organization**
   - Keep all page templates in `pages/templates/pages/`
   - Use consistent naming conventions
   - Example: `home.html`, `about.html`

3. **View Functions**
   - Use descriptive function names
   - Keep views simple and focused
   - Handle errors appropriately

4. **Template Structure**
   - Use consistent HTML structure
   - Include navigation in all pages
   - Maintain consistent styling

## Example: Creating a Contact Page

1. Create the view in `pages/views.py`:
```python
def contact(request):
    return render(request, 'pages/contact.html')
```

2. Create the template at `pages/templates/pages/contact.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>Contact Us</title>
    <style>
        /* Copy the styles from the template above */
    </style>
</head>
<body>
    <div class="header">
        <h1>Contact Us</h1>
        <div class="nav">
            <a href="{% url 'home' %}">Home</a>
            <a href="{% url 'about' %}">About</a>
            <a href="{% url 'contact' %}">Contact</a>
        </div>
    </div>
    <div class="content">
        <h2>Get in Touch</h2>
        <p>Contact us at: example@email.com</p>
    </div>
</body>
</html>
```

3. Add the URL pattern in `pages/urls.py`:
```python
path('contact/', views.contact, name='contact'),
``` 