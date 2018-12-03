# Description
A voting bot written in python 3.x for strawpoll. 
It can work on Windows, Linux and Mac as long as python is installed.

### Features
- Easy to use command line driven program
- Ability to choose from any type of strawpoll domain
- Ability to remember which proxies have already been used
- Ability to regenerate proxies automatically

# Usage
Change the following options in the python file:
v (whether or not the script prints everything)
t (the link of the poll)
o (the option that is to be voted for) 

Run the program:
```
python StrawPollBreaker.py

```


# How to install it ?
You can either download the zip or clone it with git then install the required library if it not install yet in your operating system with:
```
pip install requests

```


# How do I get the survey id and the target ?
The survey id is always the url pointing to the desired survey.

To find the desired target the user must right click the checkbox you want to vote for, then go to inspect element and search for the "value" option. 