# Template Guide

This guide covers template best practices, styling, and common patterns used in the project.

## Basic Template Structure

Every template should follow this basic structure:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Page Title</title>
    <!-- CSS styles -->
</head>
<body>
    <div class="header">
        <h1>Page Title</h1>
        <!-- Navigation -->
    </div>
    <div class="content">
        <!-- Main content -->
    </div>
</body>
</html>
```

## Navigation

Add this navigation section to your template's header:

```html
<div class="nav">
    <a href="{% url 'home' %}">Home</a>
    <a href="{% url 'about' %}">About</a>
    <!-- Add more navigation links -->
</div>
```

## Styling

### Base Styles
Add these styles to your template for consistent design:

```css
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

.button {
    display: inline-block;
    padding: 0.8rem 1.5rem;
    background-color: #3498db;
    color: white;
    text-decoration: none;
    border-radius: 4px;
    margin-top: 1rem;
    transition: background-color 0.3s;
}

.button:hover {
    background-color: #2980b9;
}
```

## Template Best Practices

1. **Consistent Structure**
   - Use the same HTML structure across all pages
   - Keep navigation in the same place
   - Maintain consistent spacing and indentation

2. **Semantic HTML**
   - Use appropriate HTML5 elements
   - Include proper meta tags
   - Use descriptive class names

3. **Responsive Design**
   - Test on different screen sizes
   - Use relative units (rem, em)
   - Include viewport meta tag

4. **Performance**
   - Minimize CSS
   - Optimize images
   - Use efficient selectors

## Common Components

### Header Section
```html
<div class="header">
    <div class="container">
        <h1>Page Title</h1>
        <p>Page description or subtitle</p>
        <div class="nav">
            <!-- Navigation links -->
        </div>
    </div>
</div>
```

### Content Section
```html
<div class="container">
    <div class="content">
        <h2>Section Title</h2>
        <p>Content goes here...</p>
        <a href="#" class="button">Call to Action</a>
    </div>
</div>
```

### Form Styling
```css
.form-group {
    margin-bottom: 1rem;
}

.form-group label {
    display: block;
    margin-bottom: 0.5rem;
}

.form-group input,
.form-group textarea {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ddd;
    border-radius: 4px;
}
``` 