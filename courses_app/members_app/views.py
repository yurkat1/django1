from django.shortcuts import render, redirect

def write_here(request):
    if request.method == "POST":
        user_writing = request.POST.get("user_writing")
        request.session["user_writing"] = user_writing
        return redirect("display_writing")
    return render(request, "members_app/writing.html")

def display_writing(request):
    user_writing = request.session.get("user_writing", "No text yet")
    return render(request, "members_app/display_writing.html",{"user_writing":user_writing})

def save_session(request):
    saved_data = request.session.get("saved_data", "No data entered")
    if request.method == "POST":
        request.session["saved_data"] = request.POST.get("saved_data")
        saved_data = request.session.get("saved_data", "No data entered")
    return render(request, "members_app/save_session.html", {"saved_data":saved_data})