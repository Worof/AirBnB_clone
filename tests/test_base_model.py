import unittest
from models.base_model import BaseModel

class TestBaseModel(unittest.TestCase):
    """Tests for the BaseModel class."""
    
    def test_id_creation(self):
        """Test that an ID is created."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "id"))
    
    def test_datetime_creation(self):
        """Test that created_at and updated_at are set."""
        instance = BaseModel()
        self.assertTrue(hasattr(instance, "created_at"))
        self.assertTrue(hasattr(instance, "updated_at"))
    
    def test_str_representation(self):
        """Test the __str__ method."""
        instance = BaseModel()
        expected = "[BaseModel] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(expected, str(instance))
    
    def test_save_method(self):
        """Test the save method updates `updated_at`."""
        instance = BaseModel()
        old_updated_at = instance.updated_at
        instance.save()
        self.assertNotEqual(old_updated_at, instance.updated_at)
    
    def test_to_dict_method(self):
        """Test the to_dict method."""
        instance = BaseModel()
        instance_dict = instance.to_dict()
        self.assertIsInstance(instance_dict, dict)
        self.assertIn("__class__", instance_dict)

if __name__ == "__main__":
    unittest.main()
