from django import forms

from courses.models import Course

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ('title','description','image','slug')
        labels = {
            'title': 'Course Title',
            'description': 'Course Description'
        },
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'slug': forms.TextInput(attrs={"class":"form-control"}),
        }
        error_messages = {
            'title': {
                "required": "You must enter the Course Title",
                "max_length": "You must enter a maximum of 50 characters"
            },
            'description': {
                "required": "You must enter the Course description",
            }
        }

class CourseEditForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = "__all__"
        fields = ('title','description','image','slug','categories','isActive')
        labels = {
            'title': 'Course Title',
            'description': 'Course Description'
        },
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'slug': forms.TextInput(attrs={"class":"form-control"}),
            'categories': forms.SelectMultiple(attrs={"class":"form-control"})
        }
        error_messages = {
            'title': {
                "required": "You must enter the Course Title",
                "max_length": "You must enter a maximum of 50 characters"
            },
            'description': {
                "required": "You must enter the Course description",
            }
        }

class UploadForm(forms.Form):
    image = forms.ImageField()