from django.shortcuts import render
from datetime import datetime


def index(request):

    # countdown = datetime(2022, 1, 1, 15, 0, 0);
    # now = datetime.now()
    # delta = countdown - now
    # print("delta =", delta)
    # days = delta.days
    # hours = delta.seconds // 3600
    # mins = (delta.seconds //60 ) % 60
    # secs = delta.seconds - hours * 3600 - mins * 60
    # print("delta2 = ", days, hours , mins, secs)

    return render(request, 'pokersociale/index.html')
    #, {
    #    'days': days,
    #    'hours': hours,
    #    'mins': mins,
    #    'secs': secs,
    #})
