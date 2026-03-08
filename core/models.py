from django.db import models
from django.contrib.auth.models import User

class ReferenceDocument(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='references/')
    content = models.TextField(blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)

class Questionnaire(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to='questionnaires/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    processed = models.BooleanField(default=False)

class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='questions')
    text = models.TextField()
    order = models.IntegerField()
    class Meta:
        ordering = ['order']

class Answer(models.Model):
    question = models.OneToOneField(Question, on_delete=models.CASCADE, related_name='answer')
    text = models.TextField()
    citations = models.TextField()
    confidence = models.FloatField(default=0.0)
    edited = models.BooleanField(default=False)
    
    def get_citations_list(self):
        if not self.citations:
            return []
        return [c.strip() for c in self.citations.split('|||') if c.strip()]
