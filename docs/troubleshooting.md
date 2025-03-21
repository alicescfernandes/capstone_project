# Troubleshooting Guide

This guide covers common issues and their solutions in the Django project.

## Common Issues

### 1. Django Not Found
**Error**: `ModuleNotFoundError: No module named 'django'`

**Solution**:
1. Activate your virtual environment:
```bash
source venv/Scripts/activate  # On Windows with Git Bash
```

2. Install Django:
```bash
pip install django
```

### 2. Migration Issues
**Error**: `No migrations to apply` or `Migration conflicts`

**Solution**:
1. Create new migrations:
```bash
python manage.py makemigrations
```

2. Apply migrations:
```bash
python manage.py migrate
```

3. If conflicts persist:
   - Delete the migrations folder
   - Delete the database
   - Run `makemigrations` and `migrate` again

### 3. Template Not Found
**Error**: `TemplateDoesNotExist`

**Solution**:
1. Check `INSTALLED_APPS` in `settings.py`:
```python
INSTALLED_APPS = [
    ...
    'your_app_name',
]
```

2. Verify template directory structure:
```
your_app/
└── templates/
    └── your_app/
        └── your_template.html
```

3. Check template name in view:
```python
def your_view(request):
    return render(request, 'your_app/your_template.html')
```

### 4. URL Pattern Issues
**Error**: `NoReverseMatch` or `URL pattern not found`

**Solution**:
1. Check URL pattern names:
```python
path('your-url/', views.your_view, name='your_url_name'),
```

2. Verify URL template tags:
```html
<a href="{% url 'your_url_name' %}">Link</a>
```

3. Check URL includes:
```python
urlpatterns = [
    path('', include('your_app.urls')),
]
```

### 5. Static Files Not Loading
**Error**: Static files not appearing or 404 errors

**Solution**:
1. Add to `settings.py`:
```python
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
```

2. Create static directory:
```bash
mkdir static
```

3. Run collectstatic:
```bash
python manage.py collectstatic
```

### 6. Database Connection Issues
**Error**: `Database connection failed`

**Solution**:
1. Check database settings in `settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

2. Verify database exists and is accessible
3. Check database permissions

### 7. Development Server Issues
**Error**: `Port already in use`

**Solution**:
1. Use a different port:
```bash
python manage.py runserver 8080
```

2. Or find and kill the process using the port:
```bash
# On Windows
netstat -ano | findstr :8000
taskkill /PID <PID> /F
```

## General Tips

1. **Check Logs**
   - Look at the development server output
   - Check Django debug page
   - Review application logs

2. **Verify Environment**
   - Ensure virtual environment is activated
   - Check Python version
   - Verify installed packages

3. **Common Fixes**
   - Clear browser cache
   - Restart development server
   - Check file permissions

4. **Debug Mode**
   - Ensure `DEBUG = True` in development
   - Use Django debug toolbar
   - Check error messages carefully

## Getting Help

If you're still experiencing issues:
1. Check the [Django documentation](https://docs.djangoproject.com/)
2. Search for similar issues on Stack Overflow
3. Ask for help in the Django community 