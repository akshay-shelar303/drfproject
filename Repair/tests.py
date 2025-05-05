# from django.test import TestCase
# from rest_framework.test import APITestCase
# from rest_framework import status
# from .models import Repair


# class RepairAPITestCase(APITestCase):
#     def setUp(self):
#         # Create a repair instance for testing
#         self.repair = Repair.objects.create(
#             customer_name="Test User",
#             phone_no="1234567890",
#             laptop_model="Test Laptop",
#             issue_description="Test Issue",
#             status="Pending",
#             user=1 # Assuming user with ID 1 exists
#         )
#         self.url = f'/api/repairs/{self.repair.id}/'  # Adjust the URL as per your routing

#     def test_get_repair(self):
#         response = self.client.get(self.url)
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.assertEqual(response.data['name'], "Test Repair")

#     def test_update_repair(self):
#         data = {
#             "name": "Updated Repair",
#             "description": "Updated Description",
#             "status": "Completed"
#         }
#         response = self.client.put(self.url, data, format='json')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)
#         self.repair.refresh_from_db()
#         self.assertEqual(self.repair.name, "Updated Repair")

#     def test_delete_repair(self):
#         response = self.client.delete(self.url)
#         self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
#         with self.assertRaises(Repair.DoesNotExist):
#             Repair.objects.get(id=self.repair.id)

