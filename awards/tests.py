from django.test import TestCase
from datetime import datetime
from .models import *





# Create your tests here.
class TestUser (TestCase):
    def setUp(self):
        self.joe = User(username='joe', password='6868uy')
        self.joe.save()

    def tearDown(self):
        User.objects.all().delete()

    def test_instance(self):
        self.assertEqu
        al(self.joe.username, 'joe')
        self.assertEqual(self.joe.password, '6868uy')
        self.assertTrue(isinstance(self.joe, User))

class TestUserProfile (TestCase):
    def setUp(self):

        self.joe = User(username='joe', password='6868uy')
        self.joe.save()
        self.joey = Profile(user=self.joe, first_name='Joel',
                                  user_name='joey', bio='cool', email='joe@gmail.com',number= '0722222222')
        self.joey.save_profile(self.joe)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.joey.first_name, 'Joel')
        self.assertEqual(self.joey.user_name, 'joey')
        self.assertEqual(self.joey.bio, 'i cool')
        self.assertEqual(self.joey.email, 'joe@gmail.com')
        self.assertEqual(self.joey.number, '0722222222')
        self.assertTrue(isinstance(self.joey, Profile))

    def test_save_profile(self):
        self.joey.save_profile(self.joe)
        self.assertTrue(len(Profile.objects.all()) > 0)

class TestPost (TestCase):
    def setUp(self):
        self.joe = User(username='joe', password='6868uy')
        self.joe.save()
        self.forest = Post(uploaded_by=self.joe, landing_image='test.jpg',
                              description='lovely', post_date=datetime.utcnow())
        self.forest.save_post(self.joe)

    def tearDown(self):
        Post.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.forest.uploaded_by, self.joe)
        self.assertEqual(self.forest.landing_image, 'test.jpg')
        self.assertEqual(self.forest.description, 'lovely')
        self.assertTrue(isinstance(self.forest, Post))

    def test_all_posts(self):
        self.assertTrue(len(Post.objects.all()) > 0)

    def test_user_posts(self):
        self.assertTrue(len(Post.get_user_profile(self.joe)) > 0)





