# Prerequisites:
- Must have nodejs & npm installed and in PATH
- User must have script execution permissions (at least RemoteSigned) (only applies to Windows users)


# How to run:
1. Have 2 separate terminals open
2. (Optional but highly recommended) Create a new virtual environment (in one of the terminal windows) inside of the folder this README.md file is in, and activate it in both of the terminals like so:
```
python -m venv .venv
source .venv/bin/activate # Linux/macOS
.venv\Scripts\activate # Windows
```
3. Run `pip install -r requirements.txt` in one of the terminal windows (this installs all the necessary packages)
4. On both terminal windows, run `cd RigetZooAdventures`
5. In one of the terminal windows, run `python manage.py tailwind start`
6. In the other terminal window, run `python manage.py runserver`
7. Open a browser and go to the address that shows up in the terminal window after completing step 6 (should be http://127.0.0.1:8000/):
```
Starting development server at [address]
Quit the server with CTRL-BREAK.
```


# Troubleshooting:
- If on Linux/macOS, you may have to comment out the `NPM_BIN_PATH` variable near the bottom of the settings.py file in the ./RolsaTech/RolsaTech/ directory
- If on Linux/macOS and you get an error on step 5, you need to run `chmod u+x ./RigetZooAdventures/theme/static_src/node_modules/.bin/*`, then do step 5 again
