from datacenter.models import Visit, Passcard
from django.shortcuts import render


def storage_information_view(request):
    no_leaved_persons = Visit.objects.filter(leaved_at__isnull=True)
    serialized_non_closed_visits = []

    for person in no_leaved_persons:
        entered_at = person.entered_at
        entered_at = entered_at.astimezone()
        duration = Visit.format_duration(Visit.get_duration(person))
        non_closed_visit = {
                'who_entered': person.passcard,
                'entered_at': entered_at,
                'duration': duration,
            }
        serialized_non_closed_visits.append(non_closed_visit)

    context = {'non_closed_visits': serialized_non_closed_visits}
    return render(request, 'storage_information.html', context)
