from django.urls import path,include

from rest_framework.routers import DefaultRouter 
# from .views import PostListRequest , PostDetailView
from .views import PostView

router = DefaultRouter()
router.register(r'',PostView,basename='posts')

urlpatterns = [
    # path('', PostListRequest.as_view()),
    # path('<int:pk>/',PostDetailView.as_view())
    # path('',PostView.as_view({'get':'list', 'post':'create'})),
    # path('<int:pk>/',PostView.as_view({'get':'retrieve', 'put':'update','delete':'destroy'})),
    path('',include(router.urls))
]
