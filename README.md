## Dublin Bus Project 

Dublin Bus Project is a web application that estimates journey times for trips on the Dublin Bus network using predictive data analytics. It was created as part of the research practicum for UCD MSc in Computer Science during the summer of 2018 by Chen Yiming, Thomas Anderson, Rosanna Hanly and Sheena Davitt.

### *What it does*

It allows the user to enter details of a Dublin Bus route (or subsection of route) and a date and time; the web app will then estimate the journey time and display it on the user interface. 

It is currently hosted at www.dublinroute.com

### *Folder structure*

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



## Deploying the application from Github

### Clone the application from Github

First, clone the Dublin_Bus_Project repo from GitHub

### Install environment requirements

1. Install anaconda

2. Create your environment with conda. For example `conda create --name myenv`

3. Activate the newly created environment: `source activate myenv`

4. Install requirements.txt using pip. For example `pip install -r requirements.txt`

### Setup the database

1. Create an empty relational database called dublinBus
2. Run the SQL commands in the /config/database.sql file to create the tables

### Setup the database

Start the following backend services:

`systemctl forecast.service start`
- Obtains the 5 day weather forecast and puts it in the database

`systemctl weatherapi.service start`
- Obtains the current weather and puts it in the datase

`systemctl current_schedule.timer start`
- Starts a SystemD timer so that a new GTFS schedule will be downloaded and uploaded to the database on a weekly basis


### Prediction model


`systemctl bus_extract.service start`


​	This will take a significant amount of time. The bus_extract.service runs the job master.sh script, which in turn runs the extract_bus_line.sh 		script, which extracts each bus line. 


4.  Then cd into the /datanalytics/prediction_model directory and enter into the command line:

   `python run.py` 

   This will create a Neural Network pickl files for each line. 

6. Naturally, users will have to insert their own api keys, passwords for database access (eg in the dbconnect.py file in the weatherapi directory), etc in order to run the web app

## Starting the web-server
To start serving the application, the Nginx and uWSGI servers needs to be started

1. Enter the command:

   `systemctl nginx start`
   
2. From the /backend folder, enter the command:
    `uwsgi uwsgi.ini`


