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

    class Post(models.Model):
    uploaded_by = models.ForeignKey(User, null=True, related_name='posts')
    name = models.CharField(max_length=200, null=True)
    landing_image = models.ImageField(upload_to='site-images/', null=True)
    description = models.TextField(blank=True)
    site_link = models.CharField(max_length=200, null=True)
    post_date = models.DateTimeField(auto_now_add=True)

    @classmethod
    def all_posts(cls):
        all_posts = cls.objects.all()
        return all_posts

    @classmethod
    def filter_by_search_term(cls, search_term):
        return cls.objects.filter(description__icontains=search_term)

    def get_user_profile(self, post):
        posts = self.objects.filter(uploaded_by=post.uploaded_by)
        return posts

    def get_one_post(self, post_id):
        return self.objects.get(pk=post_id)

    def save_post(self, user):
        self.uploaded_by = user
        self.save()

    def __str__(self):
        return self.name

