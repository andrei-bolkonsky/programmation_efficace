# Programmation efficace
This repo is about various algorithm applications from Christoph Dürr and Jill-Jênn Vie's book Programmation Efficace.

## Install

### Virtual environment
> MacOS and Zsh
1. Install homebrew
2. Install python and pip
3. Install pyenv and pyenv-virtualenv
4. Create your programmation\_efficace project

#### 1. Homebrew
```sh
/bin/bash -c “$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)”
```

#### 2. Python and Pip
```sh
brew install python
```

#### 3. Pyenv
```sh
brew update
brew install pyenv
brew install pyenv-virtualenv
```

Then you’ve to export PATH
```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
```

Add pyenv init to the profile
```sh
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.zshrc
echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv virtualenv-init -)"\nfi' >> ~/.zshrc
```

Install a default python version for pyenv:
```sh
pyenv install 3.7.0
```

#### 4. Create the local project
```sh
mkdir programmation_efficace
pyenv virtualenv 3.6.6 programmation_efficace
cd programmation_efficace
echo "programmation_efficace" > .python_version`
```
### Install the project 
Begin to git clone the project.
```sh
git clone "https://github.com/andrei-bolkonsky/programmation_efficace"
```

Then install the dependencies:
```sh
pip install -e .
```

## Usage 
Examples:
> At the root of the project
### Input file
Create a text file in the data/ repository with the input data you want to use.
Naming: **inputs_<algorith>.txt**

### Algorithm usage
Ruun a specific algorithm:
```sh
python src/<algorithm>.py < data/inputs_<algorithms>.txt
```
