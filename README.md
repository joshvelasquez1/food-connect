# Food Connect

## Recipe API Prototype

Searches TheMealDB by recipe name and displays up to five
matching recipes with their ingredients and amounts.

### Setup on Windows

Open a terminal in the food-connect folder and run:

python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt

### Run

python recipe_api.py

When prompted, enter a search such as chicken or bread.

### Current status

The prototype works locally. Integration with the team's
Django application and AWS hosting is still pending.