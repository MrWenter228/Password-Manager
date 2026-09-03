# Password Manager

A console-based password manager written in Python. The program allows users to store data for different websites, view, search, edit, and delete passwords.

## Features

* 🔐 PIN code verification before accessing the program
* ➕ Adding new passwords
* 📋 Viewing all saved records
* 🔍 Searching for a password by website name
* 🗑️ Deleting passwords
* ✏️ Changing existing passwords
* 🎲 Generating random passwords
* 💾 Saving data in JSON format
* ⚠️ Handling errors caused by incorrect user input

## Technologies Used

* `Python`
* `JSON`
* `os`
* `random`

## How the Program Works

The data is stored in a `passwords.json` file. When the program starts, it checks whether this file exists. If the file is found, the saved data is loaded automatically.

Each record contains:

* Website name;
* Username;
* Password.

The program also includes a menu that allows the user to choose the required action.

## What I Used in This Project

During the development of this project, I practiced:

* Functions (`def`);
* `while` and `for` loops;
* Conditional statements (`if`, `elif`, `else`);
* Lists and dictionaries;
* Working with files;
* JSON format;
* Error handling using `try/except`;
* Random password generation.

## Running the Project

To run the program, Python must be installed.

```bash
python test3.py
```

## Future Improvements

In the future, I plan to add:

* Password encryption;
* More secure data storage;
* The ability to edit usernames and website names;
* A graphical user interface;
* A more advanced authentication system.

> **Note:** This project was created for learning and practicing Python. Passwords are stored in a JSON file without encryption, so the program should not be used to store real confidential passwords.
