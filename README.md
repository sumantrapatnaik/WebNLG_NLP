# WebNLG_NLP
Hi, I added all the initial files except the vocab.

-Eric on 4/15
Added properly matched .vi and .en files, Added a new parse script that is easier to work with.

All scripts should work in python3. Python2 will do some weird encodings, I recomend against using it for these scripts.


Adding this here to prevent too much clutter in the commit messages.
Here is a quick list of what tests I've done:
    With sumantra's code, orig dict:  	dev bleu 1.7
    With sumantra's code, copied dict: 	dev bleu 1.4
    (Sumantra's .vi and .en files do not match!)

    With indvidual triple, 	orig dict:  	dev bleu 3.1
    With indvidual triple, copied dict: 	dev bleu 4.3  
    (I might have used a 'comprehensive' dictonary for the above test, oops!)
    With indvidual triple, copied dict, removed '|': 3.2

    Fixed concat, left '|' in, copied dict:		dev bleu 10.6
    Fixed concat, removed '|', copied dict:		dev bleu 10.7
    
Next step is to start playing with the dictonary