from django.conf.urls import url, include
from django.views import generic

from . import views


urlpatterns = [
    # url('^$', generic.RedirectView.as_view(
    #     url='./departments/'), name="index"),
    # url('^departments/', include(views.DepartmentViewSet().urls)),
    # url('^users/', include(views.EmployeeViewSet().urls)),

    url(r'^json/list/', views.user_list),
]
