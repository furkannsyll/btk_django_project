from django import forms

from courses.models import Course

# class CourseCreateForm(forms.Form):
#     title = forms.CharField(
#         label="Course Title", 
#         required=True, 
#         error_messages={"required": "You must enter the Course Title"}, 
#         widget=forms.TextInput(attrs={"class":"form-control"})
#         )
#     description = forms.CharField(widget=forms.Textarea(attrs={"class":"form-control"}))
#     imageUrl = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
#     slug = forms.SlugField(widget=forms.TextInput(attrs={"class":"form-control"}))

class CourseCreateForm(forms.ModelForm):
    class Meta:
        model = Course
        # fields = "__all__"
        fields = ('title','description','imageUrl','slug')
        labels = {
            'title': 'Course Title',
            'description': 'Course Description'
        },
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'imageUrl': forms.TextInput(attrs={"class":"form-control"}),
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
        fields = ('title','description','imageUrl','slug','categories','isActive')
        labels = {
            'title': 'Course Title',
            'description': 'Course Description'
        },
        widgets = {
            'title': forms.TextInput(attrs={"class":"form-control"}),
            'description': forms.Textarea(attrs={"class":"form-control"}),
            'imageUrl': forms.TextInput(attrs={"class":"form-control"}),
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