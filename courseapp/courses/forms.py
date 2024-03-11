from django import forms

class CourseCreateForm(forms.Form):
    title = forms.CharField(label="Course Title", required=True, error_messages={"required": "You must enter the Course Title"})
    description = forms.CharField(widget=forms.Textarea)
    imageUrl = forms.CharField()
    slug = forms.SlugField()