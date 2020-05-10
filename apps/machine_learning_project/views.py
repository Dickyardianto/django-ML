from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework import mixins

from apps.machine_learning_project.models import MachineLearning
from apps.machine_learning_project.serials import MachineLearningSerializer

from apps.machine_learning_project.models import MachineLearningAlgoritm
from apps.machine_learning_project.serials import MLAlgorithmSerializer

from apps.machine_learning_project.models import MachineLearningAlgoritmStatus
from apps.machine_learning_project.serials import MLAlgorithmStatusSerializer

from apps.machine_learning_project.models import MachineLearningRequest
from apps.machine_learning_project.serials import MLRequestSerializer

class EndpointViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MachineLearningSerializer
    queryset = MachineLearning.objects.all()


class MLAlgorithmViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet
):
    serializer_class = MLAlgorithmSerializer
    queryset = MachineLearningAlgoritm.objects.all()


def deactivate_other_statuses(instance):
    old_statuses = MachineLearningAlgoritmStatus.objects.filter(parent_mlalgorithm = instance.parent_mlalgorithm,
                                                        created_at__lt=instance.created_at,
                                                        active=True)
    for i in range(len(old_statuses)):
        old_statuses[i].active = False
    MachineLearningAlgoritmStatus.objects.bulk_update(old_statuses, ["active"])

class MLAlgorithmStatusViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.CreateModelMixin
):
    serializer_class = MLAlgorithmStatusSerializer
    queryset = MachineLearningAlgoritmStatus.objects.all()
    def perform_create(self, serializer):
        try:
            with transaction.atomic():
                instance = serializer.save(active=True)
                # set active=False for other statuses
                deactivate_other_statuses(instance)



        except Exception as e:
            raise APIException(str(e))

class MLRequestViewSet(
    mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet,
    mixins.UpdateModelMixin
):
    serializer_class = MLRequestSerializer
    queryset = MachineLearningRequest.objects.all()
