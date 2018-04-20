from django.contrib import admin
from .models import Events
from django import forms
import datetime

class EventsForm(forms.ModelForm):
    class Meta:
        model = Events
        fields = '__all__'

    def clean(self):
        event_date = self.cleaned_data.get('event_date')
        today = datetime.date.today()
        formatedDate = today.strftime("%Y-%m-%d")
        print(event_date)
        print(formatedDate)
        # form_date = datetime.datetime.strptime(event_date, "%Y-%m-%d")
        if today > event_date	:
            raise forms.ValidationError("Event Date can't be lesser than Present Date")
        return self.cleaned_data


class EventsAdmin(admin.ModelAdmin):
    form = EventsForm
    # list_display = ('topic', 'speaker', 'start_date', 'end_date')

admin.site.register(Events,EventsAdmin)