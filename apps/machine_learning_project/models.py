from django.db import models

# Create your models here.

class MachineLearning(models.Model):
    nama = models.CharField(max_length=128)
    pemilik = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

class MachineLearningAlgoritm(models.Model):
    name = models.CharField(max_length=128)
    deskripsi = models.CharField(max_length=1000)
    kode = models.CharField(max_length=50000)
    versi = models.CharField(max_length=128)
    pemilik = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_endpoint = models.ForeignKey(MachineLearning, on_delete=models.CASCADE)

class MachineLearningAlgoritmStatus(models.Model):
    status = models.CharField(max_length=128)
    active = models.BooleanField()
    created_by = models.CharField(max_length=128)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MachineLearningAlgoritm, on_delete=models.CASCADE, related_name = "status")

class MachineLearningRequest(models.Model):
    input_data = models.CharField(max_length=10000)
    full_response = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    feedback = models.CharField(max_length=10000, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)
    parent_mlalgorithm = models.ForeignKey(MachineLearningAlgoritm, on_delete=models.CASCADE)