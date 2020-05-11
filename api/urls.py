from django.urls import path, include
# from .views import StudentApiView, StudentDetail, UserList, UserDetail
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from.views import StudentApiView


router = routers.DefaultRouter()
router.register('students', StudentApiView, basename='students')

urlpatterns = [
    # path('', StudentApiView.as_view()),
    # path('detail/<int:id>/', StudentDetail.as_view()),
    # path('user/<int:id>/', UserDetail.as_view()),
    # path('user/', UserList.as_view()),
    path('api/', include(router.urls))

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
