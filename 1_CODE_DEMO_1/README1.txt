To run the code, you will have to be running on either a Linux distribution or Mac OS X Snow Leopard(v10.6)+

You will have to have the following application installed:
	- Python v3.4+ 		(https://www.python.org/downloads/)
		- With pip installation(option to include installation while installing python)
	- PostgreSQL v10+ 	(https://www.postgresql.org)
	- Heroku CLI		(https://devcenter.heroku.com/articles/heroku-cli#download-and-install)

Once installed, you will have to install these python modules through the command line:
	- requests
	- Flask
	- gunicorn
	- psycopg2-binary
	- Flask-RESTful
	- google-auth
To install these modules, open your terminal/commandline and type in:
		- sudo pip3 install <module_name>
		Example: sudo pip3 install Flask-RESTful
To run our application locally, you will have to have access to a private key file which is NOT provided as it has very sensitive data. 

NOTE: Our application is very difficult to set up locally since it includes many parts. Google authentication does not work locally for our application at this time so in order to run the code locally, you will have to make some modifications to some files. If you must run the code locally, please do not hesitate to contact Louis at ly178@rutgers.edu for further instructions. 

Once the key file is in the application directory, you will be able to run the server locally by opening the command line and changing directories into our application folder. From here, you can run the following command in your terminal:
	- heroku local
If every goes correctly, you should be notified with a notification starting gunicorn. At this point, you will be able to visit the website on your web browser by entering in localhost:5000 in the address bar. All webpages will be linked to the the mainpage so everything will be available from the main website. One thing to note is that the database is always live. Changes to the accounts locally will also be reflected online. The application hosted locally will also pull data from the database displaying information that may already be on the live website.