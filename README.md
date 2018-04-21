# WebNLG_NLP

-Pakhi 4/21
Hi, Removed "_" from mTriples, created new dictionary and converted text to lowercase.
    BLEU dev 23.3, BLEU train 1.3


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

-Eric on 4/19
After much pain and frustration, I think I have createNewVocab.py in a good state. It starts with a base vocab from the origonal project,
then adds any new words from the .en and .vi files. It strips out all puncuation, this may or may not be a good thing. Maybe have it add
both puncuation and unpuncuated words?

Note that it takes a while to run, this is due to me keeping word order AND preventing duplicate words from entering the file (which causes errors)

New scores to add:

    Fixed concat, .en dict removed pun:	    dev bleu 18.1

    Fixed concat, full dict removed pun:	dev bleu 19.4 (this is the current build!)


Strip '_' from input next? I see that the NN might deal with that already. See my notes in the relevant issue.
