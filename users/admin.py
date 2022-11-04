from django.contrib import admin
from .models import User 
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

# Register your models here.

class UserModelAdmin(BaseUserAdmin):
    

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ('id' , 'name' , 'email', 'date_of_birth', 'is_admin','is_active','is_driver')
    list_filter = ('is_admin','is_driver')
    fieldsets = (
        ('User Credentials', {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('name','date_of_birth','phone_number')}),
        ('Permissions', {'fields': ('is_admin','is_driver')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name' ,'date_of_birth', 'password1', 'password2'),
        }),
    )
    search_fields = ('email',)
    ordering = ('email','id')
    


# Now register the new UserAdmin...
admin.site.register(User, UserModelAdmin)



