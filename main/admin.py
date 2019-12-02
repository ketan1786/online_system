from django.contrib import admin
from django.middleware.csrf import get_token
from django.http import HttpRequest
from .models import User
from allauth.account.views import PasswordResetView


class AdminDisplay(admin.ModelAdmin):
    list_display = ['email', 'mobile_number', 'role']

    def save_model(self, request, obj, form, change):
        obj.role = admin

        super(AdminDisplay, self).save_model(request, obj, form, change)

        request.POST = {
            'email': obj.email,
            'csrfmiddlewaretoken': get_token(HttpRequest())
        }

        PasswordResetView.as_view()(request)


admin.site.register(User, AdminDisplay)
