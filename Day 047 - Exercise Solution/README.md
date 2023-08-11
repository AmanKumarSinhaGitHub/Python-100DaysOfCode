# Solution in Day 40

### Link : [Click Here](https://github.com/AmanKumarSinhaGitHub/Python-100DaysOfCode/tree/main/Day%20040%20-%20Exercise%20-%20Secret%20Code%20Language)

---

**Ques :** Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

## Coding:
If : the word contains atleast 3 characters, 
remove the first letter and append it at the end
And append three random characters at the starting and the end

else:
simply reverse the string

```
Example 01:

harry (more than 3 char word)
step 1 : arryh (remove first char and append to end)
step 2 : lkoarryhqwe (now add 3 random char)
```

```
Example 02:

of (less than or equal to 3 char word)
step 1 : fo (reverse the string)
```
## Decoding:
if the word contains less than 3 characters, reverse it
else:
remove 3 characters from start and end. Now remove the last letter and append it to the beginning

```
Example 01:

lkoarryhqwe (more than 3 char word)
step 1 : arryh (remove three random char form beginning and end)

step 2 : harry (now remove last char and append to beginning)
```

```
Example 02:

fo (less than or equal to 3 char word)
step 1 : of (reverse the string)
```

__Your program should ask whether you want to code or decode__

Don't understand the question? Watch this video -
[Click Here](https://youtu.be/pOWJ6WgVRIU "youtube.com/CodeWithHarry")

