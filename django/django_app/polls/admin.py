from django.contrib import admin

from .models import Choice, Question

# Register your models here.
class QuestionAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

class QuestionAdminFieldSet(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date']}),
    ]

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3

class ChoiceInlineTable(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdminFieldSetWuthChoice(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'],
                              'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline, ChoiceInlineTable]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

# admin.site.register(Question, QuestionAdmin)
# admin.site.register(Question, QuestionAdminFieldSet)
admin.site.register(Question, QuestionAdminFieldSetWuthChoice)


admin.site.register(Choice)