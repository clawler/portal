from django.test import TestCase, RequestFactory
from django.contrib.auth import get_user_model
import mock
from designsafe.apps.auth.models import AgaveOAuthToken
from designsafe.apps.auth.tasks import check_or_create_agave_home_dir
from designsafe.apps.auth.views import agave_oauth_callback


class LoginTestClass(TestCase):
  def setUp (self):
    User = get_user_model()

    user_with_agave = User.objects.create_user('test_with_agave', 'test@test.com', 'test')
    token = AgaveOAuthToken(
        token_type="bearer",
        scope="default",
        access_token="1234abcd",
        refresh_token="123123123",
        expires_in=14400,
        created=1523633447)
    token.user = user
    token.save()

    user_without_agave = User.objects.create_user(
        'test_without_agave', 'test@test.com', 'test')
    token = AgaveOAuthToken(
        token_type="bearer",
        scope="default",
        access_token="1234abcd",
        refresh_token="123123123",
        expires_in=14400,
        created=1523633447)
    token.user = user
    token.save()
    
  
  def tearDown(self):
    return
    
  """ @mock.patch('designsafe.apps.auth.models.AgaveOAuthToken.client')
  @mock.patch('agavepy.agave.Agave')
  def test_has_agave_file_listing(self, agave_client, agave):
    #agaveclient.return_value.files.list.return_value = [] // whatever the listing should look like
    #request.post.return_value = {} // some object that looks like a requests response
    
    self.client.login(username='test_with_agave', password='test')

    agave_client.files.list.return_value = {
        "name": ".",
        "path": "test",
        "lastModified": "2018-06-14T10:44:03.000-05:00",
        "length": 4096,
        "permissions": "ALL",
        "format": "folder",
        "mimeType": "text/directory",
        "type": "dir",
        "system": "designsafe.storage.default",
        "_links": {
            "self": {
                "href": "https://agave.designsafe-ci.org/files/v2/media/system/designsafe.storage.default/test"
            },
            "system": {
                "href": "https://agave.designsafe-ci.org/systems/v2/designsafe.storage.default"
            },
            "metadata": {
                "href": "https://agave.designsafe-ci.org/meta/v2/data?q=%7B%22associationIds%22%3A%11111111111111111111111-11111111-0001-001%22%7D"
            },
            "history": {
                "href": "https://agave.designsafe-ci.org/files/v2/history/system/designsafe.storage.default//test"
            }
        }
    } 
    
    resp = self.client.get('https://agave.designsafe-ci.org/files/v2/listings/designsafe.storage.default/test')
    print resp 
    self.assertEqual(resp.status_code, 200) """

  @mock.patch('designsafe.apps.auth.models.AgaveOAuthToken.client')
  @mock.patch('agavepy.agave.Agave')
  def test_no_agave_file_listing(self, agave_client, agave):
      self.client.login(username='test_without_agave', password='test')

      agave_client.files.list.return_value = {
          "status": "error", 
          "message": "File/folder does not exist", 
          "version": "test"
          }

      resp = self.client.get(
          'https://agave.designsafe-ci.org/files/v2/listings/designsafe.storage.default//test')
      print resp
      self.assertEqual(resp.status_code, 200)

  """ def test_user_without_agave_homedir_gets_redirected(self, mock_client, mock_Agave):

    pass """
    
  