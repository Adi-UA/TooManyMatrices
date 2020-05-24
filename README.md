# TooManyMatrices

Have you ever looked at a particularly gnarly math problem and thought, "there is _no way_ I can manually calculate _that_ without messing up"? If you have, then `TooManyMatrices` might ease your woes (your discrete math woes anyway) by running those calculations for you.

`TooManyMatrices` is a project in discrete mathematics where we ([@AdiUA](https://github.com/Adi-UA) and [@dev-ved30](https://github.com/dev-ved30)) build a website to solve all kinds of discrete math problems that are annoying to compute by hand or calculator.
## Using 

### Before Running 
* Run `pip install django` in the terminal
* Run `pip install numpy`

You must also clone the rep. Assuming you have Git Bash, you can use:

`git clone https://github.com/Adi-UA/TooManyMatrices.git`

Note: We are using `python 3.7.4` and `django 3.0.6`

### Running 

After going to TooManyMatrices > src on your computer, open `CMD` and run
`pythong manage.py runserver`

Open a browser and got to [localhost:8000/tmm/](localhost:8000/tmm/) to get started.

## Current Status

At this stage, we have matrix functionality and some basic calculations like factorial, r-permutations and r-combinations (WIP). We have implemented a primitive web interface using `django`. We are currently refining the interactions between the front and back end and plan on adding more functionality with a revised UI.
