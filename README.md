# TooManyMatrices

Have you ever looked at a particularly gnarly math problem and thought, "there is _no way_ I can manually calculate _that_ without messing up"? If you have, then `TooManyMatrices` might ease your woes (your discrete math woes anyway) by running those calculations for you.

`TooManyMatrices` is a project in discrete mathematics where we ([@AdiUA](https://github.com/Adi-UA) and [@dev-ved30](https://github.com/dev-ved30)) build a website to solve all kinds of discrete math problems that are annoying to compute by hand or calculator.
## Using 

### Before Running (Assuming you have pip and git)
* Run `pip install wheel`
* Run `pip install django`
* Run `pip install numpy`

Then, clone the repo with: `git clone https://github.com/Adi-UA/TooManyMatrices.git`

Note: We are using `python 3.7.4`, `wheel 0.34.2`, `django 3.0.6` and `numpy 1.18.4`

### Running 

From inside the repo on your computer, go to `src`, open `a terminal and run:

`python manage.py runserver`

**Note:** This command works as is on `CMD`, and can work as is in a `Bash` environment if you have your `python3` alias set to `python`.

Finally, open a browser and go to `localhost:8000/tmm/` to get started.

## Current Status

At this stage, we have matrix functionality, some basic calculations like factorial, r-permutations and r-combinations (WIP), and a primitive web interface using `django`. We are currently refining the interactions between the front and back end and are working on adding a better UI with more functionality.
