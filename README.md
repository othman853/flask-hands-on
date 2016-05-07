# Flask Hands On

##### Creating a Flask app from scratch to understand how Python organizes itself

Conclusions: 

 - Python has `pip` as Package Manager
 
> pip installs packages globally, similar to `npm install -g`, but the packages are still dependencies and not standalone versions, therefore, dependencies are shared accross different apps unless an isolation strategy is adopted

 - `PyEnv` manages python versions accross the system
 - `Virtualenv` isolates python envs and solves the pip shared dependencies problem
 - `pyenv-virtualenv` is a plugin of `virtualenv` for `pyenv`
 - `.python-version` is a file that lives inside each python project and is used to specify which python version is going to be used, allowing `pyenv` to do its work
 - `requirements.txt` is a manifest of dependencies in a python project
 - `pyenv-virtualenv` seems like a great strategy for environment isolation

##### Installing things:

`brew install pyenv` : install pyenv

`brew install virtualenv` : install virtualenv

`brew install pyenv-virtualenv` : install plugin for integrating both 

`pyenv install [PYTHON_VERSION]` : install a specific version of python

`pyenv virtualenv [PYTHON_VERSION] [ENVIRONMENT NAME]` : create a new environment of python with the specified version

`pip install -r [REQUIREMENTS_FILE]` : install requirements from requirements file

After that, specifying the created env into the .python-version will switch to it automatically

##### Misc Learnings:

 - pyc files can cause magic number error. This is due the python version change. They must be re-compiled
 - Flask `request` raises a 400 Bad Request Error when trying to access a field that does not exist on the form dictionary
 
## Flask Login

#### What I understood so far

 - Has the `LoginManager` class
 - Has the `UserMixin` for default auth methods on User model
 - `@login_manager.user_loader` A decorator of the source from where the users must come from.


