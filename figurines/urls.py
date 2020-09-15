from django.urls import path

from . import views

app_name = "figurines"

urlpatterns = [
    path("add_figurine/", views.add_figurine, name="add_figurine"),
    path("collection/", views.collection_user, name="collection"),
    path("search/", views.search, name="search"),
    path("did_you_see/", views.did_you_see, name="did_you_see"),
    path("post_detail/<int:id_post>/", views.post_detail, name="post_detail"),
    path("create_question/", views.create_question, name="create_question"),
    path(
        "create_question/<int:id_post>/",
        views.create_question,
        name="create_question",
    ),
    path("delete_figurine/", views.delete_figurine, name="delete_figurine"),
    path("report_post/<int:id_post>/", views.report, name="report"),
]
