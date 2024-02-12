import uuid
from datetime import datetime
class AirBnBListing:
    """Represents an AirBnB listing in the AirBnB_clone project.

    Attributes:
        id (str): Unique identifier for the listing.
        name (str): Name of the listing.
        description (str): Description of the listing.
        created_at (datetime): The date and time when the listing was created.
    """

    def __init__(self, name, description):
        """Initializes an AirBnBListing with a name and description.

        Args:
            name (str): The name of the listing.
            description (str): The description of the listing.
        """
        self.id = str(uuid.uuid4())
        self.name = name
        self.description = description
        self.created_at = datetime.now()

    def display(self):
        """Prints details of the listing."""
        print(f"Listing ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Description: {self.description}")
        print(f"Created At: {self.created_at.strftime('%Y-%m-%d %H:%M:%S')}")


# Example usage
if __name__ == "__main__":
    listing = AirBnBListing("Sunny Apartment in Downtown", "A cozy, sunny apartment perfect for your weekend getaway.")
    listing.display()