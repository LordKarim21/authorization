import secrets
import time

from django.http import Http404
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Profile
from .serializers import ProfileSerializer


class UserListAPIView(APIView):
    def get(self, request):
        user = request.user
        users_with_invite_code = Profile.objects.filter(activated_invite_code=True, invite_code=user.invite_code)
        serializer = ProfileSerializer(users_with_invite_code, many=True)
        return Response(serializer.data)


def auth_phone(request):
    if request.method == 'POST':
        phone_number = request.POST['phone_number']
        code = secrets.token_hex(2)
        Profile.objects.create(phone_number=phone_number, code=code)
        time.sleep(1)
        print(code)
        return redirect('auth_code', phone_number=phone_number)
    return render(request, 'auth_phone.html')


def auth_code(request, phone_number):
    try:
        profile = Profile.objects.get(phone_number=phone_number)
    except Profile.DoesNotExist:
        raise Http404("Profile not found")

    if request.method == 'POST':
        code = request.POST.get('code')
        if code == profile.code:
            return render(request, 'profile.html', {'phone_number': phone_number})
        else:
            error_message = "Invalid code. Please try again."
            return render(request, 'auth_code.html', {'phone_number': phone_number, 'error_message': error_message})
    return render(request, 'auth_code.html', {'phone_number': phone_number})


def profile(request, phone_number):
    try:
        profile = Profile.objects.get(phone_number=phone_number)
    except Profile.DoesNotExist:
        raise Http404("Profile not found")

    if request.method == 'POST':
        entered_invite_code = request.POST['invite_code']
        profile.invite_code = entered_invite_code
        profile.save()
    return render(request, 'profile.html', {'phone_number': phone_number})
