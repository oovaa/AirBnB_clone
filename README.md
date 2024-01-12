# Welcome to the AirBnB Clone Project

## Project Description

The AirBnB Clone project is an exciting venture that guides you through the development of a fully functional web application, starting with the creation of a command interpreter. This project lays the foundation for managing various AirBnB objects, including States, Cities, Places, Amenities, Reviews, and Users. By successfully completing this project, you'll acquire skills that seamlessly integrate into subsequent tasks such as HTML/CSS templating, database storage, API, and front-end integration.

## Project Overview

### Key Objectives

1. **Parent Class (BaseModel):** Establish a parent class (BaseModel) for initiating, serializing, and deserializing future instances.

2. **Serialization Flow:** Develop a simple flow for serialization and deserialization, transitioning smoothly between Instance, Dictionary, JSON string, and file.

3. **Object Classes:** Create classes for essential AirBnB entities (User, State, City, Place, Amenity, Review) that inherit from the BaseModel.

   - **State (models/state.py):**
     - **Public class attributes:**
       - name: string - empty string

   - **City (models/city.py):**
     - **Public class attributes:**
       - state_id: string - empty string: it will be the State.id
       - name: string - empty string

   - **Amenity (models/amenity.py):**
     - **Public class attributes:**
       - name: string - empty string

   - **Place (models/place.py):**
     - **Public class attributes:**
       - city_id: string - empty string: it will be the City.id
       - user_id: string - empty string: it will be the User.id
       - name: string - empty string
       - description: string - empty string
       - number_rooms: integer - 0
       - number_bathrooms: integer - 0
       - max_guest: integer - 0
       - price_by_night: integer - 0
       - latitude: float - 0.0
       - longitude: float - 0.0
       - amenity_ids: list of string - empty list: it will be the list of Amenity.id later

   - **Review (models/review.py):**
     - **Public class attributes:**
       - place_id: string - empty string: it will be the Place.id
       - user_id: string - empty string: it will be the User.id
       - text: string - empty string

4. **User Class (models/user.py):**
   - **Public class attributes:**
     - email: string - empty string
     - password: string - empty string
     - first_name: string - empty string
     - last_name: string - empty string

5. **FileStorage Update:**
   - Ensure FileStorage correctly manages the serialization and deserialization of User instances.

6. **Command Interpreter Update (console.py):**
   - Enhance your command interpreter to allow commands like show, create, destroy, update, and all related to the User class.
?## How to Use the Command Interpreter

### Starting the Command Interpreter

To start the AirBnB command interpreter, follow these steps:

1. Open your terminal or command prompt.

2. Navigate to the project directory containing the `console.py` script.

3. Run the following command:

    ```bash
    $ ./console.py
    ```

### Basic Commands

Once the command interpreter is running, you can use the following basic commands:

- **help:** Displays a list of available commands with brief descriptions.
  
    ```bash
    (hbnb) help
    ```

- **create \<class_name>:** Creates a new instance of the specified class.

    ```bash
    (hbnb) create User
    ```

- **show \<class_name> \<id>:** Displays the string representation of an instance based on the class name and ID.

    ```bash
    (hbnb) show User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662
    ```

- **destroy \<class_name> \<id>:** Deletes an instance based on the class name and ID.

    ```bash
    (hbnb) destroy User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662
    ```

- **all [\<class_name>]:** Displays all instances or instances of a specific class if provided.

    ```bash
    (hbnb) all
    (hbnb) all User
    ```

- **update \<class_name> \<id> \<attribute_name> "\<attribute_value>":** Updates the specified attribute of an instance.

    ```bash
    (hbnb) update User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662 first_name "John"
    ```

### Examples

Here are some examples of using the command interpreter:

```bash
$ ./console.py
(hbnb) create User
3f3e5332-ecbc-42e5-8f82-8bbd60f0f662
(hbnb) show User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662
[User] (3f3e5332-ecbc-42e5-8f82-8bbd60f0f662) {'id': '3f3e5332-ecbc-42e5-8f82-8bbd60f0f662', 'created_at': '2024-01-12T12:00:00', 'updated_at': '2024-01-12T12:00:00'}
(hbnb) update User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662 first_name "John"
(hbnb) show User 3f3e5332-ecbc-42e5-8f82-8bbd60f0f662
[User] (3f3e5332-ecbc-42e5-8f82-8bbd60f0f662) {'id': '3f3e5332-ecbc-42e5-8f82-8bbd60f0f662', 'created_at': '2024-01-12T12:00:00', 'updated_at': '2024-01-12T12:01:00', 'first_name': 'John'}
(hbnb) all
["[User] (3f3e5332-ecbc-42e5-8f82-8bbd60f0f662) {'id': '3f3e5332-ecbc-42e5-8f82-8bbd60f0f662', 'created_at': '2024-01-12T12:00:00', 'updated_at': '2024-01-12T12:01:00', 'first_name': 'John'}"]
(hbnb) quit
$
```
## Learning Objectives

Upon completing the AirBnB Clone project, you should be proficient in the following concepts without relying on external resources:

1. **Creating a Python Package:**
   - Understand the process of creating a Python package for better code organization and reusability.

2. **Developing a Command Interpreter with the `cmd` Module:**
   - Learn how to implement a command interpreter in Python using the `cmd` module, providing a user-friendly interface.

3. **Implementing Unit Testing in a Large Project:**
   - Master the art of writing unit tests using the `unittest` module to ensure code reliability and correctness in a large project.

4. **Serializing and Deserializing a Class:**
   - Understand the principles of serializing and deserializing Python class instances to and from JSON format for data persistence.

5. **Reading and Writing JSON Files:**
   - Gain proficiency in reading from and writing to JSON files, an essential skill for data storage and retrieval.

6. **Managing Datetime:**
   - Learn how to effectively manage datetime in Python, a crucial aspect for tracking timestamps and updates.

7. **Understanding UUID:**
   - Grasp the purpose and usage of Universally Unique Identifiers (UUIDs) in Python for creating unique identifiers.

8. **Utilizing *args and **kwargs:**
   - Master the use of `*args` and `**kwargs` to handle variable numbers of arguments in Python functions, enhancing flexibility.

9. **Handling Named Arguments in a Function:**
   - Learn how to handle named arguments in Python functions for better code readability and maintainability.

## Resources

Explore the following resources to deepen your understanding of the concepts covered in the AirBnB Clone project:

- [cmd module](https://intranet.alxswe.com/rltoken/8ecCwE6veBmm3Nppw4hz5A)
- [cmd module in depth](https://intranet.alxswe.com/rltoken/uEy4RftSdKypoig9NFTvCg)
- [uuid module](https://intranet.alxswe.com/rltoken/KfL9TqwdI69W6ttG6gTPPQ)
- [datetime](https://intranet.alxswe.com/rltoken/1d8I3jSKgnYAtA1IZfEDpA)
- [unittest module](https://intranet.alxswe.com/rltoken/IlFiMB8UmqBG2CxA0AD3jA)
- [args/kwargs](https://intranet.alxswe.com/rltoken/C_a0EKbtvKdMcwIAuSIZng)
- [Python test cheatsheet](https://intranet.alxswe.com/rltoken/tgNVrKKzlWgS4dfl3mQklw)
- [cmd module wiki page](https://intranet.alxswe.com/rltoken/EvcaH9uTLlauxuw03WnkOQ)
- [python unittest](https://intranet.alxswe.com/rltoken/begh14KQA-3ov29KvD_HvA)
