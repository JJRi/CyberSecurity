# Quick memo

### Used tools:
Ghidra 

EDB-debugger

Calculator with programmer mode

## Memo

In main program asks for username and key. After given, there is "check_and_modify" function in which it does the main work, it also takes 2 parametrs (given username and key). In check_and_modify you have 4 loops. First one checks that given username has 10 characters. Second loop checks that given key has only numbers and letters a through f.

Third loop goes through the given username and calls modify function, which does little magic to the username and afterwards username is crossreferenced to data found at:
**DAT_080488b0: 9e ac f7 d1 37 ae 6a 0c 3f a4 00**

Modify takes 3 parameters counter, username and char_var, which is set to 0xAA before loop. Modify iterates through the usernames characters. Basicly it shifts the character bin to right according to counter(actually the counter is check with AND-operator with value 0x7), puts it in register to hold. Then it it checks the counter with AND 0x7, subtracts that from 0x8 and shifts to left by result. 

Then the result and previous result from storage are merged with OR operator and first two values (AL register at this point) is modified with the XOR operator using the previous iterations result. First time the char_var is used. The result is crossreferenced with the data on DAT_080488b0.

Fourth loop goes through the key, it check the characters two at a time and references that to results of the modify funtion using counter, the username and char_var which is first time set to 0xFF and then the result of modify. 

With the correct username your are able to generate 40 characters long key, which is framed with NIXU{} and there is the challenges flag.


TODO:
Would it be possible to solve this with Angr or make a script/program that calculates the work done on modify?




