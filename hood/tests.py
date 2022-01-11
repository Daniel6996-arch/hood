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
            hood_name = 'nai'
            hood_location = "Test Site",
            occupants_count="Description",
        )
    def test_instance(self):
        self.assertTrue(isinstance(self.hood, NeighbourHood))

    def test_save_method(self):
        self.hood.save_site()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) > 0)

    def test_delete_method(self):
        self.hood.save_site()
        self.hood.delete_site()
        hoods = NeighbourHood.objects.all()
        self.assertTrue(len(hoods) == 0)          