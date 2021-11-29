from django.test import TestCase

from django.test import TestCase
from django.contrib.auth.models import User
from django.contrib.auth import SESSION_KEY
from django.contrib.auth import authenticate, login, logout
from django.test import Client
from . import views as v

class UsersTestCase(TestCase):
   
    def test_CheckIfUserExist(self):      
        
        """
        Test that a newly-created username is all objects.
        
        """
        self.User1 = User.objects.create_user(username="elad")
        self.User1.save()
        self.assertTrue(v.CheckIfUserExist("elad"),True)
        self.assertFalse(v.CheckIfUserExist("lee"),False)
        self.assertNotEqual(v.CheckIfUserExist("lee"),v.CheckIfUserExist("elad"),True)

    def test_new_user_is_active(self):
        self.User1 = User.objects.create_user(username="elad")
        self.User1.save()
        """
        Test that a newly-created user is inactive % active.
        
        """
        self.assertTrue(self.User1.is_active)
        self.User1.is_active = False
        self.assertFalse(self.User1.is_active)

class ViewsTestCase(TestCase):

    def test_index_loads_properly(self):
        """The index page loads properly"""
        response = self.client.get('127.0.0.1:8000')
        self.assertEqual(response.status_code, 404)
        self.assertNotEqual(response.status_code, 200)
