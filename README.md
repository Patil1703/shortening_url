URL shortening web app

Features:
1. 

Background:
I wasn’t familiar with Flask-SQLAlchemy, but chose it because it helps abstract DB interactions. 
I read through its official docs and used simple examples to test first 
Since there is a requirement of using SQLite I've thought flask would be a better option
So, first i started off researching about flask first since it is the base of our application 
I got to know that it also offers security features such as auto-escaping and sandboxing
I learnt about HTML injections that are Post and Get


Working of the project:
1. First I've imported flask, Created a function to accept long URLs, app.route(we will be using dynamic routing)
2. While i faced errors to connect html file to python file i got to know that there is a library "render_template" that connects them
3. I've started with methods Get and Post
4. '/' represents home page
5. I simultaneously created a html index page
6. created a form accepting long URLs and created buttons
7. to read data from html we need a library called "request". There is also a library url_for that builds URLs.
8. By googling I've found out that flask has a method to validate URL and implementing it.
9. While running the app wasn't opening in browser so i had to again search how to connect flask to localhost. Implemented it
10. My code had no errors but while running the app i found error on local host
11. I asked chatgpt to help me fix with the eroor giving it the code i've generated until now
12. The mistake I did was to place the validator method inside the route 
13. While fixing the errors with help of chatGPT, It also taught me usage of a new function that is redirect, used to navigate between different
pages and preventing double-submissions.
14. I thought, How could we let the user know that the URL they've given is valid and we are performing the action of shortening it? If the URL is
invalid only we would know!
15. i have googled a way to pop a message or like an alert in HTML, in flask we do have a method that is called "flash"
16. I tried to run the program again and found myself with an error "jinja2.exceptions.TemplateNotFound: index.html" it said i had to add templates folder
17. After running the code again I found an error which was a flash message ("success: URL is valid! (but not yet shortened")). Which was just indentation 
error
18. While running the code was taking inputs but was not giving output, now i started working on connecting database
19. Now i have created a function to generate a short code taking length of 6 and providing ascii codes and digits
20. I have created a redirect function that allows my shortened url to connect to the long url destination.
21. I am now trying to connect SQLite to my flask code.
22. Downloaded the database. We would be needing, a primary key, long url, short url columns in our database
23. Creating a function to connect database so that everytime there is an input, it gets stored in the database.
24, creating a cursor method to implement sql commands
25. after connecting the databse now I am creating a Analytics dashboard
26. Now connected the databse to analytics html code.
27. After trying to run the code again there is not database table shown or the short url is opening.
28. I am trying to print all the tables from databse using print statement and creating a function
29. My web page constantly started showing ShortURL not found, took help of gemeni AI, asking what could be the problems for such error
30. started revisiting redirect function and analytics html, found a syntax error.
31. fixed the syntax error where in app.py (short_code,long_url) but in analytics(long_url,short_code) so there was an error in connection
32. Now to implement click counts, i have googled and found an article in medium but was unable to read but found the the woord "link tracker in flask"
then i googled 
