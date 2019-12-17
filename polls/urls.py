from django.contrib.admin.templatetags.admin_list import results
from django.urls import path
from django.views.generic import detail

from .views import index, detail, vote, results

urlpatterns = [
    path('', index, name='index'),
    path('<int:question_id>/', detail, name='detail'),
    path('<int:question_id>/results.', results, name='results'),
    path('<int:question_id>/vote/', vote, name='vote'),
]