To use:

please install python, pdbp and git (e.g. using micromamba). Then, in your terminal, clone this repository. Example on Mac OS:

Setup (optional - skip this if you already have python, pdbp and git installed). To check, run:
```
python3 --version
git --version
python3 -c "import pdbp"
```
If the first two print a version number and the last one prints nothing, you're good to go. Otherwise:
```
brew install micromamba
brew install git
micromamba shell init --shell zsh      # then open a new terminal
micromamba create -n debugging-exercise -c conda-forge python=3.14 -y
micromamba activate debugging-exercise
pip install pdbp
```

Clone and run:
```
git clone https://github.com/mbeavitt/debuggers
cd debuggers
python3 z.py ACTG TTGATCACTGCCGAT
```
Enjoy!
