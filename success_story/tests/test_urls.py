from django.test import SimpleTestCase
from django.urls import reverse, resolve
from success_story.views import all_stories, create_story


class TestUrls(SimpleTestCase):

    def test_all_stories_url_is_resolved(self): # this test checks if the url pattern resolved to the right view function
        url = reverse('success_story:all_stories')
        self.assertEqual(resolve(url).func, all_stories)

    def test_create_story_url_is_resolved(self): # this test checks if the url pattern resolved to the right view function
        url = reverse('success_story:create_story')
        self.assertEqual(resolve(url).func, create_story)