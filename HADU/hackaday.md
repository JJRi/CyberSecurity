# Hackaday-U

I'm learning reverse engineering from the scratch. This is a free course with video, slides and exercises. 

[The course itself](https://hackaday.io/course/172292-introduction-to-reverse-engineering-with-ghidra)


|Session 1|Answer|notes|
|-|-|-|
|Ex1|hackadayu||
|EX2|hdayu||
|EX3|jarRi|fourt letter is third in CAPS|
|EX4|jcemcfc{/w|add 2 to ASCII codes of the secret word|
|skele|{bogia}|XOR letters with given keys|


|Session 2|Answer|notes|
|-|-|-|
|loop-example-1|FINDAJOBjarijar|Word lenght is 15. First 8 have to be speacials, numbers or caps.|
|control-flow-1|201 199|3 compares: 1st>2nd, SHL 2nd by 1 > 1st, 1st > 99|
|variables-example|J0(kb$!R|When keycode is tested in bash put it in to single quotes so bash won't error. Dynamic analysis gives the code in CMP if your too lazy to calculate the shifts.|
|func-example-1| |Equal amount of lower and uppercase characters.|
|heap-example-1|Any string with 12 uppercase characters|Program calculates the string lenght and allocates memory accordingly.|
|array-example|1 gbhjccxdm|Change keyword to pointer array, it's easier to read after that. Takes keyword of correct index and manipulates it two letters at a time. Subtracts smaller from bigger and adds 0x60. |

**In progress**
|Session 3|Answer|notes|
|-|-|-|
|structs| 00000002 naapurii 'YPP_d]XX' | it makes a struct where it saves the data. A function is used to  manipulate the structs variable to verify the password. Note to self: concept was clear, but to identify struct from assembly needs practise. |



