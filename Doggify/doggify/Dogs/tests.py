from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class TestAdoptionRequest(TestCase):
  """
  This class contaings tests for adoption requests
  """

  def setUp(self):
    """
    This method runs before the excution of each test case
    """
    self.client = Client()
    self.url = reverse("dogs:adoption_request")

  def test_double_request(self):
    """
    Tests not allowing doble adoption request
    """

    data = {
      "user" : "1",
      "dog" : "1",
      "adoption_date" : "27/05/2019"
    }

    response = self.client.post(self.url,data)

    self.assertEqual(reponse.status_code, 409)