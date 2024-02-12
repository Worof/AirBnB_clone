
# AirBnB Clone Project

## Description

This AirBnB Clone project aims to replicate the basic functionality of the AirBnB platform for educational purposes. The project is structured into several parts: the command interpreter for managing application objects, the backend logic, and the frontend that users interact with. The focus of this README is the command interpreter, which is the first step in creating the backend structure.

## Command Interpreter

The command interpreter in this project is designed for data management of the application's various entities such as users, places, states, cities, amenities, and reviews. It allows for creating, updating, and deleting objects and storing/retrieving them from a JSON file.

### How to Start It

To start the command interpreter, navigate to the project's root directory in your terminal and run:

\`\`\`shell
./console.py
\`\`\`

This command launches the console application where you can enter command interpreter commands.

### How to Use It

The command interpreter supports several commands:

- \`quit\`: Exits the console
- \`EOF\`: Also exits the console (End-Of-File)
- \`create <class name>\`: Creates a new instance of a given class
- \`show <class name> <id>\`: Shows the details of an object of a given class and id
- \`destroy <class name> <id>\`: Deletes an object based on its class and id
- \`all [class name]\`: Shows all objects, or all objects of a specific class
- \`update <class name> <id> <attribute name> "<attribute value>"\`: Updates an object's attribute

### Examples

1. **Creating a new user:**

\`\`\`shell
create User
\`\`\`

2. **Displaying an existing user:**

\`\`\`shell
show User <user_id>
\`\`\`

3. **Deleting a user:**

\`\`\`shell
destroy User <user_id>
\`\`\`

4. **Listing all users:**

\`\`\`shell
all User
\`\`\`

5. **Updating a user's attribute:**

\`\`\`shell
update User <user_id> email "user@example.com"
\`\`\`

These examples provide a basic overview of interacting with the AirBnB clone command interpreter. Users can manage the application's data through these commands, enabling a foundational level of interaction with the backend system.

## Conclusion

This README provides an introduction to the command interpreter part of the AirBnB clone project. It outlines how to start the interpreter, the available commands, and examples of their use. This tool is essential for managing the application's data structures and serves as the backbone for further development of the AirBnB clone.



