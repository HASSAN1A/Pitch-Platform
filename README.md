# PITCH-Platform
### 18.09.2020
####  A Python Flask CRUD web application for sharing pitch ideas

![alt text](app.png)

## Author
[Dennis Kamunya](https://github.com/D-Kamunya)

## Versioning
pitch-platformk V1.0

## Description
In life, you only have 60 seconds to impress someone. 1 minute can make or break you.
Pitch Platform is a flask web application which helps its users to pitch ideas based on different categories.The users also get the opportunity to view other users pitches,vote on them and also leave a comment 
The link to the live site is https://pitch-platform-101.herokuapp.com/

## User Story
* User can see the pitches other people have posted.
* User can vote on the pitch they liked and give it a downvote or upvote.
* User can signed in the app to leave a pitch comment
* User will receive a welcoming email once they sign up.
* User can view the pitches they have created in their profile page.
* User can comment on the different pitches and leave feedback.
* User can submit a pitch in any category.
* User can view different pitches by categories.

## Technologies Used
* Python 3.8
* Flask 
* PostgreSQL
* SQLAlchemy
* HTML  
* CSS
* JS
* MDB 4
    * Bootstrap 4
    * Font Awesome 
    * jQuery 3
* Google Font API

## Requirements
* This program requires python3.+ (and pip) installed, a guide on how to install python on various platforms can be found [here](https://www.python.org/)


## Installation and Set-up
Here is a run through of how to set up the application:
* **Step 1** : Clone this repository using **`https://github.com/D-Kamunya/pitch-platform.git`**, or downloading a ZIP file of the code.
* **Step 2** : The repository, if downloaded as a .zip file will need to be extracted to your preferred location and opened
* **Step 3** : Go to the project root directory and  create a virtual environment. Run the following commands respectively:
    * **`python3.8 -m venv --without-pip virtual`**
    * **`source virtual/bin/activate`**
        * Note that you can exit the virtual environment by running the command **`deactivate`**
* **Step 4** :  Download the latest version of pip in virtual our environment.   
    * **`curl https://bootstrap.pypa.io/get-pip.py | python`**  

* **Step 5** : Download the all dependencies in the requirements.txt using **`pip install -r requirements.txt`**
    * Create a file in your root directory called start.sh and store a generated SECRET key,MAIL_USERNAME AND MAIL_PASSWORD like so **`export SECRET_KEY="<your-key>"`**
    **`export MAIL_USERNAME="<your-key>"`**
    **`export MAIL_PASSWORD="<your-key>"`**
    * On the same file write down the command **`python3 manage.py server`** 
* **Step 6** : Go to config.py and set the SQLALCHEMY_DATABASE_URI to your own, you may use Postgres or any other SQL databse client.    
* **Step 7** : On your terminal, run the following command, **`chmod a+x start.sh`**
    * You can now launch the application locally by running the command **`./start.sh`** 
    * Open your preferred browser and view the app by opening the link **http://127.0.0.1:5000/**.

## Known Bugs
* No known bugs
Be sure to report more bugs by contacting me.

## Contribution
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
## Support and contact details
If you run into any problems feel free to contact me @dennismuriithik@gmail.com

#### License
[![license](https://img.shields.io/github/license/DAVFoundation/captain-n3m0.svg?style=flat-square)](https://github.com/DAVFoundation/captain-n3m0/blob/master/LICENSE)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Copyright (c) 2020 Dennis Kamunya
