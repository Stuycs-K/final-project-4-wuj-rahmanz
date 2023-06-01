# Work Log

## Zesan Rahman

### May 17, 2023

Researched about Burp Intruder. Assuming payload is a wordlist, there are 4 different attack-types:


* Sniper - places each payload into each payload position. Requests = length of payload * num of positions
* Battering Ram - Iterates through the payload, inputting the word for each position. Reqests = payload length
* Pitchfork - Different wordlists for each payload position. Requests depend on the payloads' lengths.
* Cluster Bomb - Similar to pitchfork. However, every possible combination of payloads is tested.

More info: https://systemweakness.com/attack-types-in-intruder-burpsuite-5c65900f71c7

### May 22, 2023

Absent for May 18 and 19 due to AP exams

Classwork plan: A website hosted by a VM. The beginning of each page describes sniper, battering ram, and pitchfork. At the bottom of each page is a login that we use to demonstrate each attack.

Homework plan: One of the linked pages is a login page, the rest of them are blank pages with "nothing there". However, using burp proxy and creating a site map will lead you to 2 payloads: one with a list of usernames and one with a list of passwords. Then they do a clusterbomb attack on the site.

Started working on website.

### May 23-24, 2023

Finished the HTML of the website. Got all the basic content down. 

### May 30,, 2023

Finished tryhackme room and secret pages for task

## Joseph Wu

### May 17, 2023

Researched and created a vm. Currently in the process of getting it to host a website.

### May 18, 2023

Attempted to create a VM with VirtualBox.

### May 19, 2023

Realized approach to VM was wrong. There goes everything :D

### May 22, 2023

Now using vagrant in combination with virtual box to create VM. In process of creating web server for VM.

### May 23, 2023

VM now successfully hosts a website at ip 192.168.33.10, accessible by the host. Make sure to put any website stuff in /box/webcontent.


### May 24, 2023
Researching how to get flask to work with apache

### May 25, 2023
Setup provisioning for VM
Flask now works with Apache. Webcontents renamed to app.
Make sure this is file structure:

|-app
    |
    |- __init__.py
    |
    |- staic
    |   |
    |   |- images and stuff
    |
    |- templates
        |
        |- index.html
        |- sniper.html
        |-etc

### May 26, 2023
Got User account database setup
Created Navbar with links to each page. Houses the login/logout.
    - Base.html houses nav bar
        - use {% extends 'base.html' %} {% block main %}
                ------code------
                {% endblock %}
          on other html pages to include nav bar on that page
Use Foundation for styling

### May 29, 2023
Added images to each page
* index.html is home page
each other page is self explanitory

### May 31, 2023
Fix login
SUPPER_SECRET_PASSWORDS now dynamically contains all accounts and their passwords
Profile page created
    - Able to change password of an account