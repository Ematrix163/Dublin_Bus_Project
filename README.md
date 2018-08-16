## About Dublin Bus Project 

Dublin Bus Project is a web application that estimates journey times for trips on the Dublin Bus network using predictive data analytics. It was created as part of the research practicum for UCD MSc in Computer Science during the summer of 2018 by Chen Yiming, Thomas Anderson, Rosanna Hanly and Sheena Davitt.

### *What it does*

It allows the user to enter details of a Dublin Bus route (or subsection of route) and a date and time; the web app will then estimate the journey time and display it on the user interface. 

It is currently hosted at www.dublinroute.com

### *Folders*

The repository consists of the following folders:

*Backend*: The python code that returns journey time estimates, interacts with our database, allows us to create user logins, etc. Diagram below.

-backend

```
├── api
├── backend
├── core
├── manage.py
├── requirements.txt
├── static
├── templates
└── uwsgi.ini
```





*Config*: Service files that allow a number of processes to continue in the background (eg continually updating weather data, etc)

*Data Analytics*: All code and jupyter notebooks related to the model creation stage of our project, including data cleaning notebooks, model training, bus line extraction scripts etc.

*Frontend*: 

All javascript files used to create the user interface. Built using React javascript framework. Diagram below.

-frontend

```
├── public
└── src
    ├── App.js
    ├── App.test.js
    ├── css
    ├── fonts
    ├── image
    │   └── weather
    ├── index.js
    ├── Login.js
    ├── Map.js
    ├── MyFav.js
    ├── ShowRoute.js
    ├── ShowStationResult.js
    ├── SideBar.js
    ├── SignUp.js
    ├── StandaloneSearchBox.js
    ├── Term.js
    ├── TwitterDisplay.js
    └── WebAPI.js

```



*Tests*: Unit test files

*Weatherapi*: Python scripts that collect current weather and weather forecast data and write them to our database







