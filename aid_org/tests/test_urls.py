from django.test import TestCase
from django.urls import reverse, resolve
from aid_org.views import aid_org_detail
from aid_org.views import aid_org_list

class TestUrls(TestCase): 
    def test_aid_org_detail_url_is_resolved(self):
        """Test if the URL is resolved to the correct view function."""
        url = reverse('aid_org:detail', args=['latet'])
        self.assertEqual(resolve(url).func, aid_org_detail)

    def test_aid_org_list_url_is_resolved(self): 
        url = reverse('aid_org:list')
        self.assertEqual(resolve(url).func, aid_org_list)

    def test_aid_org_detail_url_with_different_slug_is_resolved(self):
        """Test if the detail URL is resolved to the correct view function with a different slug."""
        url = reverse('aid_org:detail', args=['another-slug'])
        self.assertEqual(resolve(url).func, aid_org_detail)

    def test_aid_org_detail_url_with_nonexistent_slug_is_resolved(self):
        """Test if the detail URL with a nonexistent slug still resolves to the correct view function.
        Note: This test checks URL resolution and not the view's behavior with nonexistent slugs."""
        url = reverse('aid_org:detail', args=['nonexistent-slug'])
        self.assertEqual(resolve(url).func, aid_org_detail)