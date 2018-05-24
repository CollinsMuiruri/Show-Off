from django.shortcuts import render, redirect
import datetime as dt
from .models import Image
from django.http import Http404


# Create your views here.

def welcome(request):
    image = Image.objects.all()
    return render(request, 'showme/welcome.html', {"image": image})


def liveshowoffs(request):
    date = dt.date.today()
    images = Image.latest_showoffs()
    return render(request, 'showme/liveshowoffs.html', {"date": date, "images": images})


def savedshowoffs(request, past_date):

    try:
        # converting data from the string url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # raising 404 error page
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(liveshowoffs)

    return render(request, 'showme/savedshowoffs.html', {"date": date})


def detail(request, image_id):
    image = Image.objects.get(id=image_id)
    return render(request, 'showme/details.html', {"image": image})
