from django.urls import path

from .views.hello_world import *
from .views.post_list import *
# Add more imports for corresponding views
# For example:
# from .views.post_detail import post_detail

urlpatterns = [
    path("hello_world/", index, name="hello_world"),
    path("post_list/create/",createpost,name="create"),
    path("post_list/create/show/",show,name="show")

    # Add more url paths for corresponding screens
    # For example:
    # path("post_detail/", post_detail_view),
]
