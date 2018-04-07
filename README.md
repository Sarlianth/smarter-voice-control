# Smarter-voice-control


This repository is for our Gesture Based UI project in 4th year software development in Galway-Mayo Institute of Technology. The purpose of the project is to create an application using the Smarter coffee machine and Cortana in order to brew coffee using voice commands.


## Project Requirements
Develop an application that is controlled by natural means - Voice, Hand Gestures etc.


* Minimum Requirement is to develop an application that is run locally.
* Teams of two or three people.
* Any Platform and Programming Language permitted.


## Introduction
In our second semester of our final year of Software Development we received a brief to create a Gesture based project using any language and any platform that will use human gestures or voice in order to operate. Upon hearing these requirements we teamed up in a group of three and decided to do something with Voice activation using Cortana. 


One of us had a smarter coffee machine and since we are all programmers and we all love coffee we decided to implement coffee brewing and voice activation. The idea was that when programming we don't want to stand up, brew coffee and wait for it to make, so in order to avoid the time-wasting we decided that we will be able to just speak and have the coffee made for us and this will allow for us to continue working and have coffee made for us while coding and when the coffee is made we can just go and get it without waiting for the coffee to be brewed.


The Application uses:


* a C# UWP application - That creates a back-end application that creates custom Cortana commands to be used when used the key-word “Coffee” that enables the commands in Cortana as well as creating a User Friendly Application that allows the user to speak to Cortana and start coffee brewing.

* Http creates the connection between the 2 technologies which allows us to call out python script using a flask API to handle the routes and logic appropriateluy. A http request is fired off from the UWP after making a verbal request to Cortana, this http request hits a url which has been exposed by our RESTful api, which then figures which using its routes will then handle the request, and fire off another to the Smarter Coffee Machine, thus allowing us to brew a lovely pot of Java from the comfort of our desk... Now all we need is a robot to bring it to us...

* Python - We used a python script that connects to the coffee machine and allows us to do our own application that will allow for our own custom commands to be used.




## Contributors:
[Adrian Sypos](https://github.com/sarlianth)


[Daniel Verdejo](https://github.com/verdagio)


[Robert Kiliszewski](https://github.com/robertkiliszewski)


## Lecturer
[Damien Costello](https://github.com/arkiq)


## About Technologies


### Cortana


Cortana is Microsofts Visual Assistant created for Windows 10, Windows 10 Mobile, Windows Phone 8.1, Invoke smart speaker, Microsoft Band, Xbox One, iOS, Android, Windows Mixed Reality, and Amazon Alexa. Cortana can be used in many different languages such as English, Portuguese, French, German, Italian, Spanish, Chinese, and Japanese.


### Smarter Coffee Machine 
The Smarter Coffee Machine is a coffee machine developed to brew coffee by either using your phone or by just using the coffee machine itself. It allows you to choose the strength of your coffee to your liking, you can choose the amount of cups to be brewed, it brews fresh coffee using fresh coffee beans.


### C#
Is a multi-purpose programming language developed by Microsoft. The purpose of the programming language is to create Common Language Infrastructure (CLI) so that it allows multiple high-level languages to be used on different computer platforms without having to be re-written.


### Python
Python is a high-level programming language for general-purpose programming. Python does not use semi-colons, instead it used white space indentation as its formatting. Python can be used on many operating systems and allows for endless implementations.

### Flask
Flask is a framework for building RESTful api's via python.

## Voice Activation


Since the application is supposed to used a gesture based, we decided to go with voice activation since it's the easiest ways of doing something : speaking. The idea came from just simply speaking to Cortana in order to brew coffee which makes it simple to use and takes no effort from the user to do.


In order to involve Cortana in the project we created simple to use commands that will allow her to recognize the prefix that allows the usage of custom-made commands.


## Development Process


While developing the application we did a step by step process:
* Connect to the coffee machine using Python
* Create Custom Commands using C#
* Connecting the two in order to make a working application


While making the application we were able to connect to the coffee machine using Python without any problems, we were able to get the IP address of the coffee machine and were able to connect to it.


When developing the custom Cortana commands we were able to create them using C# but we were unable to use them when talking to Cortana while testing on multiple machines. We were unable to see the problem in our code so we decided to speak to our lecturer and do extended research as to why it may not work. Once our lecturer has tested our commands and tried running it on his local machine he has told us that there is a bug in the latest release of Cortana which only makes Cortana do web search when asking her to do something. Upon more research we have found out that it's not only us that have this problem, we viewed on the [Microsoft official page](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_cortana-winpc/cortana-only-providing-web-search-answers-since/2afe3c97-f578-4c58-b7d9-8b6768d453c4) that other developers have this problem since the release of the Creators Update which apparently makes Cortana only do Web Search which put us in a tight spot as Cortana was our only option.


Upon further inspection and contacting our lecturer we came to the conclusion that this bug is out of our control and that the code we have provided worked as intended and our only option was to develop the application as intended and not to worry about the bug since it was not our fault it wasn't working so we continued to develop the application but this time instead of using Cortana as the main Technology that the application will be based on we will instead create a GUI for the user with buttons in it that the user can click and basically these buttons are a replacement for the voice commands since Cortana can't recognize them.

These buttons will allow the user to basically brew coffee the same way as if they were speaking to Cortana.

## Architecture for the solution

### Front-End

* GUI - The Graphical User Interface is a simple desktop Application that has three buttons that allow the user to either brew coffee, Reset the machine to it's base options or turn it off. These buttons impplement commands for the Smarter Coffee Machine instead of implementing the Custom Cortana Commands since there is a problem with the latest update.

### Back-End
* Script.py - This Python script is our API to connect to the coffee machine by using it's IP address and being able to operate it without physically touching it. By using this script we are able to control the amount of cups that we want to brew without touching the coffee machine.

* CustomCortanaCommands - This was used in the beginning in order to create custom Cortana commands to be used vocally in order to brew coffee but since we have ran into the problem with Cortana this is no longer used in the final solution of the project.

## Conclusion and Recommendations
