from django.test import TestCase, Client
from django.urls import reverse
from success_story.models import story


class TestViews(TestCase):
    # this class will test the views of the success_story app
    def setUp(self): # this method will run before every test
        self.client = Client()
        self.create_story_url = reverse('success_story:create_story')
        self.obj = story.objects.create(date='2024-03-09',
                                        name='test',
                                        text='testing')

    def test_all_stories_GET(
            self):  # Tests if accessing the "all_stories" view with a "GET" request returns a status code of 200 and uses the correct template.
        response = self.client.get(reverse('success_story:all_stories'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/all_stories.html')

    def test_create_story_GET(
            self):  # Checks if accessing the "create_story" view with a "GET" request returns a status code of 200 and uses the correct template.
        response = self.client.get(reverse('success_story:create_story'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')

    def test_create_story_POST_valid(
            self):  # Validates that submitting valid story data to the "create_story" view via a "POST" request results in a redirect to the "all_stories" page.
        response = self.client.post(reverse('success_story:create_story'), {'date': '2024-03-09',
                                                                            'name': 'test',
                                                                            'text': 'testing'})
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/success_story/all_stories/')

    def test_create_story_POST_Not_valid(
            self):  # Ensures that submitting invalid story data to the "create_story" view via a "POST" request returns a status code of 200 and renders the same form template for correction.
        response = self.client.post(reverse('success_story:create_story'), {'date': '2024-03-09',
                                                                            'name': '',  # fail here
                                                                            'text': 'testing'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'success_story/create_story.html')
