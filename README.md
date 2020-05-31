MiniJournal is a project for the Software Engineer Experimental Course of AHU.



## Requirements

- Python >= 3.7.x
- Django >= 3.0.5

Install all of the requirements through `requirements.txt` (**After setting the development environment**) :

```bash
pip install -r requirements.txt
```

When the new requirement was added to the project, make sure to regenerate the `requirements.txt`, And change the note of requirement here (`Readme.md`) :

```bash
pip freeze > requirements.txt
```



## Setting Environment

Clone the git repository:

```bash
git clone https://github.com/Schrodinger-s-Trap/MiniJournal.git
```

Switch to the branch `test-pr`:

```bash
cd MiniJournal
git checkout test-pr
```

Install the `virtualenv` and create a new virtual environment `venv`:

```bash
pip install virtualenv
virtualenv venv
```

Activate the virtual environment:

```
# Windows(Powershell)
.\venv\Scripts\activate

# Windows(CMD)
venv\Scripts\activate

# Linux/MacOS
source venv/bin/activate
```

Then the name of the current virtual environment `venv` will now appear on the left of the prompt.

Install all of the requirements through `requirements.txt`:

```bash
pip install -r requirements.txt
```



## Running Project

Run the Django development server of the project in the local browser:

```
cd minijournal
python manage.py runserver
```

Then you can visit the project website in `http://127.0.0.1:8000`.