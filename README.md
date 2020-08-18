# Grizzly Audio Packs
![Grizzly Audio Packs](media/grizzlybanner.jpeg){: width=100%}
This is a submission for my fourth Milestone Project - Full Stack Frameworks with Django.
It was created by Lindsay Kerr, 2020
*Disclaimer: This wedpage is for educational purposes only*

---
## Table Of Contents
* [UX](#ux)
    * [User Goals](#usergoals)
    * [Design](#design)
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



### Design <a name="design"></a>
I chose to keep the colour scheme as simple as possible. This will play into the minimalist design layout of the website. Together, the two will allow the functionality of the back-end speak for itself and promote the project. Furthermore, the simplicity of the site will allow users to navigate through the pages, and promote a sense of professionalism and style.
#### Colours:
* Dark Grey: #292929
* White: #ffffff
* Light Brown: #9c824a
* Gold: #aa842a
#### Fonts:
Only one font was used throughout these project: Arial. This was used in conjunction with font weight: 200 to garnish the pages with a slim, sleek environment.

### Wireframing & Mockups <a name="wireframing"></a>
All wireframes (created with Moqup, see [Tools](#tools) can be in the [Media Folder](media/wireframing)

## Features <a name="features"></a>
### Implemented <a name="implemented"></a>
* Accounts/ Profiles
Although a user is not required to create an account to purchase from Grizzly Audio Packs, they are encouraged to do, as they will have their information saved for further use. Furthermore, any purchases made will be stored under a unique order number. This will allow users to return to any purchase. Customers receive their puchased packs through a download link, therefore if they lose their packs and wish to re-download their purchases, they are able to do so with ease. Unofrtunately, this feature is only available to registered users. If an anonymous user tries to access an order history, they will be redirected.
* Search/ Sorting/ categories
When a customer is browsing the packs, they are able to filter the packs on display using a search term, that will search the name or description, by categories, so they can browse similar products, or they can sort all the products by price, name, publication date, or popularity.
* Sample Tracks
Users are unlikely to purchase audio files for their use without being able hear a sample first. On browsing packs, users are able to play a short sample of the pack in question. This audio file relies on JavaScript to immediately stop playing when closing the pack's modal window so that audio tracks do not play over one another. If a user so wishes to download this sample file, they are able to do so, which is why the sample tracks are kept as short as possible, however they are played in loops for the user's ease.
* Bag and checkout
Users are able to easily navigate through the bag and checkout pages. All objects entered into the session storage, so that the website will be able to access these objects while the user keeps the window open. On the bag page, users are able to easily see any necessary information, or if desired, they can easily remove packs from their bag. On the checkout page, users are shown how much money they saved by purchasing packs on sale. If the user has a registered profile, their information will be saved upon checkout, if that option is chosen. 
* Store Management
As a store owner, it is possible to add and edit packs. If on the editing page, the back-end system will load the pack's details into the form for ease of use. Furthermore any media or static files they require to display the pack will be uploaded and saved to the database. In the admin page, storeowners are able to see further details about each pack, such as publication date, or number of sales, so that they can see which packs generate the most income.

### Upcoming <a name="upcoming"></a>
* Coupons & Promotions<br/>
During the checkout stage of a customer's purchase, they will be invited to enter a promotional code that will reduce the grand total of their purchase, or of individual packs. Such promotions will attract new customers or will encourage existing customers to return. These codes will be used to promote a seasonal sale or given out as referrals.
* Similar Packs<br/>
As customers browse the different packs on offer, they will be shown a selection of audio packs that share similar qualities to the one they are currently inspecting. Such qualities would include shared categories, instruments, or even packs that were bought alongside this one by other customers. This will hopefully encourage customers to buy more packs in one purchase.
* Reviews<br/>
This upcoming feature will allow registered users to leave a review, a rating of out 5, and comments, informing other customers of the quality of the audio packs being offered. This will also allow the store owner another criteria in which to filter the packs in the main sale window.

## Technologies <a name="technologies"></a>
### Languages <a name="languages"></a>
In the construction of this project, I utlised four different languages:
* [HTML](https://en.wikipedia.org/wiki/HTML#:~:text=Hypertext%20Markup%20Language%20(HTML)%20is,scripting%20languages%20such%20as%20JavaScript.) for the front-end foundations.
* [CSS](https://en.wikipedia.org/wiki/Cascading_Style_Sheets) for all webpage aesthics and styling.
* [JavaScript](https://www.javascript.com/) for any dynamic programming.
* [Python3](https://www.python.org/download/releases/3.0/) for all of my back-end programming.

### Libraries <a name="libraries"></a>
* [Django](https://www.djangoproject.com/) was used to implement a high-level Python framework for the backend development.
* [Bootstrap4](https://getbootstrap.com/) provided a web-responsive CSS framework for the front-end.
* [FontAwesome](https://fontawesome.com/start) provided the icons found through out the site.
* [TablerIcons](https://tablericons.com/) provided SVG icons that used in the carousel controls.
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/) was used as a template language to implement logic in the front-end development.
* [Psycopg2-Binary](https://pypi.org/project/psycopg2-binary/) is an adapter for the PostgreSQL database.
* [JQuery](https://jquery.com/download/) was used in tandem with JavaScript to ease the DOM manipulation.
* [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) was used to enable the Python code to modify the AWS S3.

### Tools <a name="tools"></a>
* [Stripe](https://stripe.com/en-gb) is a service that handled any online payments service.
* [GitPod](https://gitpod.io/workspaces/) provided an IDE to create this project.
* [GitHub](https://github.com/) hosted and managed this project's repositories.
* [Heroku](https://dashboard.heroku.com/apps) allowed me to host the deployed version of this project.
* [SQLite](https://www.sqlite.org/index.html) is a database provided by Django that handles my JSON files in development.
* [PostgreSQL](https://www.postgresql.org/) is a database that works with Heroku to handle my JSON files after deployment.
* [Canva](https://www.canva.com/) was used in creating all media files, such as the audio pack cover images.
* [Sampleswap](https://sampleswap.org/filebrowser-new.php) is a royalty-free website that provided all audio files. To clarify, I claim no ownership over any audio file found on these pages, nor do I seek to generate any revenue from these files.
* [Pexels](https://www.pexels.com/) is a free stock image provider, where I was able to resource the background images used in the body element of 'index.html'. Again, I claim no ownership over any photographic files found on this website.
* [Moqup](moqups.com) provided the services to create my wireframing designs found above.

## Testing <a name="testing"></a>
### Manual Testing <a name="manual"></a>
Throughout the development of this webpage, manual testing was implemented in every regard. This testing was simple but effective, testing each individual link, button or function. In this process, I was able to identify and locate every broken page or link before deployment. Unforunately, this testing is not 100% thorough, but it does allow me to simulate the user's experience through every step of a purchase or registration. Such bugs were handled and corrected to the best of my ability. 
Furthermore, before official deployment and project submission, I requested that trusted professionals used the website, attempting to push the site to its boundaries. They were able to analyse every feature or design found on the site.

### Responsive <a name="responsive"></a>
To confirm the responsiveness of the pages, I ran the project through a [Mobile Friendly Test](https://search.google.com/test/mobile-friendly). The test was only able to test one page at a time,so I ran the test with each template, with the results being: "Page is Mobile Friendly", as can be found [here](https://search.google.com/test/mobile-friendly?id=vMS5vOhoXJXS8-1sfNfiWQ). Along side this, I also conducted manual testing for responsiveness, running through the project's multiple pages, using the feature provided by Google Chrome's 'Inspect'. This allowed me to simulate viewing the webpage through the view of standard mobile devices, such as Mobile XS(320x557) or 4K(2560x1392).


### Validation <a name="validation"></a>
No testing would be complete without validation.
I used three different validators/linters:
* [W3C HTML Validator](https://validator.w3.org/)
* [W3C CSS Jigsaw Validator](https://jigsaw.w3.org/css-validator/)
* [JS Hint](https://jshint.com/)
<br />
Any and all problems or issues located by these validators were fixed pre-deployment.
Additionally, to validate any Python styling issues, I used the command in the command-line interface:<br />
`$ flake8`<br />
Any issues identified by this command were corrected to the best of my ability. There were some styling issues that were left unresolved, however these were all related to auto-generated files, such as my migration logs, or code automated in 'grizzly_audio/settings.py'.

## Deployment <a name="deployment"></a>
### Github Repository <a name="github"></a>


### Heroku <a name="heroku"></a>


### AWS Hosting <a name="aws"></a>


## Credits <a name="credits"></a>

