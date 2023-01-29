## Inspiration
Ensure loved ones, including the elderly and small children, are protected without cameras or other intrusive features.  Inspired by the door flags found in apartment buildings, this low-cost tool additionally encapsulates environment and wellness data.

## What it does
This tool collects data on the room environment - light, temperature, humidity, and sound, to help monitor individuals living alone without the need for a camera.  Personal wellbeing is tracked through simple buttons, to form an interface easy for the elderly and/or small children.

## How we built it
An Arduino collects environment data and sends the communication serially to a Raspberry Pi, mounted on the back of a 7'' display.  A web server and simple interface which uses Flask, Python, HTML, and CSS was developed on the Raspberry Pi.  Live data is gathered from the Arduino and displayed on the webpage, along with wellness buttons and a few photos of the user's favorite memories.

## Challenges we ran into
Establishing communication between the Raspberry Pi and Arduino, and cleaning the data for display on the webpage. 

## Accomplishments that we're proud of
Building a simple interface which is easily navigated by all individuals, and gathering live environment data.  Utilizing and connecting non-traditional products.

## What we learned
During this first hackathon project, learning the process of determining where errors were originating, as well as using Serial communication and the Raspberry Pi and Arduino hardware for the first time.

## What's next for Safe + Sound
Potential extensions of this project include collecting historical data on the environment and wellbeing of the individual to determine inconsistencies in the data - for instance, tracking the average light patterns/levels and noticing a period of time with no lights turned on could represent the individual has fallen or may need to be assisted.  In addition, the product may send live updates to family members or friends when odd patterns or updates are detected.
