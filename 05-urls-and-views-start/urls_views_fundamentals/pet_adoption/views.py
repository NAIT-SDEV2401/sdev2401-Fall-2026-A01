from django.shortcuts import render

PET_TYPES = {
    'dog': {
        'name': 'Dog',
        'traits': 'Loyal, energetic, needs space and exercise.',
        'lifestyle_fit': 'active'
    },
    'cat': {
        'name': 'Cat',
        'traits': 'Independent, cuddly, low-maintenance.',
        'lifestyle_fit': 'quiet'
    },
    'rabbit': {
        'name': 'Rabbit',
        'traits': 'Gentle, small, requires calm environment.',
        'lifestyle_fit': 'quiet'
    },
    'parrot': {
        'name': 'Parrot',
        'traits': 'Social, intelligent, needs stimulation.',
        'lifestyle_fit': 'social'
    }
}

def home_page(request):
    return render(request, "pet_adoption/home_page.html", {"pet_types": PET_TYPES})