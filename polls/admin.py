from django.contrib import admin

from .models import Question, Choice

"""
If you want to reorder the fields
"""
# class QuestionAdmin(admin.ModelAdmin):
# fields = ['pub_date', 'question_text']

"""
If you want to group fields into fieldsets
"""


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_recently_published')
    fieldsets = [
        (None, {'fields': ['question_text']}),
        ('Date Information', {'fields': ['pub_date']})
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)

admin.site.register(Choice)
