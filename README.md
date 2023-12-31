# Human Robot Collaboration Using Natural Language Interface

Project Description

This project aims to facilitate human-robot collaboration through a natural language interface. The fundamental idea is to empower users to guide and instruct the robot in real-time, diverting it from its pre-trained tasks. This allows the robot to perform new tasks and respond accurately to specific directions. The project utilizes a Jetbot that is trained on certain tasks, including basic movements, object avoidance and color-based object recognition. The robot possesses the ability to communicate verbally.

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
![diag](https://github.com/mimran980/jetbot/assets/112286488/8e6c56f6-c0a9-4b74-9599-72f73d2bcb4e)


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



