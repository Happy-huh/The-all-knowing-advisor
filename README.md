# ALL KNOWING ADVISOR
## A CHAT BOT:
### DESCRIPTION:
This program was created by Onyedika Stephen Akujieze, as the last project to his cs50P introduction to programing with python. See the [video demo](https://youtu.be/rWlRo1sDj0k)
#### Design Choice:
Ever since I started programming with python I have been particularly intrested in programs that would allow me communicate or interact with my computer for example the number guessing game, rock, paper, sissors, little professor, etc. Each of them being more interactive than the last. My interest towards interactive programs and the recent rise to fame of chat GPT I then came of with the idea of The All Knowing Advisor. He was initially supposed to be a Wizard from the name "All Knowing", but a wizard has to have a wizard's voice and python dosen't have features that support that so I changed the design to an advisor instead of a wizard to make the best use of my available resourses. The design is very simple and does not have in it so many libaries or code lines it is optimized for readability and workability.
## Libaries Used:
The All Knowing Advisor comes with two major features namely wolframalpha which handles almost all questions like what is your name, how old are you, 3 mutiplied by 5 etc. And Wikipedia which answers all questions that cannot be answered by the wolframalpha libary like who was the first president of the united state. It also other features that will be discussed below.
**wolframalpha**
This is a libary which can give expert-level answers using wolfram's algorithms, knowledge and AI technologies. It can answer questions like what is your name, how old are you, 3 mutiplied by 5 etc. To start using wolframalpha libary firstly, you have to install it by typing
```python
pip~install~wolframalpha
```
on your terminal. Then, sign in to the wolframalpha developers portal. After logging in, go to My Apps to start creating your first app. To obtain your ID, first sign up to get your AppID button. After a one-time survey about intended usage, the AppID creation dialog will appear. Give your application a name and a simple description to register an AppID. Each application must have it's own unique AppID. You can then use the ID in your code to connect to the api. TO know more visit the wolframalpha [Documentation](https://www.pypi.org/project/wolframalpha/)
**wikipedia**
The wikipedia libary was used in the project to allow THE ALL KNOWING ADVISOR answer all 'wh' questions like who was the first man to go to the moon, what is the largest mammal on earth etc. It also answer's this question by justing get inputs like biggest mammals, first man on the moon etc. It can also be tweaked the more per its [Documentation](https://www.pypi.org/project/wikipedia). To install wikipedia run
```python
pip~install~wikipedia
```
**pyttsx3**
pyttsx3 libary was used in this project to convert texts to sound. It is an easy to use text to speech conerter in python. It was used to read text files and also raw strings and it's .runAndWait() finction was used after every speech which can be tweaked per it's [Documentation](https://www.pypi.org/project/pyttsx3). TO install pyttsx3 run
```python
pip~install~pyttsx3
```
**time**
The time libary was used to get the exact time the entire program ran in order to calculate the bill in minutes.
## Functions:
The project consists of a main function and 6 other functions in the main python file(allknowing.py) with 5 test functions in test_allknowing.py which will be discussed below.
**main**
The main function simply calls the allknowing function and is called at the bottom of the file on the condition that it is the main file.
**allknowing**
This is where most of the functionalities of THE ALL KNOWING ADVISOR is situated. It first introduces the all knowing avdisor then promts the user for and input either to ask a question, chat, or quit. Then executes the the next portion of code depending on the input the user made or repromts the user if the user has given an invalid input.
**tts_str**
Short for text to speech string and as the name implies the function takes in one argument a string which it converts to speech says out and also prints to the terminal.
**tts_file**
Short for text to speech file. This function takes in one argument a string which is a name of a txt file. It reads the file, turns it to a speech, says it out and also prints it to the terminal if the argument entered is not a string or not a valid txt file it would raise an error.
**wolf**
This is where the wolframalpha libary is implemented it take in one argument which is a string likely to be a question it then writes that answer to 2 txt files and calls tts_file on that txt file.
**wikiped**
This is where the wikipedia libary is implemented it take in one argument a string which is to be a question it then writes that answer to 2 txt files namely answer.txt and history.txt and calls tts_file on answer.txt.
**payment_per_time**
This function calculates the total time the program ran. It takes two command line arguments start and finish which are float figures but when finish is subtracted from start it gives the ammount of time the program ran in seconds. It then converts it to minutes by dividing it by 60 then multiply it by 2 dollars to know how much the user owes.
**test_wolf**
This function test the return value of the wolf function. The wolf function returns an answer this function tests to see if the function is returning the right answer without any issues. But this test function can return an error if the request from the wolframalpha's API encounters an issue.
**test_wikiped**
This function test the return value of the wikiped function. The wikiped function returns an answer this function tests to see if the function is returning the right answer without any issues.
**test_payment_per_time**
This function test the return value of the payment_per_time function.
**test_tts_str**
This function simply tests the return value of the payment_per_time function.
**test_tts_file**
This function reads a file and stores it in a variable then calls the tts_file to read that same file and compares the return value of tts_file and the file stored in the variable. For example it reads a file called intro and stores it in a variable called x the compares x with the return value of tts_file when intro is passed as it's argument.
### TXT Files
The project consists of 4 txt files as follows.
**intriduction.txt**
This file simply contains the introductory message of the ALL KNOWING ADVISOR.
**answer.txt**
When an answer is made by either the wolf or wikiped function it is writtten in this file. It overwrites what was previously contained in the file and writes a new answer.
**history.txt**
In this file is contained all the answers that has been made and contains any new answer also.
**requirements.txt**
This file contains all the PIP installables although it does not add to the functionality of the program it is a guide for any one who intend to use the program or know more about this program.