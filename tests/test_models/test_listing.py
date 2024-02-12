import unittest
from models.listing import AirBnBListing
from datetime import datetime

class TestAirBnBListing(unittest.TestCase):
    """Test cases for the AirBnBListing class."""

    def test_listing_creation(self):
        """Test that a listing is correctly created with given attributes."""
        name = "Test Listing"
        description = "Test Description"
        listing = AirBnBListing(name, description)
        self.assertEqual(listing.name, name)
        self.assertEqual(listing.description, description)
        self.assertTrue(isinstance(listing.id, str))
        self.assertTrue(isinstance(listing.created_at, datetime))

    def test_listing_display(self):
        """Test the display method of a listing."""
        listing = AirBnBListing("Test Display", "Display Description")
        with self.assertRaises(TypeError):
            # Assuming display method prints details and returns None
            result = listing.display()
            self.assertIsNone(result)

# More tests can be added here

if __name__ == '__main__':
    unittest.main()
