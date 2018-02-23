# Key Learning points for Developer's Tools

## Table of contents

1. Shell Workshop
2. What is version control?
3. Create A Git Repo
4. Review A Repo's History
5. Add Commits To A Repo
6. Tagging, Branching and Merging
7. Undoing Changes
8. Working with Remotes
9. Working on Another Developer's Repository
10. Staying in Sync With A Remote Repository
11. Requests & Responses
12. The Web from Python
13. HTTP in the Real World


## 1.  Shell Workshop
- __echo__ command is used to print messages in the shell.
- __!__ mark is a special character in the shell.
- If you put __' '__ around special signs then shell will interpret them as a regular string.
- To list content of a directory in the shell command __ls__ can be used.
- When you start the shell it will look into your home directory. To list content of another directory you can write __ls name_of_directory__.
- To check current directory use command __cd__.
- To go to another directory write __cd new_directory__.
- To go back to parent directory use command __..__
- __;__ lets us write two commands on the same line. They will be executed separately
- __$__ sign in front of the word indicates that it is a shell variable.
- __pwd__ stands for print working directory.
- Unix uses __/__ to separate folders in the directory.
- __ls -l__ - prints longer, more details description of files.
- Shell lets you match file names with the patterns. If you want to find all pdf documents in your directory you can use following code: __ls -l Documents/*.pdf__
- __ls abc*__   # list all files starting with abc---
- __ls *abc*__  # list all files containing --abc--
- __ls *abc__   # list all files ending with --abc
- __mkdir__ is used for creating new directory.
- In order to move file to another folder you can use command __mv__. You need to specify which file are you moving to which directory __mv 'file_to_move' drectory_name__
- It is also possible to match many documents at the same time and move them together to the new directory e.g __mv Documents/*pdf Documents/Books__
- to download file from the web you can use command __curl__. It will show the html for the page. If you add __curl L_ followed by the website addres in ' '__ you will be able to see the source code for the website.
- Curl is very useful to download files by URL: __curl -0 google.html -L 'http://google.com'__.
- The file can be downloaded from URl using following code __curl -L -o dictionary.txt 'https://tinyurl.com/zeyq9vc'__
- command __cat__ reads the file and outputs the content. It can read multiple files.
- command __less__ read file and shows one page at the time. Use can use __space__ or arrows to scroll down, __b__ to go back and __/__ to search and __q__ to quit.
- __rm__ is the command to remove of the file.
- __grep__ command can look for words in the file.
- To count number of words in the file we can use following code: __grep -c ibo filename__. You can use regular expressions for patterns matching using grep.
- In shell whenever you create or modify variable you just give it name and = e.g __numbers='one two tree'__.
- If you want to print new variable you need to follow following command: __echo $file_name__.
- The value of __$PWD__ is the current working directory.
- __LOGNAME__ is an environment variable that contains the username of the account you're logged in as.
- Files contain shell comands are called shell scripts.

# 2. What is version control?
``Version control System (VCS)`` helps you to create save points that will help you save a current state of your work.

``Commit`` - snapshot of your work.

``Repository/repo`` - directory which contains all your work.

A ``checkout`` is when content in the repository has been copied to the Working Directory.

``Staging Area/Staging Index/Index`` - A file in the Git directory that stores information about what will go into your next commit.

``SHA`` - ID number of the commit.

``Branch`` -  new line of development is created that diverges from the
main line of development.

# 3. Create A Git Repo

To create a new repository with Git, we'll use the ``git init`` command.
