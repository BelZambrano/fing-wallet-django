from django import template

register = template.Library()


@register.filter
def clp(valor):
    try:
        return "{:,.0f}".format(valor).replace(",", ".")
    except:
        return valor
