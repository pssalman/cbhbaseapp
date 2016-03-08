from django.conf.urls import include, patterns, url

from rest_framework_nested import routers

from authentication.views import AccountViewSet, LoginView, LogoutView
from departments.views import AccountDepartmentsViewSet, DepartmentViewSet
from cbhbaseapp.views import IndexView

router = routers.SimpleRouter()
router.register(r'accounts', AccountViewSet)

router.register(r'departments', DepartmentViewSet)

accounts_router = routers.NestedSimpleRouter(
    router, r'accounts', lookup='account'
)
accounts_router.register(r'departments', AccountDepartmentsViewSet)

urlpatterns = [
    url('^api/v1/', include(router.urls)),
    url(r'^api/v1/', include(accounts_router.urls)),
    url(r'^api/v1/auth/login/$', LoginView.as_view(), name='login'),
    url(r'^api/v1/auth/logout/$', LogoutView.as_view(), name='logout'),
    url('^.*$', IndexView.as_view(), name='index'),
]
