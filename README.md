<div id="top"></div>

<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->

[![oc][oc-project-shield]][oc-project-url]
[![django][django-shield]][django-url]
[![crud][crud-shield]][crud-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">

<h1 align="center">OC - PROJECT N°9 - Web Application Using Django Framework</h1>

  <p align="center">
   LITReview is a django web application allowing users to create or asked for books reviews.
    <br />
    </p>
</div>

<img src="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80">
<a href="https://images.unsplash.com/photo-1524995997946-a1c2e315a42f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=1470&q=80"><small>By Susan Q Yin</small></a>





<!-- ABOUT THE PROJECT -->
## About The Project

### Authentication
![Authentication](static/assets/oc_project_9_authentication.gif)


### CRUD
#### Create a Ticket
![Create Ticket](static/assets/oc_project_9_create.gif)
#### Create a Review
![Create Review](static/assets/oc_project_9_create_review.gif)
#### Update a post
![Update Post](static/assets/oc_project_9_update.gif)
#### Delete a post
![Update Post](static/assets/oc_project_9_delete.gif)


### Followers
![Followers](static/assets/oc_project_9_followers.gif)

<p align="right">(<a href="#top">back to top</a>)</p>



### Built With

* HTML
* CSS & SASS
* Python - Django Framework

<p align="right">(<a href="#top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

### Installation & Running the script

1. Clone the repo
   ```sh
   git clone https://github.com/Jliezed/oc_project_9_litreview.git
   ```

#### Create and activate a virtual environment
2. Go to your project directory
   ```sh
   cd oc_project_9_litreview
   ```
3. Install venv library (if not yet in your computer)
   ```sh
   pip install venv
   ```
4. Create a virtual environment
   ```sh
   python -m venv env
   ```
5. Activate the virtual environment
   ```sh
   source env/bin/activate
   ```
#### Install packages
6. Install the packages using requirements.txt
   ```sh
   pip install -r requirements.txt
   ```
#### Set environment variables
7. Create a copy of the file ".env.default" and rename it ".env"
8. Set value to the .env file:
   1. Define a secret key
   2. Debug to True for local development or False for production
   3. Allowed host equal to 127.0.0.1 for local environment

      ```sh
      SECRET_KEY='YOUR SECRET KEY'
      DEBUG=True
      ALLOWED_HOSTS=['127.0.0.1']
      ```

#### Run the server
9. Access to the app: http://127.0.0.1:8000/accounts/login/
   ```sh
   python manage.py runserver
   ```
10. Access to the Admin: http://127.0.0.1:8000/admin/login/?next=/admin/
   ```sh
   User: toto
   Password: secret
   ```
---


<p align="right">(<a href="#top">back to top</a>)</p>










<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[oc-project-shield]: https://img.shields.io/badge/OPENCLASSROOMS-PROJECT-blueviolet?style=for-the-badge
[oc-project-url]: https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python

[django-shield]: https://img.shields.io/badge/Django-blue?style=for-the-badge
[django-url]: https://www.djangoproject.com/

[crud-shield]: https://img.shields.io/badge/-CRUD-blue?style=for-the-badge
[crud-url]: https://en.wikipedia.org/wiki/Create,_read,_update_and_delete

