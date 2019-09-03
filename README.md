# Project-Finder

This program was designed to speed up the time it took me to analyze and respond to a work email.

## Setting
At the time of uploading this file, I work in IT and help provide relocation services. I receive weekly emails, usually on Mondays, about 
potential projects where my help might be needed. 

## Problem
Many other people that work for the same company also receive the project emails, so usually the people that answer first/early are 
the ones who are selected to work at the projects of their choice (projects normally only vary by location). Because of this, the projects
that come up around the area where I live are normally gone really fast, which makes the speed in which I respond to those work emails
very important.

## Constants
The work emails sent weekly by the company I work at are very structured and follow a standard format, as shown below.
> #(number) (Three letters in parenthesis)                                                                                    
> Size of project (in number of workstations)                                                                                         
> Date and time                                                                                                               
> *Location*

Here is a real project listing example:
> #3 (ATN)                                                                                                                    
> 150 WS                                                                                                        
> Wednesday 8/28 - 4pm                                                                                                        
> Friday 8/30 - 9am                                                                                                                   
> Redwood City    

## Solution
In order to fix my problem, I decided to create a python program that would easily filter out the projects that are too far from where I
live and also respond to the project listing email without having to manually write a response.

### Filtering by Location
I used regular expressions in order to easily parse through the text body of the email. The first set of regex filtered through the entire
email and extracted ALL of the projects it found. The second round of filtration went over the projects obtained from the first round and
determined which projects fit the location criteria I gave it.

### Reading/Sending Emails
In order to read and send emails, I used the imapclient, pyzmail, and smtplib modules. Something interesting about this part is that 
I had to decode the email text before processing it and I had to encode the response before I sent it.

### User Input
After the program is done determining whether a project is within a preferable city or not, the user is then given the option to 
respond to a certain project or not.

## Disclaimers/Limitations
Here are some limitations of this program:
  * Cannot send reply to more than one potential project
  * Passwords are stored in plain text
  * Certain characters are encoded incorrectly and show up as gibberish on the final email (does not detract from email's meaning)
  * Program is not easily changed; everything is thrown outside of functions and is read from top to bottom
  * Location is not dynamic
  
 Something I want to make known is that this program does not follow proper programming standards, such as the usage of methods, 
 functions, objects, etc. This program is just something fun I made to help me respond to my work emails quicker.






