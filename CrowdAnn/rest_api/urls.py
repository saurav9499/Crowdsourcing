from rest_framework import routers
from .views import ImageViewset, AnnotationViewset

router = routers.DefaultRouter()
router.register(r'images', ImageViewset)
router.register(r'annotation', AnnotationViewset)

urlpatterns = router.urls
