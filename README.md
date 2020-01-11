# Interview

During the development process of this interview I used
[pyenv](https://github.com/pyenv/pyenv) as Python versions manager, and also
[pyenv-virtualenv](https://github.com/pyenv/pyenv-virtualenv) as a pyenv plugin
to manage virtualenvs.

If you also use the same tools as me when you `cd` the directory where you
clone this repo will automatically activate the virtualenv
that we'll create next.

## Steps to run this program

```
   $ git clone git@github.com:fjpalacios/interview.git
   $ pyenv install 3.8.0
   $ pyenv virtualenv 3.8.0 onestic
   $ cd interview
   $ pip3 install -r requirements.txt
   $ python3 main.py
```

## Steps to run the test suite

```
   $ pytest
```

## Comments on directories
The original CSV files are located in the **csv** directory, the CSV files
generated after the execution of the tasks are located in the **tasks**
directory.
