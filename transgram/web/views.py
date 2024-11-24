from datetime import datetime

from django.shortcuts import render


def index(request):
    context = {
        'current_year': datetime.now().year
    }

    return render(request, template_name='web/index.html', context=context)
