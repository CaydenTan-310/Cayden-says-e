# Cayden's chatbot

## Description
Math chatbot that provides formulae for students.

## Guide to Running
Note: replace all ```pip3``` with ```pip``` wherever necessary.  
### Setting Up
First, ensure that you have virtualenv installed on your system.  
```$ pip3 install virtualenv```  
```$ pip install virtualenvwrapper-win``` *[windows only]*

Next, set up the virtual environement, and activate it
```$ virtualenv venv```  
```$ source venv/bin/activate```  

Install requirements
```$ pip3 install -r requirements.txt```

### Running 
You could either:  

#### Use Python3 to run app.py
```$ python3 app.py```

#### Use flask to run the app (Unix Bash for Linux, Mac, etc.)
```$ export FLASK_APP=app.py``` *[only needs to be done once]*  
```$ flask run```

#### Use flask to run the app (Windows CMD)
```> set FLASK_APP=app.py``` *[only needs to be done once]*  
```> flask run```

#### Use flask to run the app (Windoes Powershell)
```> $env:FLASK_APP = "hello"``` *[only needs to be done once]*  
```> flask run```

### Ending
Close the flask process by pressing ^C (contol C)
```$ deactivate``` to end the virtualenv

## Sources
[https://flask.palletsprojects.com/en/1.1.x/cli/](https://flask.palletsprojects.com/en/1.1.x/cli/)