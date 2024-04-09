from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User, Group
from host.models import hostReq
import re
class HostViewsTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.create_host_url = reverse('host:create_host')
        # Setup for user and group
        self.group = Group.objects.create(name='מארח')
        self.user = User.objects.create_user(username='testuser', password='12345')
        self.superuser = User.objects.create_superuser(username='superuser', password='12345')
        self.user.groups.add(self.group)
        self.obj = hostReq.objects.create(
            fullname="Test Host",
            user=self.user,
            street="Test Street",
            city="Test City",
            housetype="Test Type",
            rooms=1,
            beds=1,
            kosher=True,
            phone="1234567890",
            email="test@test.com",
            description="Test Description",
            is_occupied=False
        )


    def test_create_host_GET_as_authorized_user(self):
        """Test if an authorized user can access the create_host view"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(self.create_host_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'host/create_host.html')

    def test_create_host_GET_as_unauthorized_user(self):
        """ Test if an unauthorized user can access the create_host view"""
        # Assume unauthorized_user is already created and not part of 'מארח' group or a superuser
        unauthorized_user = User.objects.create_user(username='unauthuser', password='12345')
        self.client.login(username='unauthuser', password='12345')
        response = self.client.get(self.create_host_url)
        self.assertEqual(response.status_code, 403)  # Assuming PermissionDenied raises a 403 Forbidden


    def test_all_hosts_GET(self):
        """Test if the all_hosts view returns the correct template and status code"""
        response = self.client.get(reverse('host:all_hosts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'host/all_hosts.html')

    def test_delete_host_as_authorized_user(self):
        """Test if an authorized user can access the delete_host view"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('host:delete_host', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 302)
        self.assertEqual(hostReq.objects.count(), 0)
    
    def test_delete_host_as_unauthorized_user(self):
        """Test if an unauthorized user can access the delete_host view"""
        unauthorized_user = User.objects.create_user(username='unauthuser', password='12345')
        self.client.login(username='unauthuser', password='12345')
        response = self.client.get(reverse('host:delete_host', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 403)
        
    
    def test_edit_host_as_authorized_user(self):
        """Test if an authorized user can access the edit_host view"""
        self.client.login(username='testuser', password='12345')
        response = self.client.get(reverse('host:edit_host', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'host/create_host.html')
        
    def test_edit_host_as_unauthorized_user(self):
        """Test if an unauthorized user can access the edit_host view"""
        unauthorized_user = User.objects.create_user(username='unauthuser', password='12345')
        self.client.login(username='unauthuser', password='12345')
        response = self.client.get(reverse('host:edit_host', args=[self.obj.pk]))
        self.assertEqual(response.status_code, 403)
        
    def test_export_excel(self):
        """Test if the export_excel view returns an excel file with the correct content"""
        self.client.login(username='testuser', password='12345')  # Log in the user
        response = self.client.get(reverse('host:export_excel'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'donations/excel')
        self.assertTrue(response['Content-Disposition'].startswith('attachment; filename=hosts'))
        self.assertTrue(response.content)  # Check that the response has content


    def test_export_pdf(self):
        """Test if the export_pdf view returns a PDF file with the correct content"""
        self.client.login(username='testuser', password='12345')  # Log in the user
        response = self.client.get(reverse('host:export_pdf'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response['Content-Type'], 'application/pdf')

        self.assertTrue(response.has_header('Content-Disposition'))
        content_disposition = response['Content-Disposition']

        # Use regular expressions to match the filename with or without quotes
        self.assertTrue(re.search(r'filename=(?:"?)(hosts\.pdf)(?:"?)', content_disposition))

        self.assertTrue(response.streaming_content)  # Check that the response has streaming content