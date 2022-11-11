from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .forms import UserCreationForm, UserChangeForm
from .models import User, OtpCode
from django.contrib.auth.models import Group


@admin.register(OtpCode)
class OtpCodeAdmin(admin.ModelAdmin):
    list_display = ('phone_number', 'code', 'created')


class UserAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm

    list_display = ['email', 'phone_number', 'is_admin']
    list_filter = ['is_admin']
    readonly_fields = ['last_login']

    # ghaleb zaheri
    # is_superuser az PermissionsMixin miad va hame dastresi haro dare
    fieldsets = [
        ['Main', {'fields': ['email', 'phone_number', 'full_name', 'password']}],
        ['Permissions',
         {'fields': ['is_active', 'is_admin', 'is_superuser', 'last_login', 'groups', 'user_permissions']}],
    ]

    add_fieldsets = [
        ['Main', {'fields': ['phone_number', 'email', 'full_name', 'p1', 'p2']}],
    ]

    search_fields = ['email', 'phone_number']
    # dastebandi karbara
    ordering = ['full_name']
    # 2 ta meghdar ro kenar ham mizare
    # bara permission ha hast
    filter_horizontal = ['groups', 'user_permissions']

    # age yaro superuser nabod vali hame dastresi haro dash natone khodshe super kone ya baghiye ro
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)
        is_superuser = request.user.is_superuser
        if not is_superuser:
            form.base_fields['is_superuser'].disabled = True
        return form

# user khodemon ro ezaf mikonim
# admin.site.unregister(Group)
admin.site.register(User, UserAdmin)
