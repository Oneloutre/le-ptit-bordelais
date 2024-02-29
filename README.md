![banner](Assets/banner.png)

---

![GitHub license](https://img.shields.io/github/license/oneloutre/le-ptit-bordelais) ![GitHub last commit](https://img.shields.io/github/last-commit/oneloutre/le-ptit-bordelais)![language](https://img.shields.io/badge/language-python-blue) ![GitHub repo size](https://img.shields.io/github/repo-size/oneloutre/le-ptit-bordelais) ![Made with love](https://img.shields.io/badge/%E2%9D%A4%EF%B8%8F_Made_with-love-red) 

Le p'tit bordelais is a simple discord bot written in Python.
We coded it for fun since we had nothing else to do (I hate maths.)


### What it can do for now :point_up: :

- With the command `/pont` you'll have the next 5 openings of the Pont Chaban Delmas
- The famous `/help` will get you the help menu.

### What it **can't** do for now :unamused: :

- cooking, cleaning, do your homework... basically, you'll have to do this on your own.

---

# Installation :wrench: :

Before every install step, download the git repo with

```git clone https://github.com/Oneloutre/le-ptit-bordelais.git```

Then, when it's done, create a file named `config.py`

in this file, simply write `BOT_TOKEN = "YOUR BOT TOKEN` and of course, replacing "YOUR BOT TOKEN" with... Your token. It makes sense, right ?

### Using Python :snake: directly :

Go in your folder using `cd le-ptit-bordelais` and then :

Execute `pip install -r requirements.txt` then `python main.py`

:warning: make sure that you're using Python **3.12** !

### Using Docker :whale: :

Execute `docker build -t le-ptit-bordelais .` then `docker run -d le-ptit-bordelais`


