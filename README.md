# Password Security Audit and Recommendation Report Generator

## Table of contents
* [General info](#general-info)
* [Features](#features)
* [Technologies Used](#technologies-used)
* [Prerequisites](#prerequisites)
* [Setup](#setup)
* [Testing for Development](#testing-for-evelopment)
* [Solutions](#solutions)
* [Tools and Plugins](#tools-and-plugins)
* [Future Plans](#future-plans)
* [Inspirations and Acknowledgments](#inspirations-and-acknowledgments)

## General info
This program is a password security audit tool designed for clients of 'Niebezpiecznik', a leading cybersecurity company in Poland. It allows users to check the security of their passwords by verifying if they meet specific complexity requirements. If a password fails to meet the requirements, the program generates a recommendation report to help users improve their password security.

## Features
- Verifies password complexity based on the following requirements:
  1. The password must contain at least one lowercase letter, one uppercase letter, and one special character.
  2. The password cannot contain spaces.
  3. The password must have a minimum length of 8 characters.
- User-friendly command-line interface for entering the password to be audited.
- Generates a detailed recommendation report if the password is not secure, indicating which requirements the password fails to meet.
- Provides a confirmation message for secure passwords.

## Technologies Used
- Python programming language

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)

## Prerequisites

To run this project, make sure you have Python 3.11.2 installed on your computer.

## Setup

To run the project locally, follow these steps:

- Clone this repository to your local machine.
- Navigate to the project directory.
- Run the program:
```
python3 password_security_audit.py
```

## Testing for Development

To ensure the correctness of the password_security_audit.py module, we have created a test suite in test_password_security_audit.py using pytest. The test cases cover different scenarios to verify the is_password_secure() function.

You can run the tests using pytest by running the following command in the terminal:
```
pytest test_password_security_audit.py
```

These tests will help ensure that the is_password_secure() function works correctly and that the password security audit program behaves as expected in different scenarios. If any of the tests fail, it will help identify the issues that need to be addressed in the code.

## Solutions
During the development of this project, several challenges were addressed and solutions were implemented:

1. **Checking Password Complexity**: The program checks for lowercase, uppercase, special characters, spaces, and minimum length using different conditional checks.

```
if not any(char.islower() for char in password):
    no_lower_char = True
```
2. Generating Recommendation Report: 

The program generates a customized recommendation report based on the specific requirements the password fails to meet.

```
if no_lower_char == True:
    print("Your password must contain at least one lowercase letter.")
```
3. Determining Password Security: The program uses a combination of boolean variables to determine the overall security of the password.
```
if any([lenght_too_short, contains_space, no_special_char, no_lower_char, no_upper_char]) == True:
    # Displaying the recommendation report
else:
    print("Your password is secure.")
```

## Tools and Plugins

The program uses the standard Python library and does not require any additional tools or plugins.

## Future Plans

- Implement password strength evaluation using popular password cracking algorithms and heuristics.
- Add the option to save and manage passwords securely.

## Inspirations and Acknowledgments

This project was inspired by the "Praktyczny Python" training course and was adapted from the original version for educational purposes.
