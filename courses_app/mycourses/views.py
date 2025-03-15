from django.shortcuts import render

def my_page(request):
    if request.user.is_authenticated:
        message = "This is the Courses page"
    else:
        message = "You have no permissions to view this page"

    return render (request, "mycourses/my_page.html", {"message": message,})


