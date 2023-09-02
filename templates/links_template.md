{# templates/links_template.md #}

### Links to useful services

| Type| Company|Why|Link|Message|
|----------|-------------|------|---|---|
{% for link in links -%}
| {{ link.type }} | [{{ link.service_name }}]({{ link.service_url }}) | {{ link.motiv }} | [{{ link.url }}]({{ link.url }}) | {{ link.explanation }} | 
{% endfor %}
