URL shortening web app

Features:
1.  Shortens long URLs into short codes.
2.  Click count tracking for each shortened link.
3.  Analytics page to view all URLs and statistics.
4.  Input validation to prevent invalid or duplicate entries.
5.  Persistent storage using SQLite.


Structure:

shortening_url/                 # Root project folder
  app.py                     # Main Flask application code
  url.db                     # SQLite database file (can be created on first run)
  
static/                    # Folder for static assets like CSS, JS, images
  styles.css             # CSS stylesheet for styling your pages
  
templates/                 # HTML templates folder (Flask expects this name)
  index.html             # Homepage with URL form and short URL display
  analytics.html         # Analytics dashboard page showing URLs and stats
  
README.md    


Background:

I wasn’t familiar with Flask-SQLAlchemy but chose it because it helps abstract database interactions.
I read through the official documentation and first tested some simple examples.
Since the requirement was to use SQLite, Flask would be a better option.
So, I started by researching Flask first, as it is the foundation of our application.
I learned that Flask also offers security features such as auto-escaping and sandboxing.
Additionally, I learned about HTML injection vulnerabilities related to POST and GET requests.


Project Workflow:

1. I began by importing Flask and creating a function to accept long URLs, using 'app.route' with dynamic routing.
2. Initially, I encountered errors when trying to connect the HTML file to the Python script. I discovered the 'render_template' function, which facilitates this connection.
3. I started implementing HTTP methods GET and POST.
4. The '/' route was set to represent the home page.
5. Simultaneously, I created the HTML index page.
6. The index page included a form to accept long URLs along with buttons for submission.
7. I used the 'request' library to read data submitted from HTML. Additionally, I utilized 'url_for' to build URLs dynamically.
8. Through research, I learned that Flask provides methods to validate URLs, which I then implemented.
9. When the app did not open automatically in the browser, I researched how to connect Flask to localhost and implemented the solution.
10. Although my code had no syntax errors, running the app resulted in errors on localhost.
11. I sought assistance from ChatGPT by providing the current state of my code and error details.
12. One identified mistake was placing the URL validator method inside the route function, which I corrected.
13. While fixing errors with ChatGPT’s help, I learned to use the 'redirect' function to navigate between pages and prevent form resubmission.
14. I considered how to inform users when their URL is valid and shortening is in process, as invalid URLs were only known internally.
15. I researched how to display messages or alerts like in HTML and learned about Flask’s 'flash' method for this purpose.
16. Running the program again, I encountered a 'jinja2.exceptions.TemplateNotFound: index.html'  error, which was resolved by adding a 'templates' folder.
17. Another issue was an indentation error causing a flash message ("success: URL is valid! (but not yet shortened)"), which I fixed.
18. The program accepted input but did not produce output, so I started working on database integration.
19. I created a function to generate a short code of length 6 using ASCII letters and digits.
20. I implemented a redirect function that maps shortened URLs to their original long URL destinations.
21. I began connecting SQLite with my Flask application.
22. After downloading SQLite, I identified the need for database columns such as primary key, long URL, and short URL.
23. I wrote a function to connect to the database and store inputs on each submission.
24. I used a cursor to execute SQL commands.
25. Once the database connection was established, I started working on an analytics dashboard.
26. I connected the database data to the analytics HTML page.
27. Running the code showed no database table or short URL functionality initially.
28. I created a function to print all database tables for debugging purposes.
29. The webpage frequently showed “Short URL not found.” I consulted Gemini AI to identify potential causes.
30. Upon review, I found syntax errors in the redirect function and analytics HTML template.
31. Specifically, mismatched variable unpacking between '(short_code, long_url)' in 'app.py' and '(long_url, short_code)' in 'analytics.html' caused issues, which I corrected.
32. To implement click counts, I searched for “link tracker in Flask” and followed relevant tutorials.
33. I found a helpful tutorial on DigitalOcean and cross-checked it with my code, leveraging both Google and ChatGPT for assistance.
34. After updating the code, the click count was not incrementing initially, so I added an SQL increment query within the redirect method.
35. I corrected spelling mistakes and other syntax errors that arose.
36. After successfully implementing click counts, I proceeded to add a creation date for each shortened URL.
