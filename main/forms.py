from django import forms
from allauth.account.forms import SignupForm


class AdditionalSignupForm(SignupForm):
    mobile_number = forms.CharField(max_length=15, label="Mobile Number")

    def save(self, request):
        user = super(AdditionalSignupForm, self).save(request)
        user.mobile_number = request.POST.get('mobile_number')
        user.save()
        return user
