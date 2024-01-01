# Raspberry Pi Security Lock System

## Project Overview

This project involves creating a security lock system using a Raspberry Pi 4 and various peripherals, including a 12V solenoid door lock, IR sensor, Raspberry Pi camera module, RFID scanner, and more. The system employs facial recognition and RFID technology to grant access to authorized personnel while logging unrecognized faces on a Flask website.

## Project Components

- Raspberry Pi 4 Model B (8GB)
- 12V solenoid door lock
- 12V relay
- IR sensor
- Raspberry Pi camera module v3
- RFID scanner
- Battery pack for solenoid
- USB battery pack for Raspberry Pi
- SD card
- Micro HDMI cable

## Project Steps

1. **Set Up the Raspberry Pi:**
   - Connect the Raspberry Pi camera module and configure it to work with OpenCV.
   - Set up the IR sensor to detect the presence of a user.

2. **Face Recognition with OpenCV:**
   - Implement face recognition using OpenCV. Train the system with images of allowed persons and create a face recognition model.

3. **Face Recognition and Door Unlocking:**
   - Integrate the face recognition script with the door lock system.
   - When a recognized face is detected, log the successful attempt and unlock the door by sending a signal to the relay.

4. **Master Override with RFID Scanner:**
   - Connect the RFID scanner to the Raspberry Pi.
   - Implement a script that reads RFID cards and compares the scanned RFID against a master list.
   - If the master RFID is detected, log the successful attempt and open the door by activating the solenoid.

5. **Logging Denied Attempts with Images:**
   - Modify the face recognition and RFID scripts to capture an image when an access attempt is denied.
   - Save the captured image along with other relevant information to a file or database.

6. **Scheduled Deletion of Old Logs:**
   - Implement a scheduled task to delete older log entries, ensuring efficient use of storage.

7. **Flask Web Application:**
   - Install Flask on the Raspberry Pi.
   - Create a Flask web application that displays a list of previous access attempts, including details such as timestamp, type of attempt, and associated images.

8. **Serve Static Images with Flask:**
   - Create a folder named `static` for storing access attempt images.
   - Modify the Flask app script to include the `static` folder.

9. **Run the Flask App:**
   - Execute your Flask app script on the Raspberry Pi.
   - Access the website from your computer's web browser by navigating to `http://<raspberry_pi_ip>:5000`.

10. **Power Management:**
    - Ensure stable power sources for both the Raspberry Pi and the solenoid.

11. **Testing and Calibration:**
    - Test each component individually and calibrate the face recognition system and RFID scanner.

12. **Security Measures:**
    - Implement additional security measures, such as encryption for stored face data and secure handling of log information.

## TODO

- **Upload Training Data Through WiFi:**
   - Implement a feature to upload training data for face recognition from devices connected to the same WiFi network through the flask website.

- **RFID Override:**
   - Incorporate an RFID override functionality, allowing authorized personnel to use RFID cards for immediate door access.
    
 - **user Authentication:**
   - Require user to login when accessing the flask website.
     
## Acknowledgments
Huge thank you to these people for their extremely helpful resources
- [Instructables - Raspberry Pi Launch Python script on startup](https://www.instructables.com/Raspberry-Pi-Launch-Python-script-on-startup/)
- [GitHub - OpenCV Face Recognition for Raspberry Pi](https://github.com/justsaumit/opencv-face-recognition-rpi4)
- [Peppe8o - Beginner's Guide to Install a Flask Python Web Server on Raspberry Pi](https://peppe8o.com/beginners-guide-to-install-a-flask-python-web-server-on-raspberry-pi/)



