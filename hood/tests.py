from django.test import TestCase
from django.contrib.auth.models import User
from .models import Posts, Business, NeighbourHood, UserProfile
# Create your tests here.
class ProfileTestClass(TestCase):
    def setUp(self):
        
        user = User.objects.create(
            username="test_user", first_name="dan", last_name="dante"
        )
        neighbourhood = NeighbourHood.objects.create(
            hood_name='hood', hood_admin=user, hood_location='location', occupants_count='333'
        )

        self.profile = UserProfile(
            username = user,
            hood=neighbourhood,
            email = "image@jpg",
            #followers = "followers.set()"
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.profile, UserProfile))

    def test_save_method(self):
        self.profile.save_profile()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)

    def test_delete_method(self):
        self.profile.save_profile()
        self.profile.delete_profile()
        users = User.objects.all()
        self.assertTrue(len(users) > 0)  


class HoodTestClass(TestCase):  # Website class test
    def setUp(self):
        # creating a user
        user = User.objects.create(
            username="test_user", first_name="site", last_name="awards"
        )
        

        self.hood = NeighbourHood(
            hood_admin= user,
            hood_name = 'nai',
            hood_location = "Test Site",
            occupants_count="3333",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, NeighbourHood))

    def test_save_method(self):
        self.hood.save_hood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):
        self.hood.save_hood()
        self.hood.delete_hood()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 0)          

class BusinessTestClass(TestCase):
    def setUp(self):
        
        user = User.objects.create(
            username="test_user", first_name="dan", last_name="dante"
        )
        neighbourhood = NeighbourHood.objects.create(
            hood_name='hood', hood_admin=user, hood_location='location', occupants_count='333'
        )

        self.business = Business(
            business_name = 'user',
            business_user = user,
            hood=neighbourhood,
            business_email = "image@jpg",
            #followers = "followers.set()"
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.business, Business))

    def test_save_method(self):
        self.business.save_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) > 0)

    def test_delete_method(self):
        self.business.save_business()
        self.business.delete_business()
        businesses = Business.objects.all()
        self.assertTrue(len(businesses) == 0)        

class PostTestClass(TestCase):
    def setUp(self):
        
        user = User.objects.create(
            username="test_user", first_name="dan", last_name="dante"
        )
        neighbourhood = NeighbourHood.objects.create(
            hood_name='hood', hood_admin=user, hood_location='location', occupants_count='333'
        )

        self.post = Posts(
            author = user,
            body = 'body',
            
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.post, Posts))

    def test_save_method(self):
        self.post.save_post()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) > 0)

    def test_delete_method(self):
        self.post.save_post()
        self.post.delete_post()
        posts = Posts.objects.all()
        self.assertTrue(len(posts) == 0)                  