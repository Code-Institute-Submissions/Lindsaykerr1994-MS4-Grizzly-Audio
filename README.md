# Grizzly Audio Packs
![Grizzly Audio Packs](media/grizzlybanner.jpeg)
This is a submission for my fourth Milestone Project - Full Stack Frameworks with Django.
It was created by Lindsay Kerr, 2020
*Disclaimer: This wedpage is for educational purposes only*

---
## Table Of Contents
* [UX](#ux)
    * [User Goals](#usergoals)
    * [Design] (#design)
    * [Wireframing & Mockups](#wireframing)
* [Features](#features)
    * [Implemented](#implemented)
    * [Upcoming](#upcoming)
* [Technologies](#technologies)
    * [Libraries](#libraries)
    * [Languages](#languages)
    * [Tools](#tools)
* [Testing](#testing)
* [Deployment](#deployment)
    * [Github Repository](#github)
    * [Heroku](#github)
    * [AWS Hosting](#aws)
* [Credits](#credits)

## UX <a name="ux"></a>
### User Goals <a name="usergoals"></a>
---
### Design <a name="design"></a>
---
### Wireframing & Mockups <a name="wireframing"></a>
---

## Features <a name="features"></a>
### Implemented <a name="implemented"></a>
---
### Upcoming <a name="upcoming"></a>
---

## Technologies <a name="technologies></a>
### Languages <a name="languages"></a>
---
In the construction of this project, I utlised four different languages:
* [HTML](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,scripting%20languages%20such%20as%20JavaScript.) for the front-end foundations.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) for all webpage aesthics and styling.
* [JavaScript](https://www.javascript.com/) for any dynamic programming.
* [Python3](https://www.python.org/download/releases/3.0/) for all of my back-end programming.
### Libraries <a name="libraries"></a>
---
* [Django](https://www.djangoproject.com/) was used to implement a high-level Python framework for the backend development.
* [Bootstrap4](https://getbootstrap.com/) provided a web-responsive CSS framework for the front-end.
* [FontAwesome](https://fontawesome.com/start) provided the icons found through out the site.
* [TablerIcons](https://tablericons.com/) provided SVG icons that used in the carousel controls.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) was used as a template language to implement logic in the front-end development.
* [Psycopg2-Binary](https://pypi.org/project/psycopg2-binary/) is an adapter for the PostgreSQL database.
* [JQuery](https://jquery.com/download/) was used in tandem with JavaScript to ease the DOM manipulation.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) was used to enable the Python code to modify the AWS S3.
### Tools <a name="tools"></a>
---
* [Stripe](https://stripe.com/en-gb) is a service that handled any online payments service.
* [GitPod](https://gitpod.io/workspaces/) provided an IDE to create this project.
* [GitHub](https://github.com/) hosted and managed this project's repositories.
* [Heroku](https://dashboard.heroku.com/apps) allowed me to host the deployed version of this project.
* [SQLite](https://www.sqlite.org/index.html) is a database provided by Django that handles my JSON files in development.
* [PostgreSQL](https://www.postgresql.org/) is a database that works with Heroku to handle my JSON files after deployment.
* [Canva](https://www.canva.com/) was used in creating all media files, such as the audio pack cover images.
* [Sampleswap](https://sampleswap.org/filebrowser-new.php) is a royalty-free website that provided all audio files. To clarify, I claim no ownership over any audio file found on the page.
* [Pexels](https://www.pexels.com/) is a free stock image provider, where I was able to resource the background images used in the body element of 'index.html'.
## Testing <a name="testing"></a>
### Manual Testing <a name="manual"></a>
---
Throughout the development of this webpage, manual testing was implemented in every regard. This testing was simple but effective, testing each individual link, button or function. In this process, I was able to identify and locate every broken page or link before deployment. Unforunately, this testing is not 100% thorough, but it does allow me to simulate the user's experience through every step of a purchase or registration. Such bugs were handled and corrected to the best of my ability. 
Furthermore, before official deployment and project submission, I requested that trusted professionals used the website, attempting to push the site to its boundaries. They were able to analyse every feature or design found on the site.
### Responsive <a name="responsive"></a>
---
To confirm the responsiveness of the pages, I ran the project through a [Mobile Friendly Test](https://search.google.com/test/mobile-friendly). The test was only able to test one page at a time,so I ran the test with each template, with the results being: "Page is Mobile Friendly", as can be found [here](https://search.google.com/test/mobile-friendly?id=vMS5vOhoXJXS8-1sfNfiWQ). Along side this, I also conducted manual testing for responsiveness, running through the project's multiple pages, using the feature provided by Google Chrome's 'Inspect'. This allowed me to simulate viewing the webpage through the view of standard mobile devices, such as Mobile XS(320x557) or 4K(2560x1392). 
### Validation <a name="validation"></a>
---
No testing would be complete without validation.
I used three different validators/linters:
* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
* [JS Hint](https://jshint.com/)
Any and all problems or issues located by these validators were fixed pre-deployment.
Additionally, to validate any Python styling issues, I used the command in the command-line interface:
`$ flake8`
Any issues identified by this command were corrected to the best of my ability. There were some styling issues that were left unresolved, however these were all related to auto-generated files, such as my migration logs, or code automated in 'grizzly_audio/settings.py'.
## Deployment <a name="deployment"></a>
### Github Repository <a name="github"></a>
---

### Heroku <a name="heroku"></a>
---
### AWS Hosting <a name="aws"></a>
---
## Credits <a name="credits"></a>


Testing

https://search.google.com/test/mobile-friendly?id=vMS5vOhoXJXS8-1sfNfiWQ