import unittest
from django.urls import reverse, resolve
from forum.views import addInForum, addInDiscussion, home


class TestUrls(unittest.TestCase):
    def test_home_url_is_resolved(self):
        url = reverse('forum:home')
        self.assertEqual(url, '/forum/home/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, home)  # checks if the url pattern resolved to the right view function

    def test_addInForum_url_is_resolved(self):
        url = reverse('forum:addInForum')
        self.assertEqual(url, '/forum/addInForum/')     # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, addInForum)  # checks if the url pattern resolved to the right
                                                            # view function


    def test_addInDiscussion_url_is_resolved(self):
        url = reverse('forum:addInDiscussion')
        self.assertEqual(url, '/forum/addInDiscussion/')  # check if the url we want is same as we got
        self.assertEqual(resolve(url).func, addInDiscussion)  # checks if the url pattern resolved to the right
                                                                # view function
