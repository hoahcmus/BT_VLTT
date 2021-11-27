from django.urls import path

from .views.hello_world import hello_world_view
from .views.post_list import post_list_view
# Add more imports for corresponding views
# For example:
# from .views.post_detail import post_detail

urlpatterns = [
    path("hello_world/", hello_world_view, name="hello_world"),
    path("post_list/", post_list_view, name="post_list"),
    # Add more url paths for corresponding screens
    # For example:
    # path("post_detail/", post_detail_view),
]
