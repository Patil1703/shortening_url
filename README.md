URL shortening web app

Features:
1.  Shorten long URLs to a 6-character short code.
2.  Validate input URLs for correctness.
3.  Redirect short URLs to their original destinations.
4.  Track and increment click counts for each short URL.
5.  Store creation dates for each shortened URL.
6.  Simple analytics dashboard to view URLs, clicks, and creation dates.
7.  Flash messages for user feedback on URL submission.

Technologies Used

- Python 3.x
- Flask
- SQLite (via 'sqlite3' module)
- HTML (Jinja2 templating)


Background:

I wasn’t familiar with Flask-SQLAlchemy but chose it because it helps abstract database interactions.
I read through the official documentation and first tested some simple examples.
Since the requirement was to use SQLite, Flask would be a better option.
So, I started by researching Flask first, as it is the foundation of our application.
I learned that Flask also offers security features such as auto-escaping and sandboxing.
Additionally, I learned about HTML injection vulnerabilities related to POST and GET requests.


Project Workflow:

1. I began by importing Flask and creating a function to accept long URLs, using 'app.route' with dynamic routing.
2. Initially, I encountered errors when trying to connect the HTML file to the Python script. When I encountered this error in connecting HTML and Flask. I searched for 'connect HTML template Flask' and found render_template in the Flask docs.
3. I started implementing HTTP methods GET and POST.
4. The '/' route was set to represent the home page.
5. Simultaneously, I created the HTML index page.
6. The index page included a form to accept long URLs along with buttons for submission.
7. I used the 'request' library to read data submitted from HTML. Additionally, I utilized 'url_for' to build URLs dynamically.
8. To validate URLs, I checked if Flask had a built-in solution. It didn’t, so I used Python’s urllib.parse after checking documentation and examples.
9. I wanted to prevent duplicate short codes, so I ensured the short_code column was unique and used a retry logic in case of collision.
10. To catch user errors, I validated URL formats and used flash messages to notify users about incorrect inputs.
11. When the app did not open automatically in the browser, I researched how to connect Flask to localhost and implemented the solution.
12. Although my code had no syntax errors, running the app resulted in errors on localhost.
13. I sought assistance from ChatGPT by providing the current state of my code and error details.
14. One identified mistake was, Initially placing the URL validator inside the route handler, which made it inaccessible in other parts of the code. After ChatGPT pointed it out, I moved it to a standalone function.
15. While fixing errors with ChatGPT’s help, I learned to use the 'redirect' function to navigate between pages and prevent form resubmission.
16. I considered how to inform users when their URL is valid and shortening is in process, as invalid URLs were only known internally.
17. I researched how to display messages or alerts like in HTML and learned about Flask’s 'flash' method for this purpose.
18. Running the program again, I encountered a 'jinja2.exceptions.TemplateNotFound: index.html'  error, I realized Flask expects templates inside a templates/ folder — a naming convention I learned to respect going forward., which was resolved by adding a 'templates' folder.
19. Another issue was an indentation error causing a flash message ("success: URL is valid! (but not yet shortened)"), which I fixed.
20. The program accepted input but did not produce output, so I started working on database integration.
21. I created a function to generate a short code of length 6 using ASCII letters and digits.
22. I implemented a redirect function that maps shortened URLs to their original long URL destinations.
23. I began connecting SQLite with my Flask application.
24. After downloading SQLite, I identified the need for database columns such as primary key, long URL, and short URL.
25. I wrote a function to connect to the database and store inputs on each submission.
26. I used a cursor to execute SQL commands.
27. Once the database connection was established, I started working on an analytics dashboard.
28. I connected the database data to the analytics HTML page.
29. Running the code showed no database table or short URL functionality initially.
30. I created a function to print all database tables for debugging purposes.
31. The webpage frequently showed “Short URL not found.” I consulted Gemini AI to identify potential causes.
32. Upon review, I found syntax errors in the redirect function and analytics HTML template.
33. After seeing how the same bug repeated due to bad indentation, I started double-checking Python formatting more carefully.
34. Specifically, mismatched variable unpacking between '(short_code, long_url)' in 'app.py' and '(long_url, short_code)' in 'analytics.html' caused issues, which I corrected.
35. To implement click counts, I searched for “link tracker in Flask” and followed relevant tutorials. I read blog posts and forum answers, and verified them by testing in my own code.
36. I found a helpful tutorial on DigitalOcean and cross-checked it with my code, leveraging both Google and ChatGPT for assistance.
37. After updating the code, the click count was not incrementing initially, so I added an SQL increment query within the redirect method.
38. I corrected spelling mistakes and other syntax errors that arose.
39. After successfully implementing click counts, I proceeded to add a creation date for each shortened URL.
