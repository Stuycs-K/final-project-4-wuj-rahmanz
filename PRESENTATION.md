# The Weakest Link

By Joseph Wu and Zesan Rahman

Tryhackme room - https://tryhackme.com/room/burpsuiteintruderqu

## What is Burp Intruder?

Burp intruder is a tool in burp used for automating customized attacks against web applications. It enables you to configure attacks that send the same HTTP request over and over again, inserting different payloads into predefined positions each time.

There are 4 different types of attacks that we will go into depth soon.

* Sniper 
* Pitchfork
* ClusterBomb
* Battering Ram

### Basic Terminology

Positions - Any section of the website that users can input information in. For this website, we're going to mostly use logins so usernames and passwords.

Payloads - Lists of possible words that can be correct when inputted in a position. 

## Creating a Site Map

First, we need to establish a target. Go under the target tab and then go to the site map tab. If you're on the website on Burpsuite, you should see folders on the left side and a request/response box on the bottom right. 

Next, click on the arrow pointing to the website you're on. For our site, you should see a login folder. Open that and click on the folder under login. It should say something like email=\<email>&password=\<password>.

In order to manipulate this weakness, we need to send the request to burp intruder. You can copy/paste it or right click on the request and click send to Intruder. Now, go to the Intruder tab and you should see the request and the target in the payload positions section.

## Sniper
<p align = "center">
<img src = https://community.akamai.steamstatic.com/economy/image/-9a81dlWLwJ2UUGcVs_nsVtzdOEdtWwKGZZLQHTxDZ7I56KU0Zwwo4NUX4oFJZEHLbXH5ApeO4YmlhxYQknCRvCo04DEVlxkKgpot621FAR17PLfYQJD_9W7m5a0mvLwOq7cqWdQ-sJ0xOzAot-jiQa3-hBqYzvzLdSVJlQ3NQvR-FfsxL3qh5e7vM6bzSA26Sg8pSGKJUPeNtY/360fx360f>
</p>

Sniper delivers a payload one entry at a time. It is very useful for delivering XSS scripts (the javascript room that we did).

For this, let's say we know some valid email address - john@smith.com. We also know he has a password in the first 10 words in the rockyou list. 

There are weird symbols on the password and email. They indicate where the payload will go. Since we are using sniper, we are going to use the payload only on the password section. Set the email to john@smith.com. Then go to the payloads tab. Add the first 10 words of rockyou (you can either load or add them manually).

Start the attack and a new tab should open up. Notice the lengths. Most of them should be the same length, but one is different. That different length means the response was different. You should check the response of the one with a different length to confirm if that word is what you're looking for.

## Pitchfork

<p align = "center">
<img src = https://previews.123rf.com/images/iimages/iimages2205/iimages220502332/186220641-farmer-pig-holding-rake-with-haystack-illustration.jpg>
</p>

Pitchfork takes the nth index (n = 0,1,2,3...) of each payload and inputs them in their positions. Imagine you have two payloads, payload1 and payload2. The attack would look something like this-

* Request 1: Username = payload1[0] Password = payload2[0]
* Request 2: Username = payload1[1] Password = payload2[1]
* Request 3: Username = payload1[2] Password = payload2[2]

and so on until one of the payloads has no more words left.

Pitchfork is extremely useful for attacks with 2 different but somewhat related parameters. For example, an ID and a name or a name and birthday. 

## Cluster Bomb

<p align = "center">
<img src = https://cdn.discordapp.com/attachments/873056214664228866/1115380442393231370/clusterbomb.png>
</p>

Cluster bomb is similar to pitchfork except it runs all possible combinations of the payloads inputted. It is essentially a bruteforce method for pitchfork. Once again, imagine payload1 and payload2 with some amount of words. 

* Request 1: Username = payload1[0] Password = payload2[0]
* Request 2: Username = payload1[0] Password = payload2[1]
* Request 3: Username = payload1[0] Password = payload2[2]

and so on until payload1.length * payload2.length requests have been made. Once again, you are essentially praying something works out for this method.

## Extra - Battering Ram

<p align = "center">
<img src = https://images.fineartamerica.com/images/artworkimages/mediumlarge/2/our-battering-ram-michael-maslin.jpg>
</p>

Battering Ram is a very niche type of attack. It is similar to sniper, except it takes multiple positions. It takes only one payload. It will take a word in the payload and input it in all identified positions. This is useful for cookies with a body parameter or wherever you might need to input multiple of the same thing. 