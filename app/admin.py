from django.contrib import admin
from app.models import JobPost, Location, Author, Skills


class JobAdmin(admin.ModelAdmin):
    #this one will be reflected on db.sqlite3
    #which needs to refer to ao Field
    list_display=('__str__', 'title', 'date', 'salary')
    list_filter = ('date', 'salary', 'expiry')
    search_fields = ['title', 'description']
    search_help_text = 'Write in your query and hit enter'
    # fields = (('title', 'description'), 'expiry')
    # exclude = ['title']
    fieldsets = (('Basic information', {'fields':('title', 'description')}),
                 ('More information', {'classes': ('collapse', ),'fields':('expiry', 'salary', 'slug')}))

# Register your models here.
# admin.site.register(JobPost, JobAdmin)
admin.site.register(JobPost)
admin.site.register(Location)
admin.site.register(Author)
admin.site.register(Skills)

