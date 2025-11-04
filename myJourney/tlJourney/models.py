from django.db import models

# This model represents your learning journey details
class LearningJourney(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


# This model represents your personal information
class AboutMe(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    email = models.EmailField()
    hobby = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name
