# Intro - Crash Course to Awesome Programming Practices
## Understanding Source Control (Git & Github)
1. `Git` is a form of `source control`, a way to keep track of your changes in your code and help you manage to collaborate with others while programming. It's kinda like how Google Docs keeps track of everyone's history of what changes everyone has made. It’s incredibly useful because it becomes your personal portfolio and is used everywhere in the Computer Science world.

2. Github is like Google Drive but for code. It’s a service that stores `repositories`  or `repo` for short which is basically a “home” folder for a project.  The home folder for any project is also called the `root directory`. 

3. Companies like Google, Microsoft, IBM, etc. use GitHub and any publicly available project that you can contribute to is called an `Open Source Project`. *(don't push school assignments here because it's public and that can be counted as plagiarism, but you can still use git for yourself without pushing to the remotely to GitHub)*. 

4. Here is more info on Git in video form that goes through a simple tutorial and the process of how to use it:
https://www.youtube.com/watch?v=MJUJ4wbFm_A

## Getting to Know Source Control for Yourself (Gitimmersion Lab & Github)
1. Make a http://github.com/ account if you don’t already have one, this becomes your portfolio basically. 
2. Make a repo called `gitimmersion` and clone it and follow the instructions for the labs for git.
3. Try the `gitimmersion labs`  in that folder *(It uses the Ruby language, but git can be used with any piece of code or text).*
4. Link: http://gitimmersion.com/index.html *(You will need to setup git by downloading and installing it if you are on Windows. Otherwise, git should be already installed)*

## Getting Started with Python using Source Control - Teach Your Kids To Code by Bryson Payne
1. Make a http://github.com/ account if you don’t have one, this becomes your portfolio basically. 
2. Go on your GitHub and make a Repo called `PythonPractice`
3. Create a folder called gitprojects (I recommend using your home user account folder).
4. Clone that repo in your folder and it will create a folder called `PythonPractice`

In your terminal / command prompt it should be something like:
```bash
git clone https://www.github.com/username/PythonPractice.git
```
5. Complete your programming practice in that folder. 

### Exercise 1:  `SquareSpiral1.py`  

You are given the following code:

```python
# SquareSpiral1.py - Draws a square spiral
import turtle

t = turtle.Pen() 

for x in range(100):
	t.forward(x)
	t.left(90)
```

- In observance of best source control practices, you should commit often. In this piece of code there are two main parts, so you should create commit messages for both: creating the turtle and making it move in a spiral. 

(Assuming you have Python 3 Setup) 
1. Type the following code:
```python
# SquareSpiral1.py - Draws a square spiral
import turtle

t = turtle.Pen() 
```

- So far, we’ve created the `SquareSpiral1.py` file,  and imported the turtle `library`.  A `library`  in python is a collection of functions and methods that allows you to perform lots of actions without writing your own code.  `turtle` is a built in library in python which means you don’t have to download and install it. See: [25.1. turtle — Turtle graphics — Python 3.7.0 documentation](https://docs.python.org/3/library/turtle.html)

2. We now need to keep track of changes in your code “save it” with git.

	- To access the folder so you can do git commands on it, get the location of the file by right clicking on it and In your terminal or command prompt `cd` (change directory) into the `gitprojects/PythonPractice` folder. 
	
```bash 
cd gitprojects/PythonPractice 
```

	- Alternatively, you can find the exact location of a file or folder on Windows by right clicking on it and clicking properties or by simply right clicking on the folder and click `Git Bash Here`. For all other operating systems, simply just drag and drop the file onto the terminal after typing `cd ` and the folder location should automatically be generated.

In Terminal / Command Prompt type the following
- `git add SquareSpiral.py`
- `git commit -m "Created my first turtle"`
- `git push origin master` 

Aside – *The* `origin` * part pushes it remotes to a remote repository, “the cloud”, in our case it’s GitHub.* *Without the* `origin`*, it doesn’t push to GitHub but only locally.* *If you are using* `Jupyter Notebook`, *you can do bash commands like git by executing something like* `% git add SquareSpiral.py` *by itself and then deleting it after executing it.*

3. Finish the code:
```python
# SquareSpiral1.py - Draws a square spiral
import turtle

t = turtle.Pen() 

for x in range(100):
	t.forward(x)
	t.left(90)
```

Aside – *this* `for loop` *is an for each loop and reads as "for each x times counting from the range of 0 to 99" move turtle t forward by x then turn the turtle left 90 degrees.*

In Terminal / Command Prompt type the following
- `git add SquareSpiral.py`
- `git commit -m "Made my turtle dance in a spiral 100 times"`
- `git push origin master` 

4. YAY! You successfully made your commits and uploaded your first piece python code to GitHub as a git master!

## Bonus Points - Watch Intro to Python from Harvard’s CS50 class
- https://www.youtube.com/watch?v=n_8zxTH7SvA
- https://www.youtube.com/watch?v=icOod04jYww

## Share with me links to your GitHub Repositories 

1. Read about [The anatomy of a perfect pull request – Hugo Dias – Medium](https://medium.com/@hugooodias/the-anatomy-of-a-perfect-pull-request-567382bb6067)

2. Fork this repository and sending a pull request after adding your name and url to your repos when you change this file.

3. Set it up for the next person.

## I have completed my gitimmersion:
- Hansel Wei [gitimmersion](https://github.com/darkmastermindz/gitimmersion)
- Your Name [gitimmersion](https://github.com/{yourusername}/gitimmersion)

## I have started my PythonPractice:
- Hansel Wei [Python Practice](https://github.com/darkmastermindz/PythonPractice)
- Your Name [Python Practice](https://github.com/{yourusername}/PythonPractice)

## I have followed along and completed my PythonCS50_2017
- Hansel Wei [PythonCS50_2017](https://github.com/darkmastermindz/PythonCS50_2017)
- Your Name [PythonCS50_2017](https://github.com/{yourusername}/PythonCS50_2017)
