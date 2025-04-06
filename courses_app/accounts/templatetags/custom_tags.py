from django import template


register = template.Library()

@register.simple_tag
def capitalize_(text):
    text = text.strip().capitalize()
    return text

@register.simple_tag
def cut_text(text, max_length):
    max_length = int(max_length)
    if len(text) > max_length:
        return text[:max_length]

@register.inclusion_tag('partials/zodiac_list.html')
def zodiac_signs():
    signs = [
        "Aries", "Taurus", "Gemini", "Cancer",
        "Leo", "Virgo", "Libra", "Scorpio",
        "Sagittarius", "Capricorn", "Aquarius", "Pisces"
    ]
    return {'signs': signs}