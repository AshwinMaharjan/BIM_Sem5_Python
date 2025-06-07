<!-- base.html -->
<html>
<body>
  <h1>Welcome</h1>
  {% block content %}{% endblock %}
</body>
</html>

<!-- about.html -->
{% extends "base.html" %}
{% block content %} <p>About Us</p> {% endblock %}
