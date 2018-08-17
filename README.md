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



## To deploy

1. First, clone the Dublin_Bus_Project repo from GitHub
2. To recreate our database, create an empty database called dublinBus, then run the SQL commands in the database.sql file in the config directory to create the tables
3. Then cd into the /config directory. Type the following into the command line

`sudo service forecast.service start`

`sudo service weatherapi.service start`

`sudo service current_schedule.timer start`

4. Then, in the same directory, enter the following command


`sudo service bus_extract.service start`


​	This will take a significant amount of time. The bus_extract.service runs the job master.sh script, which in turn runs the extract_bus_line.sh 		script, which extracts each bus line. 


4.  Then cd into the /datanalytics/prediction_model directory and enter into the command line:

   `python run.py` 

   This will create a Neural Network pickl files for each line. 

5. To start the application, cd into backend folder and enter the following at the command line 

   `python manage.py runserver`

6. Naturally, users will have to insert their own api keys, passwords for database access (eg in the dbconnect.py file in the weatherapi directory), etc in order to run the web app


