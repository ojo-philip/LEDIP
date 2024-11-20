from django.shortcuts import render, get_object_or_404, redirect
from .models import Team
# Create your views here.

def team_page(request, slug, pk):
    team_detail = get_object_or_404(Team, slug=slug, pk=pk)

    context = {
        'team_detail': team_detail,
    }
    return render(request, 'blog/team.html', context)