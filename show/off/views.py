from django.shortcuts import render,redirect
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'showme/welcome.html')

def liveshowoffs(request):
    date = dt.date.today()
    return render(request, 'showme/liveshowoffs.html', {"date": date})

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

    return render(request, 'showme/savedshowoffs.html', {"date":date})
