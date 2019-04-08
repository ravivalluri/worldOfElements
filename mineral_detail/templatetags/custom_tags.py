from django import template

register = template.Library()


@register.simple_tag(name='url_filter_replace')
def url_filter_replace(request, field, value):
    """Always returns to home page and applies necessary filter."""

    url_string = request.GET.copy()

    return u"/?{}={}".format(field, value)
