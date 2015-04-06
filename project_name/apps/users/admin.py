from django import forms
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.models import Group
from .models import User


class UserCreationForm(forms.ModelForm):
    password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('email', 'display_name', )

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords didn't match")

        return password2

    def save(self, commit=True):
        user = super(UserCreationForm, self).save(commit=False)

        user.set_password(self.cleaned_data['password2'])

        if commit:
            user.save()

        return user


class UserChangeForm(forms.ModelForm):
    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = ('email', 'password', 'is_admin', 'is_staff')

    def clean_password(self):
        return self.initial['password']


@admin.register(User)
class UserAdmin(UserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ('email', 'display_name', 'is_admin', 'is_staff', 'is_active')
    list_filter = ('is_admin', )

    fieldsets = (
        (None, {
            'fields': ('email', 'display_name', 'password', 'last_login')
        }),
        ('Personal', {
            'fields': ('first_name', 'last_name', 'bio')
        }),
        ('Permissions', {
            'fields': ('is_admin', 'is_staff', 'is_active')
        })
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide', ),
            'fields': ('email', 'display_name', 'password1', 'password2')
        }),
    )

    search_fields = ('email', 'display_name')
    ordering = ('email', )

    filter_horizontal = ()

admin.site.unregister(Group)
