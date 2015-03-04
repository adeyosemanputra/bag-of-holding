from django import forms

from tracker.models import Application, Engagement, EngagementComment, Activity, ActivityComment, Person


class ApplicationAddForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'description']


class ApplicationSettingsGeneralForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['name', 'description']


class ApplicationSettingsMetadataForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['platform', 'lifecycle', 'origin', 'industry', 'business_criticality', 'external_audience', 'internet_accessible']


class ApplicationSettingsTagsForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = ['tags']


class ApplicationDeleteForm(forms.ModelForm):
    class Meta:
        model = Application
        fields = []


class EngagementAddForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = ['start_date', 'end_date']
        labels = {
            'start_date': 'Scheduled start date',
            'end_date': 'Scheduled end date'
        }


class EngagementEditForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = ['status', 'start_date', 'end_date']
        labels = {
            'start_date': 'Scheduled start date',
            'end_date': 'Scheduled end date'
        }


class EngagementDeleteForm(forms.ModelForm):
    class Meta:
        model = Engagement
        fields = []


class EngagementCommentAddForm(forms.ModelForm):
    class Meta:
        model = EngagementComment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs = {'rows': 3})
        }


class ActivityAddForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['activity_type', 'users']
        labels = {
            'users': 'Assigned users'
        }


class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ['status', 'activity_type', 'users']
        labels = {
            'users': 'Assigned users'
        }


class ActivityDeleteForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = []


class ActivityCommentAddForm(forms.ModelForm):
    class Meta:
        model = ActivityComment
        fields = ['message']
        widgets = {
            'message': forms.Textarea(attrs = {'rows': 3})
        }


class PersonAddForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = ['first_name', 'last_name', 'email', 'phone_work', 'phone_mobile']