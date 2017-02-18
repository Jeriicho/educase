from __future__ import unicode_literals

from django.db import models

class Subject(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return self.name

class Science(models.Model):
    name = models.CharField(max_length=250)
    subcategory_exists = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", Subcategory : " + str(self.subcategory_exists)

class Economy(models.Model):
    name = models.CharField(max_length=250)
    subcategory_exists = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", Subcategory : " + str(self.subcategory_exists)

class Art(models.Model):
    name = models.CharField(max_length=250)
    subcategory_exists = models.BooleanField(default=False)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.name + ", Subcategory : " + str(self.subcategory_exists)

class Upload(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    file = models.FileField(max_length=10)

    def __str__(self):
        return self.subject + str(self.file)

class Test(models.Model):
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)

    def __str__(self):
        return self.subject