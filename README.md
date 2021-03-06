# pitch-perfect :see_no_evil: :hear_no_evil: :speak_no_evil:
One Time Pad Implementation with a GUI

## Features
* Provides a minimal email client
* Encrypts messages with OTP and PGP
* Uses 1024-byte long keys for OTP
* Uses RSA with size 4096 for PGP

## Installation
    $ git clone https://github.com/f34rl00/pitch-perfect.git
    $ cd pitch-perfect
    $ pip install -r requirements.txt
    
## Usage
    $ python qt_app.py
  This will start the application and run the setup wizard for the first time.  
### **Note:** This program is not intended to be used as an email client, therefore **creating a new email account is recommended.**
 
## Screenshots
<img src="https://github.com/f34rl00/pitch-perfect/blob/master/screenshots/image1.png" width="640">

## Documentation
Nothing much :/

## TO-DO List
- [ ] Other mailbox fuctions  
- [x] Write email server settings in config file
- [x] Email text length limit for otp encryption
- [ ] Menubar not visible on mac os
- [ ] Google application password needed for login
- [x] Json for otp keys
- [x] Program update function
- [x] Email drop down recommendations in to: section while writing an email
- [x] Automatically add addresses from an email to contacts
- [ ] Send pgp public key within the app
- [ ] Read receipts

### Have you seen the movie?
No, I haven't.
