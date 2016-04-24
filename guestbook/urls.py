from django.conf.urls import url
from . import views


urlpatterns = [
    # only for testing
    url(r'^test$', views.TestView.as_view(), name="test_view"),

    # shows the list of entries and a form to add a new entry
    # parameters: ?paginate_by - controls the number of entries on the page
    url(r'^$', views.EntryListView.as_view(), name="entry_list"),
]
