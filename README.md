Encryption Program
Overview
This is a simple encryption and decryption web application built using Flask and Python. The application allows users to encrypt and decrypt text using a custom encryption algorithm. It features a stylish and dynamic UI with a glitching background and custom cursor, creating an immersive experience for users.

Key Features:
Encrypt and decrypt messages securely.
View a list of previously encrypted messages.
Stylish and interactive user interface with a glitching background.
Custom cursor for an engaging experience.

How It Works

Encryption Algorithm:
The encryption algorithm used is a substitution cipher. Each character in the plaintext is mapped to a corresponding character from a shuffled set of characters (including spaces, punctuation, digits, and letters). 
The characters are shuffled randomly at the beginning to ensure that each encryption session has a different mapping.

Components:

Flask handles the web application backend.
Python's random module is used to shuffle the character set for the encryption key.
HTML, CSS, and JavaScript are used to build the user interface with a glitch effect and custom cursor.

Workflow:
The user enters text to be encrypted in the input field and submits the form.
The entered text is encrypted and displayed as cyphertext on the same page.
The user can also decrypt a message by entering encrypted text into the decryption form.
A list of previously encrypted messages is displayed on the page.


Setup

Prerequisites:
Python 3.x
Flask


Installation:
Clone the repository:


git clone https://github.com/5ar-G/Encryption-Program
cd encryption-program


Create a virtual environment (optional but recommended):

python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`


Install the required dependencies:

pip install -r requirements.txt


Run the Flask app:

python app.py

Open your browser and navigate to http://127.0.0.1:5000/.

Usage

Encrypting a Message:
Enter the text you want to encrypt into the "Enter text to encrypt" input field.
Click the "Encrypt" button to encrypt the message.
The encrypted text will be displayed on the page, and it will also be added to the list of encrypted messages.


Decrypting a Message:
Click the "Decrypt a Message" button to switch to the decryption form.
Enter the encrypted text into the "Enter text to decrypt" input field.
Click the "Decrypt" button to get the original plain text.


Viewing Encrypted Messages:
The list of previously encrypted messages will be displayed at the bottom of the page. Each entry shows the original text and its encrypted counterpart.


File Structure

encryption-program/
├── app.py               # Main Flask application
├── encrypt.py           # Encryption and decryption functions
├── templates/
│   └── index.html       # Main HTML file with the UI
└── requirements.txt     # Python dependencies

