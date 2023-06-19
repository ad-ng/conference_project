# speakers/views.py
from django.shortcuts import render

def speaker_list(request):
    speakers = [
        {'id': 1, 'name': 'Speaker 1', 'bio': 'Bio 1', 'contact': 'Contact 1'},
        {'id': 2, 'name': 'Speaker 2', 'bio': 'Bio 2', 'contact': 'Contact 2'},
        {'id': 3, 'name': 'Speaker 3', 'bio': 'Bio 3', 'contact': 'Contact 3'},
        {'id': 4, 'name': 'Speaker 4', 'bio': 'Bio 4', 'contact': 'Contact 4'},
        {'id': 5, 'name': 'Speaker 5', 'bio': 'Bio 5', 'contact': 'Contact 5'},
    ]
    context = {'speakers': speakers}
    return render(request, 'speakers/speaker_list.html', context)
     context = {'speakers': speakers}
    return render(request, 'speakers/speaker_list.html', context)
def create_speaker(request):
    return render(request, ' speakers/create_speaker.html')
def speaker_details(request, speaker_id):
    # Retrieve speaker information based on speaker_id (dummy data)
    speaker = {"id": speaker_id, "name": "Speaker", "bio": "Bio", "contact": "Contact"}
    return render(request, "speakers/speaker_details.html", {"speaker": speaker})
