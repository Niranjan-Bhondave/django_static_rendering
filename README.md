settings.py:
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    os.path.join(BASE_DIR,"static")
]

index.html
{% load static %}
    <link rel="stylesheet" href="{% static 'style.css' %}">
     {% for product in products %}
            <li>{{ product.name }} - ${{ product.price }}</li>
        {% endfor %}
