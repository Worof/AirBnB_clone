"""
Airbnb Clone Project - Console Documentation

Overview
--------
The console is a custom command-line interface for our Airbnb clone application,
which serves as an administrative tool to handle data models interactively. It
provides functionality to create, update, destroy, and manage objects, as well
as store and persist objects to a JSON file.

Starting the Console
--------------------
To start the console, navigate to the root directory of the project and execute
the `console.py` script:

$ ./console.py

Or, if you need to specify the interpreter:

$ python3 console.py

Command List
------------
`create` - Creates a new instance of a specified class and prints the `id`.
`show` - Prints the string representation of an instance based on class name and `id`.
`destroy` - Deletes an instance based on the class name and `id`.
`all` - Prints all instances of a class or if no class is specified, all instances of every class.
`update` - Updates an instance based on the class name and `id` by adding or updating its attributes.
`count` - Retrieves the number of instances of a certain class.
`quit` - Exits the console.
`EOF` - End of file, exits the console.

Usage Examples
--------------
- Create a new `User`:
  create User
- Show a `User` with a specific `id`:
  show User 1234-5678
- Destroy a `Place` with a specific `id`:
  destroy Place 1234-5678
- List all instances of `User`:
  all User
- Update a `User`'s email with a specific `id`:
  update User 1234-5678 email "example@example.com"
- Count all `Place` instances:
  Place.count()

Extending the Console
---------------------
The console can be extended with new commands by adding methods to the `HBNBCommand`
class in `console.py`. The new command should be prefixed with `do_`, followed by
the command name. It will be recognized and made available during the next console
session.

Testing the Console
-------------------
Unittests for the file storage engine can be found in `tests/` directory and can
be executed using the standard unittest module:

$ python3 -m unittest discover tests

This documentation provides a brief guide on how to use the command-line console
for the Airbnb clone project. It is advised to keep it updated with any changes to
the console functionality or command syntax.