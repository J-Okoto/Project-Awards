from django.db import models

# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, null=True, related_name='profile')
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    profile_photo = models.ImageField(upload_to='images/', blank=True,default='dwf_profile.jpg')
    user_name = models.CharField(max_length=50, null=True)
    bio = models.TextField(blank=True)
    phone = models.IntegerField(null=True)
    email = models.CharField(max_length=50, null=True)

    def save_profile(self, current_user):
        self.user = current_user
        self.save()

    def __str__(self):
        return self.user_name