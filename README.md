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
