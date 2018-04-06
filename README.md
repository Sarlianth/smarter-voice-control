# Smarter-voice-control

This repository is for our Gesture Based UI project in 4th year software development in Galway-Mayo Institute  of Technology. The purpose of the project is to create an application using the Smarter coffee machine and Cortana in order to brew coffee using voice commands.

## Project Requirements
Develop an application that is controlled by natural means - Voice, Hand Gestures etc.

* Minimum Requierement is to develop an application that is ran locally.
* Teams of two or three people.
* Any Platform and Programming Language permitted.

## Introduction
In our second semester of our final year of Software Developemnt we received a brief to create a Gesture based project using any language and any platform that will use human gestures or voice in order to operate. Upon hearing these requirements we teamed up in a group of three and decided to do something with Voice activation using Cortana. 

One of us had a smarter coffee machine and since we are all programmers and we all love coffee we decided to implement coffee brewing and voice activation. The idea was that when programming we don't want to stand up, brew coffee and wait for it to make, so in order to avoid the time wasting we decided that we will be able to just speak and have the coffee made for us and this will alow for us to continue working and have coffee made for us while coding and when the coffee is made we can just go and get it without waiting for the coffee to be brewed.

The Application uses:

* a C# UWP application - That creates a back-end application that creates custom Cortana commands to be used when used the key-word "Coffee" that enables the commands in Cortana as well as creating a User Friendly Application that allows the user to speak to Cortana and start coffee brewing.
* Python - We used a python script that connects to the coffee machine and allows us to do our own application that will allow for our own custom commands to be used.


## Contributors:
[Adrian Sypos](https://github.com/sarlianth)

[Daniel Verdagio](https://github.com/verdagio)

[Robert Kiliszewski](https://github.com/robertkiliszewski)

## Lecturer
[Damien Costello](https://github.com/arkiq)

## About Technologies

### Cortana

Cortana is Microsofts Visual Assistant created for Windows 10, Windows 10 Mobile, Windows Phone 8.1, Invoke smart speaker, Microsoft Band, Xbox One, iOS, Android, Windows Mixed Reality, and Amazon Alexa. Cortana can be used in many different languages such as English, Portuguese, French, German, Italian, Spanish, Chinese, and Japanese.

### Smarter Coffee Machine 
The Smarter Coffee Machine is a coffee machine developed to brew coffee by either using your phone or by just using the coffee machine itself. It allows you to choose the strenght of your coffee to your liking, you can choose the amount of cups to be brewed, it brews fresh coffee using fresh coffee beans.

### C#
Is a multi-purpose programming language developed by Microsoft. The purpose of the programming language is to create Common Language Infrastructure (CLI) so that it allows multiple high-level languages to be used on different computer platforms without having to be re-written.

### Python
Python is a high-level programming language for general-purpose programming. Python does not use semi-colons, instead it used white space indentation as its formatting. Python can be used on many operating systems and allows for endless implementations.

## Voice Activation

Since the application is supposed to used a gesture based, we decided to go with voice activation since its the easiest ways of doing something : speaking. The idea came from just simply speaking to Cortana in order to brew coffee which makes it simple to use and takes no effort from the user to do.

In order to involve Cortana in the project we created simple to use commands that will allow her to recognize the prefix that allows the usage of custom made commands.

## Development Process

While developing the application we did a step by step process:
* Connect to the coffee machine using Python
* Create Custom Commands using C#
* Connecting the two in order to make a working application

While making the application we were able to connect to the coffee machine using Python without any problems, we were able to get the IP address of the coffee machine and were able to connect to it.

When developing the custom Cortana commands we were able to create them using C# but we were unable to use them when talking to Cortana while testing on multiple machines. We were unable to see the problem in our code so we decided to speak to our lecturer and do extended research as to why it may not work. Once our lecturer has tested our commands and tried running it on his local machine he has told us that there is a bug in the latest release of Cortana which only makes Cortana do web search when asking her to do something. Upon more research we have found out that it's not only us that have this problem, we viewd on the [Microsoft official page](https://answers.microsoft.com/en-us/windows/forum/windows_10-win_cortana-winpc/cortana-only-providing-web-search-answers-since/2afe3c97-f578-4c58-b7d9-8b6768d453c4) that other developers have this problem since the release of the Creators Update which apparently makes Cortana only do Web Search which put us in a tight spot as Cortana was our only option.

Upon further inspection and contacting our lecturer we came to the conclusion that this bug is out of our control and that the code we have provided worked as intended and our only option was to develop the application as intended and not worry about the bug since it was not our fault it wasn't working so we continued to develop the application with the idea that this is how it will work if the bug didn't exist in the new update. Basically the application is created as it is supposed to work but due to Cortana being faulty it isn't capable of using our commands, but if it were to work properly, Cortana would be able to brew coffee when asked to without any problems.


