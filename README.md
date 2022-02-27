## What does your program do ?

This program will generate for you a password and organise it into a file, it will also copy the generated password into your clipboard

## What are the prerequisites ?

This program need in addition of python 3, pyperclip.
You can install pyperclip by running the following command : < pip install pyperclip > on Windows.
                                                             < pip3 install pyperclip > on MacOS and Linux.

You can also remove the requirement just by removing the 7th and 92th line of the .py file

## Why There isen't any .exe ?

The awnser is easy ! This program is made with customisation in mind.
It's not rulled out of having one in the future, but for now it's not the case.

## What can be customised ?

You can easily customise the following few things ;

1. Add or edit Email address (or Pseudonym)
2. The Password lenght
3. The character that can be used for generation
4. The Pwd file structure
5. Files names and extentions

## How to customise them ?

1. You can add email to the program either by using the second option of the menu
   or you can open the "data.dbeml" in your favorite text editor, each email should be on a new line and you should always add a newline at the end.

   if you want to change the order in which the program list email address, you can only do that (As of now) in your favorite text editor,
   The first line is the first email or Pseudonym. and the last is the last.

   Here's an example of how a "normal" data.dbeml file look.
   <img src="https://github.com/Torreip/PyPassGen/blob/master/images/1.png" alt="Normal looking data.dbeml" />

2. By default the password lenght is set to 16, if you want to increase or decrease it  you can do so by modifying the 90th line whim should like this :
   (pwd = "".join(random.choices(chartest, k=16)))
   the value you should modify is the k, so for example to have a password lenght of 128 the line shoud look like this :
   pwd = "".join(random.choices(chartest, k=128))

3. By default the characters used by the generator is the following string stored at line 88 :
   #$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~';
   If for example you don't wan't any Special characters for your password you can just remove them (I actively discourage disabeling special characters as they add a security layer).

4. You can modify how the "pwd.txt" file is structered. by default it sould look like somethink like this : 
   
   --- Awnsome APP ---
   
   Email : Torreip@example.com
   Password : h7$YsvknHKdo~F1$

   The structure is located from line 94 to 96: the structure is everything between "".

5. Even tho it's not advised you obviously change file name and extension used by the program to do so you need to change EVERY occurence of the file being either opened. You can also change the file location.

###### Last Update 20/02/22 (or 02/20/22)