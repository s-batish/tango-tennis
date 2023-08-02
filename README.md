# Tango Tennis
## Table of Contents
1. [UX](#ux)
    - [Project Goals](#project-goals)
    - [User Stories](#user-stories)
    - [Development Planes](#development-planes)
        - [Strategy Plane](#strategy-plane)
        - [Scope Plane](#scope-plane)
        - [Structure Plane](#structure-plane)
        - [Skeleton Plane](#skeleton-plane)
        - [Surface Plane](#surface-plane)
2. [Features](#features)
    - [Site Features](#site-features)
    - [Features Left to Implement](#features-left-to-implement)
3. [Testing](#testing)
    - [Testing Features](#testing-features)
    - [Testing User Stories](#testing-user-stories)
    - [Responsiveness](#responsiveness)
    - [Browser Compatability](#browser-compatability)
    - [Lighthouse Testing](#lighthouse-testing)
    - [Code Validation](#code-validation)
    - [Bugs](#bugs)
4. [Deployment](#deployment)
    - [Heroku Deployment](#heroku-deployment)
    - [Forking the Project](#forking-the-project)
    - [Cloning the Project](#cloning-the-project)
5. [Technologies Used](#technologies-used)
    - [Technologies](#technologies)
    - [Python Modules Used](#python-modules-used)
    - [External Python Modules](#external-python-modules)
6. [Credits](#credits)
## UX
### Project Goals
### User Stories
### Development Planes
#### Strategy Plane
#### Scope Plane
#### Structure Plane
#### Skeleton Plane
#### Surface Plane
## Features
### Site Features
### Features Left to Implement
## Testing
### Testing Features
### Testing User Stories
### Responsiveness
### Browser Compatability
### Lighthouse Testing
### Code Validation
### Bugs
## Deployment
### Heroku Deployment
- This game was deployed to Heroku. The steps to do this are as follows:
    - Create an account with [Heroku](https://id.heroku.com/login).
    - On the Heroku dashboard, click the button that says "New", then click "Create new app".
    - Choose a unique name for the app.
    - Select your region, then click "Create app".
    -  Click on the "Settings" button on the menu.
    - Scroll down to the section "Config Vars" and click "Reveal Config Vars".
    - Add the following Config Vars:
        - CLOUDINARY_URL: The URL from your Cloudinary dashboard
        - DATABASE_URL: The URL from your ElephantSQL dashboard
        - PORT: 8000
        - SECRET_KEY: Your Secret Key
    - Go to the "Deploy" button on the menu at the top.
    - Select GitHub as the deployment method and click the "Connect to GitHub" button.
    - Search for the repository "tango-tennis" and then click "Connect".
    - Scroll to the bottom of the page and either click "Enable Automatic Deploys" in the Automatic deploys section or "Deploy branch" in the Manual deploy section.
### Forking the Project
- Follow the steps below to fork this project,:
    - Locate the hangman repository: https://github.com/s-batish/tango-tennis
    - Click the 'Fork' button at the top right of the page.
### Cloning the Project
- Follow the steps below to clone this project:
    - Locate the hangman repository: https://github.com/s-batish/tango-tennis
    - Click the green 'Code' button.
    - Copy the URL for the repository.
    - Open the repository and open a new terminal.
    - Change the current directory to the location that you want the cloned directory to be.
    - Type 'git clone' and paste the copied URL.
    - Press 'enter' to create the clone.
## Technologies Used
### Technologies
- HTML
    - Used to create the structure of the website
- CSS
    - Used to implement additional styling across the website
- JavaScript
    - Used to set the timeout for the messages
- Python
    - Used for the application of the Django framework
- Django
    - Main framework used to build the website
- Bootstrap
    - Used to implement main styling across the website
- Gitpod
    - Used to develop and edit the code
- Git
    - Used to add, commit and push the code
- GitHub
    - Used to store and deploy the code
- [Balsamiq](https://balsamiq.com/)
    - Used to create wireframes
- [Lucidchart](https://www.lucidchart.com/)
    - Used to make the database diagrams
- [Cloudinary](https://cloudinary.com/)
    - Used to store the images used on the website
- [Google Fonts](https://fonts.google.com/)
    - Used to import fonts
- [Font Awesome](https://fontawesome.com/icons)
    - Used icons from this website for the social media icons
- [Fontjoy](https://fontjoy.com/)
    - Used to create the font pairings used on the website
- [TinyPNG](https://tinypng.com/)
    - Used to reduce the size of the images used on the website
- [Favicon](https://favicon.io/)
    - Used to create a favicon
### Python Modules Used
- Django class based views (CreateView, ListView, DeleteView, UpdateView)
    - Used to apply create, read, update and delete functionalities
- Mixins (LoginRequiredMixin, UserPassesTestMixin)
    - Used to ensure user is logged in to access certain views and tests whether they are authorised to access these views
- Messages
    - Used to post success messages for certain user actions
- Timedelta and date
    - Used to get today's date and edit which dates can be booked
### External Python Modules
- Django==3.2.20
    - Main framework used for the website
- django-allauth==0.54.0
    - Used for site authentication for sign in, login and logout
- cloudinary==1.33.0
    - Used to store images
- dj3-cloudinary-storage==0.0.6
    - Cloudinary library needed to run Cloudinary
- urllib3==1.26.15
    - Cloudinary library needed to run Cloudinary
- dj-database-url==0.5.0
    - Library needed for PostgreSQL
- psycopg2==2.9.6
    - Used to connect to PostgreSQL
## Credits