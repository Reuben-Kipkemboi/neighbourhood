# Neighbourhood

#### By Reuben Kipkemboi

## Table of Content

+ [Description](#description)
+ [Installation Requirement](#installation-requirements)
+ [Technology Used](#technologies-used)
+ [License](#license)
+ [Authors Info](#authors-info)

## Description
You really don’t know what is happening in your neighborhood most of the time. What if an important meeting happens, theft or even death wouldn’t you like to know about it.
This is a Web application that allows you to be in the loop about everything happening in your neighborhood. From contact information of different handyman to meeting announcements or even alerts.

[Go Back to the top](#neighbourhood)


## User Stories

User Can :-

* Sign in with the application to start using.
* Set up a profile about me and a general location and my neighborhood name.
* Find a list of different businesses in my neighborhood.
* Find Contact Information for the health department and Police authorities near my neighborhood.
* Create Posts that will be visible to everyone in my neighborhood.
* Change My neighborhood when I decide to move out.
Only view details of a single neighborhood.

[Go Back to the top](#neighbourhood)

Registration

![Registration](./app/static/images/register.png)

Login

![Login](./app/static/images/login.png)


Home Module

![News Highlights](./app/static/images/home.png)

Our Neighbourhoods

![Neighbourhoods](./app/static/images/hoods.png)


Create a Neighbourhood

![business](./app/static/images/create.png)


Create New Business in your Neighbourhood

![create Business ](./app/static/images/api.png)

Create a Post/Alert

![create Post ](./app/static/images/post.png)


## Behaviour Driven Development
| Behaviour | Input | Output |
| ---------------- | --------------- | ------------------ |
| Application starts | **On page load** | Login page for user to login |
| Registration| **Registration page** | The registration page has a register form for new users  to register to the application and are redirected to login |
| Button click | **View More click** | Upon clicking neighbourhoods navigation User can see a the available homesteads and on click of `view more` button user can see the details of a single  neighbourhood|
| Button click | **Join or Leave button** | one can decide to join a neighbourhood and also leave the neighbourhood.To leave you click on leave button and to join Join button.One can only be a member of one neighbourhood at a time|
| Profile Icon | **Profile Icon click** | User gets option to view profile, update profile and logout.On view profile user can view and also edit his or her own profile.The logout button basically ends the users session|
| Forms | **Form filling** | User gets to fill in various forms, and depending on various tasks the form are meant for, upon submission the act is done e.g for profile update on form submission users profile is updated|


## Installation Requirements

### Prerequisites

- Django
- Pip & Python
- cloudinary 
- Postgres Database
- Gunicorn

## Instructions
   
##### Clone Repository:  
 ```bash 
https://github.com/Reuben-Kipkemboi/neighbourhood.git 
```
##### Install and activate Virtual Environment virtual  
 ```bash 
cd <projectname> && python3 -m venv virtual && source virtual/bin/activate 
```  
##### Install Dependencies  
 ```bash 
 pip install -r requirements.txt 
```  
##### Setup Database  
  SetUp Database User,Password, Host then following Command  

 ```bash 
python manage.py makemigrations  
 ``` 
 Now Migrate

 ```bash 
 python manage.py migrate 
```
##### Run Application  
 ```bash 
 python3 manage.py runserver 

 or
 ./manage.py runserver
```
##### Test Application  
 ```bash 
 python manage.py test <appname>
```
Open the application on your browser `127.0.0.1:8000`.  

[Go Back to the top](#neighbourhood)


## Technologies Used

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/bootstrap-%23563D7C.svg?style=for-the-badge&logo=bootstrap&logoColor=white)
![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)

## License
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[MIT License](LICENSE)

## Live Site

<!-- #### https://linda-jirani.herokuapp.com/ -->


## Author's Info

 :email: [Reuben Kipkemboi](https://gmail.com)  

<p align = "center">
    &copy; 2023 @Reuben Kipkemboi.
</p>
