To use:

please install python, pdbp and git (e.g. using micromamba). Then, in your terminal, clone this repository. Example on Mac OS:

Setup:
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
