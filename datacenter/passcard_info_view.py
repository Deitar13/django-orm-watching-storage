from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    passcard_visits = Visit.objects.filter(passcard_id=passcard)
    serialized_visits = []

    for passcard_visit in passcard_visits:
        duration = Visit.get_duration(passcard_visit)
        serialized_visits.append(
            {
                'entered_at': passcard_visit.entered_at,
                'duration': duration,
                'is_strange': Visit.is_visit_long(duration)
            },
        )

    context = {
        'passcard': passcard,
        'this_passcard_visits': serialized_visits
    }
    return render(request, 'passcard_info.html', context)
