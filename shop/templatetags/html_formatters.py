from django import template

def currency_us(value):
    return f"${value:,.2f}"

def productimages(value):
    return f"https://raw.githubusercontent.com/ademic2022/productimages/master/images/{value}"

register = template.Library()
register.filter("currency_us", currency_us)
register.simple_tag(productimages)