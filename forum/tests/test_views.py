from django.urls import reverse
from django.test import TestCase, Client
from forum.models import forum, Discussion


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()  # act as client
        self.obj = forum.objects.create(name='avigail',
                                        email='avigails90@gmail.com',
                                        topic='test',
                                        description='help my')

    def test_home_GET(self):
        ''' test if the forum home page display to client '''
        response = self.client.get(reverse('forum:home'))  # client try to go to the forum home page
        self.assertEqual(response.status_code, 200)  # success render code is 200
        self.assertTemplateUsed(response, 'base_layout.html')  # inherit the base.html
        self.assertTemplateUsed(response, 'forum/home.html')  # display this template

    def test_addInForum_POST_Valid(self):
        ''' test if we can add subject to forum using the form '''
        forum_count = forum.objects.count()  # counting all subjects in forum prior to add attempt
        response = self.client.post(reverse('forum:addInForum'), {'name': 'avigail',
                                                                  'email': 'avigails90@gmail.com',
                                                                  'topic': 'test',
                                                                  'description': 'help my', })  # the add attempt

        self.assertEqual(response.status_code, 302)  # if add successfully than redirect
        self.assertEqual(forum.objects.count(), forum_count + 1)  # means we added another subject using form

    def test_addInForum_POST_NOT_Valid(self):
        ''' test to check function if form is not valid '''
        response = self.client.post(reverse('forum:addInForum'), {'name': '',
                                                                  'email': '',
                                                                  'topic': '',
                                                                  'description': ''})

        self.assertEqual(response.status_code, 200)  # if not valid we render the page again

    def test_addInDiscussion_POST_Valid(self):
        ''' test if we can add comment to a subject using the comment form '''
        Discussion_count = Discussion.objects.count()  # counting all subjects in forum prior to add attempt
        response = self.client.post(reverse('forum:addInDiscussion'), {'forum': self.obj.pk,
                                                                       'discuss': 'check',
                                                                       'name': 'avigail', })  # the add attempt

        self.assertEqual(response.status_code, 302)  # if add successfully than redirect
        self.assertEqual(Discussion.objects.count(), Discussion_count + 1)  # means we added another subject using form

    def test_addInDiscussion_POST_NOT_Valid(self):
        ''' test to check function if comment form is not valid '''

        response = self.client.post(reverse('forum:addInForum'), {'forum': '',  # here it is Not valid
                                                                  'discuss': 'check',
                                                                  'name': 'avigail', })

        self.assertEqual(response.status_code, 200)  # if not valid we render the page again
