# Why do you need this thing?
In present time it's very hard to be a junior in the Hi Tech echo system.   
You always need to be on the edge for finding people to help you search for that desired job.  
This notion led me to write this little python program.

# What it does?
In short, this tool searches on google for linkedin profiles that matches a certain keyword.  
Then it stores the profile urls to a file for later use. 

# How it does it:
1. First it goes to google.com and search for the query 'site:linkedin.com/in/ AND "KEYWORD" AND "LOCATION"'
    * Example query: 'site:linkedin.com/in/ AND "I\'m hiring" AND "Israel"'
2. For every result it gets it stores the linkedin url to a file for later use 
3. Login to your personal linkedin profile and iterate the list one by one to try to add them to your reined list with a personal note
    * for every loop it puts the person url in a different list to indicate we already tried to add them to our personal fried list
    
# What do I need to do to use your tool?
Very little just 
* substitute "WEBDRIVER_PATH" with your selenium webdriver path ([Get it here](https://www.selenium.dev/downloads/#browsersExpand "WebDrivers") )
* substitute "KEYWORD" with the desired search keyword, Example: "HR"
* substitute "LOCATION" with the desired location, Example: "israel"
* Create a file with a custom message inside the Messages folder
  * You can create more than one file, the code will choose one of them at random 
  * One thing to keep in mind, Linkedin restricts the messages to only 300 characters so make sure not to write messages that are longer then that  
* substitute "EMAIL_OR_USERNAME" and "PASSWORD" with your linkedin username and password
* Run the script 

# I feel like I can help you make this tool even better!
Great I'm open for PR's forked my repo and submit your improvements.  
I would be happy to review then and marge them if they fit my goal 

