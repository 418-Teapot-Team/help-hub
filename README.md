# HelpHub Project - HandToHand - Teapot 418
This test task was done by team `TEAPOT-418` for `BEST` hackathon, which involves developing a website to help people search for volunteers. The backend stack for this project is Python Flask, and the frontend stack is Vue.js, Tailwind.css. Below, you will find all the necessary information and descriptions related to the test task.

## Description
The goal of this test task is to create a website for everyone that allows people to post their requests for help/volunteering.
The website has a user-friendly interface and provide functionalities such as login as volunteer or requestor, see all requests, apply to request for volunteers and approve applier for requestor.

**Team**:
- [Roman Skok](https://github.com/romesk) - backend
- [Mykola Balii](https://github.com/Kolia913) - frontend
- [Nasobko Tymofii](https://github.com/TimofiyJ) - backend
- [Pavlo Kramar](https://github.com/Pasha1007) - frontend
- [Oleksii Uzhva](https://github.com/oleksyii) - frontend

**This project uses**:
- [GitHub Actions](https://docs.github.com/en/actions)
- [GCP VM](https://cloud.google.com/products/compute), [MySQL](https://cloud.google.com/sql/postgresql)
- [Docker](https://www.docker.com/), [docker-compose](https://docs.docker.com/compose/)
- [Python](https://python.org/), [Flask](https://flask.palletsprojects.com), [SQLAlchemy](https://www.sqlalchemy.org/)
- [Vue.js](https://vuejs.org/), [Tailwind.css](https://tailwindcss.com/), [Pinia](https://pinia.vuejs.org/)
- [JWT tokens](https://jwt.io/)

> The website is hosted on AWS and can be reached using next address: http://34.107.31.175:3001/
>
> The website REST API is public and can be reached using next address: http://34.107.31.175:8001/

## How does the project actually work?

### Sign-in & Sign-up Page
Website includes a sign-in and sign-up page to manage user accounts. Users can create a new account by providing their desired name, email address, phone and password.
Existing users can sign in using their credentials to access their data. Also, during authorization user can select a role to be. Each user can have both roles.

### Key Features
* Users (logged in and not) can see all requests, but to apply you need to have a volunteer account.
* Users (logged in and not) can see all volunteers and their personal data to contact for help.
* Each user has a public profile and can edit its own
* After volunteers apply requestor can see all appliers and chose one to approve. After that chosen applier has better statistics.

### Local Setup
To setup locally run (do not forget to create .env file, there is .env.sample)

`docker-compose up --env-file=backend/.env`
