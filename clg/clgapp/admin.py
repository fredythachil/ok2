from django.contrib import admin

# Register your models here.
from .models import *

# Register your models here.
admin.site.register(Student)
admin.site.register(Branch)
admin.site.register(Department)
admin.site.register(Purpose)
