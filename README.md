# Kweh-clone-cog
This is a test to transfert Kweh to red-discordbot cog

## How to setup

### Setup Environnement
You will need a version of Python 3.8:
Why : https://docs.discord.red/en/stable/guide_cog_creation.html
Link to last installer : https://www.python.org/downloads/release/python-3810/

Create a virtual environnement using theses commands inside the root directory: 
```bash
pip install --user virtualenv virtualenvwrapper-win # adds tools to create virtual environnement
python -m virtualenv --python="C:\Program Files\Python38\python.exe" env # create virtual environnement
%cd%/env/Scripts/activate.bat # Activate the environnement
pip install -r requirement.txt # install prerequirements
``` 

### Run Bot
You need to create a bot by using theses commands :
```bash
redbot-setup # Follow instructions
redbot <instance name> --dev # Run bot
```
Then link it to a instance using : https://discord.com/developers/applications

### Add cogs

Contact your bot inside discord and use : 
```
[p]addpath <this_root_folder>
[p]load kweh
```

### Subsequent runs :

```bash
%cd%/env/Scripts/activate.bat
redbot <instance name> --dev
```

//
%cd%/env/Scripts/activate.bat
redbot testbot --dev