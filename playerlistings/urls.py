from django.urls import path
from django.conf.urls import url
from playerlistings import views
from playerlistings.views import UploadFileView
urlpatterns = [
    path('upload/', UploadFileView.as_view(), name='People'),
    url(r'^api/players$', UploadFileView.get_player_list),
    url(r'^api/players/(?P<pk>[A-Za-z0-9]+)$', UploadFileView.player_detail)
]