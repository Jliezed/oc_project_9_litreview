from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

import appreview.views


app_name = "appreview"
urlpatterns = [
    path("home/", appreview.views.home, name="home"),
    path("my_posts/", appreview.views.my_posts, name="my_posts"),
    # Ticket paths
    path("ticket/add/", appreview.views.create_ticket, name="create_ticket"),
    path("ticket/<int:ticket_id>/update/", appreview.views.update_ticket,
         name="update_ticket"),
    path("ticket/<int:ticket_id>/delete/", appreview.views.delete_ticket,
         name="delete_ticket"),
    # Review paths
    path("review/add/", appreview.views.create_review, name="create_review"),
    path("review/<int:ticket_id>/add/",
         appreview.views.create_review_existing_ticket, name="create_review_ticket"),
    path("review/<int:review_id>/update/", appreview.views.review_update,
         name="update_review"),
    path("review/<int:review_id>/delete/", appreview.views.delete_review,
         name="delete_review"),
    # Other paths

    path("followers/", appreview.views.followers, name="followers"),

]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

