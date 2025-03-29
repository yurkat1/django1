from django.urls import path
from members_app.views import write_here, display_writing, save_session

urlpatterns = [
    path("writing/", write_here, name="writing"),
    path("display_writing/", display_writing, name="display_writing"),
    path("save_session/", save_session, name="save_session")

]

