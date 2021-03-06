from django.db import models


class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120, blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    update = models.DateField(auto_now_add=False, auto_now=True)

    # needed for viewing correctly
    def __str__(self):  # __unicode__ for 2x
        return self.email
