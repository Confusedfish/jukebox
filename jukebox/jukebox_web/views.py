# -*- coding: UTF-8 -*-

from django.shortcuts import render_to_response
from django.core.context_processors import csrf
from django.http import HttpResponseRedirect
from django.contrib.auth import logout as auth_logout
from django.template import RequestContext
from django.contrib.messages.api import get_messages
from django.conf import settings
from jukebox.jukebox_core.models import Song, Genre
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.models import AnonymousUser

def index(request):
    if request.user.is_authenticated():
        request.session.set_expiry(settings.SESSION_TTL)

        genres = Genre.objects.all()
        years = Song.objects.values("Year").distinct()
        years = years.exclude(Year=None).exclude(Year=0).order_by("Year")

        context = {
            "username": request.user.get_full_name(),
            "genres": genres,
            "years": years
        }
        context.update(csrf(request))
        return render_to_response('index.html', context)
    else:
        return HttpResponseRedirect('login')

def login_page(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/')
    else:
        return render_to_response(
            'login.html',
            {
                "backends": settings.SOCIAL_AUTH_ENABLED_BACKENDS,
            },
            RequestContext(request)
        )

def login_guest(request):
    user = authenticate(username="guest", password="clear")
    if user is not None:
        if user.is_active:
            login(request, user)
    return HttpResponseRedirect('/')

def login_error(request):
    messages = get_messages(request)
    return render_to_response(
        'login.html',
        {"error": messages},
        RequestContext(request)
    )

def logout(request):
    auth_logout(request)
    return HttpResponseRedirect('/')

def language(request, language):
    from django.utils.translation import check_for_language
    from django.utils import translation

    response = HttpResponseRedirect("/")
    if language and check_for_language(language):
        if hasattr(request, "session"):
            request.session["django_language"] = language
        else:
            response.set_cookie(settings.LANGUAGE_COOKIE_NAME, language)
        translation.activate(language)

    return response
