# Human Robot Collaboration Using Natural Language Interface

Jetbot
Project Description

This repository hosts a project that focuses on enabling human-robot collaboration through a natural language interface. The core concept is to create a user-friendly interaction between a robot and a human using voice commands and responses. The project employs a Jetbot, which has been trained to perform various tasks, including basic movements and object recognition based on color. The robot is capable of processing voice commands, understanding them, and responding verbally to carry out the requested actions.
Features

    Voice Interaction: Users can communicate with the Jetbot using natural language voice commands.
    Task Execution: The robot is trained to perform tasks such as movement and object picking based on color.
    Voice-to-Text Conversion: The Whisper library is used to capture user voice through the microphone and convert it into text.
    Text-to-Speech Conversion: The GTTS (Google Text-to-Speech) library is utilized to enable the robot to respond to the user's commands by speaking.
    Microphone and Speaker Integration: The project includes microphone and speaker components to facilitate voice-based interaction.

Technologies Used

    Jetbot: The hardware platform for the robot.
    ChatGPT API: Used for converting natural language text into robotic language.
    Whisper Library: Employed to capture user voice from the microphone and convert it into text.
    GTTS (Google Text-to-Speech) Library: Used for enabling the robot to respond verbally.
    Microphone and Speaker: Hardware components integrated into the Jetbot for voice interaction.

High Level Architecture Diagram:
![ros](https://github.com/mimran980/jetbot/assets/112286488/ccce4700-7163-4011-8f56-a881b0b49323)


Technical Architecture

![image](https://github.com/mimran980/jetbot/assets/112286488/e53569a0-fe21-48b2-b495-8a1a740c2c34)

Road Following Demo:
Here is a short demo of its trained task where it needs to follow a road.

https://github.com/mimran980/jetbot/assets/112286488/e60992ab-a97e-40ef-8cea-7aac16a587b4


Acknowledgments

This project was made possible by the contributions of the open-source community and the following libraries:

    ChatGPT API
    Jetbot
    Whisper Library
    GTTS (Google Text-to-Speech) Library

For any questions or inquiries about the project, please feel free to reach out to Imran Muhammad using mi3dr@umsystem.edu



