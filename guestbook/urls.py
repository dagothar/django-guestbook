from django.conf.urls import url
from . import views


urlpatterns = [
    # only for testing
    url(r'^test$', views.TestView.as_view(), name="test_view"),
    url(r'^$', views.EntryListView.as_view(), name="entry_list"),
]
