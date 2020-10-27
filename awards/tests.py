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
        self.assertEqual
        (self.joe.username, 'joe')
        self.assertEqual(self.joe.password, '6868uy')
        self.assertTrue(isinstance(self.joe, User))

class TestUserProfile (TestCase):
    def setUp(self):

        self.joe = User(username='joe', password='6868uy')
        self.joe.save()
        self.joey = Profile(user=self.joe, name='Joel',
                                  user_name='joey', description='cool', email='joe@gmail.com',country= 'kenya')
        self.joey.save_profile(self.joe)

    def tearDown(self):
        Profile.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.joey.name, 'Joel')
        self.assertEqual(self.joey.user_name, 'joey')
        self.assertEqual(self.joey.description, 'i cool')
        self.assertEqual(self.joey.email, 'joe@gmail.com')
        self.assertEqual(self.joey.country, 'kenya')
        self.assertTrue(isinstance(self.joey, Profile))

    def test_save_profile(self):
        self.joey.save_profile(self.joe)
        self.assertTrue(len(Profile.objects.all()) > 0)

class TestProject (TestCase):
    def setUp(self):
        self.joe = User(username='joe', password='6868uy')
        self.joe.save()
        self.forest = Project(uploaded_by=self.joe, landing_page='test.jpg',
                              description='lovely', post_date=datetime.utcnow())
        self.forest.save_project(self.joe)

    def tearDown(self):
        Project.objects.all().delete()

    def test_instance(self):
        self.assertEqual(self.forest.uploaded_by, self.joe)
        self.assertEqual(self.forest.landing_page, 'test.jpg')
        self.assertEqual(self.forest.description, 'lovely')
        self.assertTrue(isinstance(self.forest, Project))

    def test_all_projects(self):
        self.assertTrue(len(Project.objects.all()) > 0)

    def test_user_projects(self):
        self.assertTrue(len(Project.get_user_profile(self.joe)) > 0)





