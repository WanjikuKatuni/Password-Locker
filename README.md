# Password Locker

Simple Python App that stores account passwords in a vault and also generates passwords for a user. Touches on Test Driven Development using unittest (Python test framework).

## Technologies Used

- Python3.8
- unittest (Python test framework)


##### Setup Instructions and Installation

- Clone this repository to a location in your file system. `https://github.com/WanjikuKatuni/Password-Locker.git`
- Open terminal command line then navigate to the root folder of the application. `cd Password-locker`
- Run `./run.py` 


## Behaviour Driven Development

1. Displays Intro Message to user
    - OUTPUT: ""Welcome to PasswordLocker. What should we call you?""
   - INPUT: "Ann"
   - OUTPUT: "Hello Ann. what would you like to do?"
2. Enter Short Code
   - INPUT: "new"
   - INPUT: "new_user_name", "new_password", "confirm_password"
   - OUTPUT: "Ann 12345" 
   - ERROR: displays error incase of login error
3. Enter Short Code
   - INPUT: "log" 
   - OUTPUT: "Enter login details" 
   - OUTPUT: "guestuser 12345"
   - ERROR: displays error incase of login error
4. Enter Short Code
   - INPUT: "X"
   - OUTPU: "Leaving so soon? Goodbye"

5. AFTER LOGIN IN WITH USERNAME/GUEST
   - Enter Short Code
   - INPUT: "sto" to store account credentials 
   - OUTPUT: "Enter account details for storage in the VAULT" 
   - INPUT: "Instagram" "shee_annie" "123"
   - OUTPUT: "Instagram, shee_annie, 123"
   - ERROR: displays error incase of error
   - Enter Short Code
   - INPUT: "dis" to display account credentials 
   - OUTPUT: "Below are all your saved credentials" 
   - OUTPUT: "Instagram, shee_annie, 123"
   - ERROR: "No credentials available"


## Development

Want to contribute? Great!

To fix a bug or enhance an existing module, follow these steps:
- Fork the repo
- Create a new branch (git checkout -b improve-feature)
- Make the appropriate changes in the files
- Add changes to reflect the changes made
- Commit your changes (git commit -am 'Improve feature')
- Push to the branch (git push origin improve-feature)
- Create a Pull Request


## Known Bugs

If you find a bug (the website couldn't handle the query and or gave undesired results), kindly open an issue here by including your search query and the expected result.

If you'd like to request a new function, feel free to do so by opening an issue here. Please include sample queries and their corresponding results.

### License

*MIT*
Copyright (c) 2022 **Ann Wanjiku**

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.