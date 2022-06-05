from django.shortcuts import render
import json


def IndexPage(request):
    """Main page of the site"""
    q = request.GET.get('q', None)
    alarms_tmp = json.load(open("alarms.json"))
    alarms = {}
    if q:
        for key, value in alarms_tmp.items():
            info = {}
            for k2, v2 in value["districts"].items():
                if q.lower() in k2.lower():
                    info[k2] = v2
            if info:
                value["districts"] = info
                alarms[key] = value
            else:
                if q.lower() in key.lower():
                    alarms[key] = value
    else:
        alarms = alarms_tmp

    context = {
        "alarms": alarms.items(),
        'q': q,
    }
    return render(request, "main/index.html", context)
