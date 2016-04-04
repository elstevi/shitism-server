# shitism-server
A small flask app that randomly outputs one of Jim Lahey's shitisms from our curated selection of shitisms.

## endpoints

### /chat
This requires no arguments, and is a POST. It returns a json object with the shitism embeded. It is meant for webhook use with popular chat applications like rocketchat and slack. It should just work. There is an example of setup in the example part of this readme.

### /cli
This requires no arguments, and is a GET. It returns a plaintext body that is the shitism, followed by a newline (\n). Useful for cli applications like replacing fortune.

### /
This requires no arguments, and is a GET. It returns a plaintext body that is the shitism.

## Faq
Q: What is a shitism?
A: A genre of sayings that Jim Lahey, a trailer park boys character, says often to his foe. They always include some mutation of shit.

Q: You forgot my favorite shitism!
Q: You spelled * wrong!
Q: Why didn't you do * ?
A: Open a pull request.

Q: I'm not quite sure if it is worth it to run a server just to get my daily dose of shitisms.
A: You are wrong, but I maintain this server:  . Use it if you wish.

Q: Why did you waste your time writing this?
A: Why did you spend your time giving a shit? 

## Examples of use

### Web Browser
Go to the server in your web browser.

### .cshrc, .bashrc, whatever your poison
add this line on systems with fetch:
fetch -o - -q --timeout=2 http://ava.sea.douglas-enterprises.com:5000i/cli

or this line on systems with wget:
wget -qO- --timeout=2 http://ava.sea.douglas-enterprises.com:5000/cli

### rocketchat & slack
My shitism-server integration in rocketchat is an outgoing webhook.
| config option | my value | description |
| name		| shitisms | the name of the integration |
| channel 	| NULL	   | i want shitisms in all of my channels |
| trigger words | .shitism | don't want any false positives on shit|
| urls		| http://<shitism_server> | the url to you or my shitism server|
| post as	| my username | the username the bot posts as |
| alias		| Jim Lahee - Trailer Park Supervisor |
| avatar url 	| https://i.ytimg.com/vi/EE_hObInp9I/maxresdefault.jpg | because authentic|

Thats about all you need. 
