from django.contrib.auth.admin import UserAdmin, admin
from django.utils.translation import gettext_lazy as _

from users.models.profile import Profile
from users.models.users import User


class ProfileAdmin(admin.StackedInline):
    model = Profile
    fields = ('age', 'gender', 'weight', 'height', 'experience', 'photo')


@admin.register(User)
class UserAdmin(UserAdmin):
    change_user_password_template = None
    fieldsets = (
        (None, {'fields': ('email',)}),
        (_('Personal information'),
         {'fields': ('first_name', 'last_name',)}),
        (_('Permissions'), {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        (_('Important dates'),
         {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )
    list_display = ('id', 'full_name', 'email',)
    list_display_links = ('id', 'full_name')
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups',)
    search_fields = ('first_name', 'last_name', 'id', 'email',)
    ordering = ('-id',)
    filter_horizontal = ('groups', 'user_permissions',)
    readonly_fields = ('last_login',)

    inlines = (ProfileAdmin, )
