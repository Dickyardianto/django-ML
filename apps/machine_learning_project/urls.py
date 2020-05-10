from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from apps.machine_learning_project.views import EndpointViewSet
from apps.machine_learning_project.views import MLAlgorithmViewSet
from apps.machine_learning_project.views import MLAlgorithmStatusViewSet
from apps.machine_learning_project.views import MLRequestViewSet

router = DefaultRouter(trailing_slash=False)
router.register(r"machine_learning", EndpointViewSet, basename="mahchine_learning")
router.register(r"mlalgorithms", MLAlgorithmViewSet, basename="mlalgoritm")
router.register(r"mlalgorithmstatuses", MLAlgorithmStatusViewSet,
                basename="mlalgorithmstatuses")
router.register(r"mlrequests", MLRequestViewSet, basename="mlrequests")

urlpatterns = [
    url(r"^api/v1/", include(router.urls)),
]
