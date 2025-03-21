# Template Guide

This guide explains how to work with templates in the Django project.

## Template Structure

The project uses a single app called `app` with the following template structure:

```
app/
└── templates/
    └── app/              # App-specific templates
        ├── base.html     # Base template
        ├── home.html     # Home page
        └── about.html    # About page
```

## Base Template

The `base.html` template serves as the foundation for all other templates. It contains:

1. Common HTML structure
2. Shared CSS and JavaScript
3. Navigation menu
4. Content blocks

Example `base.html`:
```html
<!DOCTYPE html>
<html>
<head>
    <title>{% block title %}Django Project{% endblock %}</title>
    <style>
        /* Common styles */
    </style>
</head>
<body>
    <nav>
        <a href="{% url 'home' %}">Home</a>
        <a href="{% url 'about' %}">About</a>
    </nav>
    
    <main>
        {% block content %}
        {% endblock %}
    </main>
    
    <footer>
        <p>&copy; 2024 Django Project</p>
    </footer>
</body>
</html>
```

## Extending Templates

All page templates should extend the base template:

```html
{% extends "app/base.html" %}

{% block title %}Page Title{% endblock %}

{% block content %}
<div class="container">
    <h1>Page Content</h1>
    <p>Your content here...</p>
</div>
{% endblock %}
```

## Template Tags

Common Django template tags:

1. **URL Tags**:
```html
<a href="{% url 'home' %}">Home</a>
```

2. **Static Files**:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'css/style.css' %}">
```

3. **Conditionals**:
```html
{% if user.is_authenticated %}
    <p>Welcome, {{ user.username }}!</p>
{% else %}
    <p>Please log in.</p>
{% endif %}
```

4. **Loops**:
```html
{% for item in items %}
    <div class="item">{{ item.name }}</div>
{% endfor %}
```

## Best Practices

1. **Template Organization**:
   - Keep all templates in `app/templates/app/`
   - Use descriptive filenames
   - Group related templates in subdirectories

2. **Template Inheritance**:
   - Always extend the base template
   - Use blocks for content sections
   - Keep common elements in the base template

3. **Template Logic**:
   - Keep logic in views, not templates
   - Use template tags for simple operations
   - Avoid complex calculations in templates

4. **Template Variables**:
   - Use descriptive variable names
   - Pass only necessary data from views
   - Use context processors for global data

## Common Issues

1. **Template Not Found**:
   - Check template path in view
   - Verify template directory structure
   - Ensure app is in INSTALLED_APPS

2. **Template Inheritance Issues**:
   - Verify base template exists
   - Check block names match
   - Ensure proper template loading

3. **Static Files Not Loading**:
   - Check STATIC_URL setting
   - Verify static files directory
   - Run collectstatic if needed

## Testing Templates

1. Start the development server:
```bash
python manage.py runserver
```

2. Visit your pages and check:
   - Template inheritance
   - Static files loading
   - Template tags working
   - Responsive design 