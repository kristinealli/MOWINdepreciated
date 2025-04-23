from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.utils import timezone
from cards.models import UserCardProgress

@login_required
def user_progress_log(request):
    # Filter progress logs for today
    today = timezone.now().date()
    todays_progress_log = UserCardProgress.objects.filter(
        user=request.user,
        last_reviewed__date=today
    )

    context = {
        'todays_progress_log': todays_progress_log
    }
    return render(request, 'cards/user_progress_log.html', context) 