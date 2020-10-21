from django.contrib import admin
from .models import Task, Documents, WorkOrService, Conditions, Contract, Timing


admin.site.register(Task)
admin.site.register(Documents)
admin.site.register(WorkOrService)
admin.site.register(Conditions)
admin.site.register(Contract)
admin.site.register(Timing)
