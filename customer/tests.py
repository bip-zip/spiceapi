from django.test import TestCase
from .models import Customer
from rest_framework.test import APITestCase
from .serializers import CustomerSerializer

# for model
class CustomerModelTest(TestCase):
    def setUp(self):
        self.customer_data = {
            'name': 'SpiceUser1',
            'email': 'okok@gmail.com',
            'contact': '9800000000',
        }

    def tearDown(self):
        # Clean up test data
        Customer.objects.all().delete()

    def test_create_customer(self):
        # Test creating a new customer
        initial_count = Customer.objects.count()

        customer = Customer.objects.create(**self.customer_data)

        new_count = Customer.objects.count()
        self.assertEqual(new_count, initial_count + 1)

        # Verify the data was saved correctly
        saved_customer = Customer.objects.get(pk=customer.pk)
        self.assertEqual(saved_customer.name, self.customer_data['name'])
        self.assertEqual(saved_customer.email, self.customer_data['email'])
        self.assertEqual(saved_customer.contact, self.customer_data['contact'])

    def test_customer_str_method(self):
        # Test the __str__ method of the Customer model
        customer = Customer.objects.create(**self.customer_data)
        self.assertEqual(str(customer), self.customer_data['name'])


# for serializers
class CustomerSerializerTest(TestCase):

    def test_valid_data(self):
        data = {
            'name': 'SpiceUser1',
            'email': 'okok@gmail.com',
            'contact': '9800000000',
        }
        serializer = CustomerSerializer(data=data)
        self.assertTrue(serializer.is_valid())
        self.assertEqual(serializer.errors, {})

    def test_missing_required_field(self):
        data = {
            'email': 'okok@gmail.com',
            'contact': '9800000000',
        }
        serializer = CustomerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('name', serializer.errors)

    def test_invalid_email_format(self):
        data = {
            'name': 'SpiceUser1',
            'email': 'invalid_email',  # Invalid email format
            'contact': '9800000000',
        }
        serializer = CustomerSerializer(data=data)
        self.assertFalse(serializer.is_valid())
        self.assertIn('email', serializer.errors)

class CustomerAPISerializerTest(APITestCase):

    def test_create_customer_with_valid_data(self):
        data = {
            'name': 'SpiceUser1',
            'email': 'okok@gmail.com',
            'contact': '9800000000',
        }
        response = self.client.post('/api/customer/', data, format='json')
        self.assertEqual(response.status_code, 201)  # Check for successful creation
        self.assertEqual(Customer.objects.count(), 1)

    def test_create_customer_with_invalid_data(self):
        data = {
            'email': 'okok@gmail.com',
            'contact': '9800000000',
        }
        response = self.client.post('/api/customer/', data, format='json')
        self.assertEqual(response.status_code, 404)  # Check for bad request
        self.assertEqual(Customer.objects.count(), 0)  # No customer should be created
