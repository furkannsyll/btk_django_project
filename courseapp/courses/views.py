from django.shortcuts import get_object_or_404, redirect, render
from courses.forms import CourseCreateForm, CourseEditForm, UploadForm
from .models import Course, Category, UploadModel
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test

def index(request):
    courses = Course.objects.filter(isActive=1, isHome=True)
    categories = Category.objects.all()

    return render(request, "courses/index.html", {'categories': categories, 'courses': courses,})

def isAdmin(user):
    return user.is_superuser

@user_passes_test(isAdmin)
def create_course(request):
    # if not request.user.is_authenticated:
    #     return redirect("index")

    if request.method == "POST":
        form = CourseCreateForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect("/courses")
    
    else:
        form = CourseCreateForm()
        
    return render(request, "courses/create-course.html", { "form":form })

@login_required()
def course_list(request):
    courses = Course.objects.all()
    return render(request, "courses/course-list.html", {'courses': courses,})

def course_edit(request,id):
    course = get_object_or_404(Course, pk=id)
    if request.method == "POST":
        form = CourseEditForm(request.POST, request.FILES, instance=course)
        form.save()
        return redirect("course_list")
    else:
        form = CourseEditForm(instance=course)

    return render(request, 'courses/edit-course.html', {'form': form })

def course_delete(request,id):
   course = get_object_or_404(Course, pk=id)

   if request.method == "POST":
       course.delete()
       return redirect("course_list")

   return render(request, 'courses/course-delete.html', {'course': course })

def upload(request):
    if request.method == "POST":
        form = UploadForm(request.POST, request.FILES)

        if form.is_valid():
            model = UploadModel(image=request.FILES["image"])
            model.save()
            return render(request, "courses/success.html")
    else:
        form = UploadForm()
    return render(request, 'courses/upload.html', { "form":form })

def search(request):
    if "q" in request.GET and request.GET["q"] != "":
        q = request.GET["q"]
        courses = Course.objects.filter(isActive=True, title__contains=q).order_by("date")
        categories = Category.objects.all()
    else:
        return redirect("/courses")
    
    return render(request, 'courses/search.html', {'categories': categories, 'courses': courses,})

def details(request, slug):

    course = get_object_or_404(Course, slug=slug)

    context = {
        'course': course
    }
    return render(request, 'courses/details.html', context)

def getCoursesByCategoryName(request, slug):
    courses = Course.objects.filter(categories__slug=slug, isActive=True).order_by("date")
    categories = Category.objects.all()

    paginator = Paginator(courses, 3)
    page = request.GET.get('page',1)
    page_obj = paginator.page(page)

    return render(request, 'courses/list.html', {'categories': categories, 'page_obj': page_obj, 'selectedCategory': slug})