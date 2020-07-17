from django import template
from courses.models import Course
from django.utils.safestring import mark_safe
import markdown2
register = template.Library()


@register.simple_tag

def newest_course():
    '''Gets the most Recent course thst was added to the library.'''
    return Course.objects.latest('pub_date')


@register.filter('markdown_to_html')
def markdown_to_html(markdown_text):
    '''converts markdown text to html'''
    html_body = markdown2.markdown(markdown_text)
    return mark_safe(html_body)

