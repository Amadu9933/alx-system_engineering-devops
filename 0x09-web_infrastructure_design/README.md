# 0x09. Web infrastructure design 

Imagine a user types "www.foobar.com" in their browser to access your website. Here is how the infrastructure would work:

Server: A server is a computer system that is connected to the internet and is responsible for hosting websites, applications, and other digital services. In our case, we are using one server that will host our website.

Domain Name: A domain name is the address that users use to access your website, for example, www.foobar.com. It is a human-readable identifier that maps to the IP address of the server where your website is hosted.

DNS Record: A DNS record is a type of configuration file that specifies the IP address associated with a domain name. In our case, we need to create a DNS record for the www subdomain that points to the IP address of our server, which is 8.8.8.8.

Web Server: A web server is a software application that handles HTTP requests and responses. It listens for incoming requests from users, sends them to the appropriate application server, and then returns the response to the user. In our case, we will use Nginx as our web server.

Application Server: An application server is a software application that runs the code base of your website or application. It processes requests from the web server, executes the application logic, and then returns a response to the web server. In our case, we will use an application server to host our code base.

Code Base: A code base is a collection of source code files that make up your website or application. It is compiled and executed by the application server.

Database: A database is a software application that stores and manages data. It provides a structured way to store and retrieve data, such as user accounts, product catalogs, and order histories. In our case, we will use MySQL as our database.

When a user types www.foobar.com into their browser, the following process occurs:

The user's computer sends an HTTP request to the web server at www.foobar.com.

Nginx, the web server, receives the request and forwards it to the appropriate application server based on the URL.

The application server processes the request, retrieves data from the database, and generates an HTTP response.

The application server sends the HTTP response back to Nginx.

Nginx sends the HTTP response back to the user's computer, and the website is displayed in the user's browser.

Issues with this infrastructure:

SPOF: This infrastructure has a single point of failure, which means that if the server fails, the website will go offline. To mitigate this, we can use multiple servers in a load-balanced setup, which distributes traffic among the servers, providing redundancy and fault tolerance.

Downtime during maintenance: Deploying new code or updates to the website will require restarting the web server and application server, which may cause temporary downtime. To minimize downtime, we can use techniques such as rolling deployments, where only a portion of the server is taken offline at a time, allowing the website to remain online during the update process.

Limited Scalability: As traffic to the website grows, a single server may not be able to handle the load. To scale the infrastructure, we can use techniques such as horizontal scaling, where additional servers are added to the load balancer as traffic increases. We can also use caching to reduce the load on the database and optimize the performance of the website.
