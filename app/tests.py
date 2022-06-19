from django.test import TestCase, TransactionTestCase
from .models import *
from django.contrib.auth.models import User

# Create your tests here.
class PostTestClass(TestCase):
    def setUp(self):
        self.new_post = Post(title='Test',post_description='test is a test', post_image='test,jpg')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_post, Post))

    def test_save_method(self):
        self.new_post.save()
        my_posts = Post.objects.all()
        self.assertTrue(len(my_posts) > 0)

    def test_delete_method(self):
        self.new_post.save()
        self.new_post.delete_post()
        my_posts = Post.objects.all()
        self.assertFalse(len(my_posts) > 0)
        
    def test_update_post(self):
        self.new_post.save()
        user_projects = Post.objects.all()
        self.assertTrue(len(user_projects) > 0)

    #clear after testing
    def tearDown(self):
        Post.objects.all().delete()
        
#business Testcases      
class BusinessTestClass(TransactionTestCase ):
    def setUp(self):
        self.new_business = Business(business_name='Bar',business_email_address='mybar@gmail.com',business_image='bar.jpg' )

    def test_instance(self):
        self.assertTrue(isinstance(self.new_business, Business))

    def test_business_create_method(self):
        self.new_business.save()
        test_businesses = Business.objects.all()
        self.assertTrue(len(test_businesses) > 0)

    def test_business_delete_method(self):
        self.new_business.save()
        self.new_business.delete_businesses()
        test_businesses = Business.objects.all()
        self.assertFalse(len(test_businesses) > 0)
        
    def test_update_business_method(self):
        self.new_business.save()
        test_businesses = Business.objects.all()
        self.assertTrue(len(test_businesses) > 0)

    def tearDown(self):
        Business.objects.all().delete()
        
#neighbourhood test cases     
class NeighborhoodTestClass(TestCase):
    def setUp(self):
        self.new_hood = Neighbourhood(image='hood.jpg',describe='neighbourhood for test',name='Muthaiga',neighbourhood_location='Kiambu Road',occupants_count='120',health_contacts='0700000000', police_contacts='03244444433',date_of_creation='19/7/2022')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_hood, Neighbourhood))

    def test_neighbourhood_create_method(self):
        self.new_hood.save()
        neighbourhoods = Neighbourhood.objects.all()
        self.assertTrue(len(neighbourhoods) > 0)
    
    def test_neighbourhood_delete_method(self):
        self.new_hood.save()
        self.new_hood.delete_neighbourhood()
        test_neighbourhoods = Neighbourhood.objects.all()
        self.assertFalse(len(test_neighbourhoods) > 0)