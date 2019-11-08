# Marvelus Module Management System

> Marvelus Module Management System

## Requirement
1. Python 3.7 
2. Node.js (npm)
3. MySQL version > 8 (set the root account's password to be `root` or edit the setting file in `Entrytask/settings.py`)

## Build Setup

### Database setup 
1. We use two databases named `entrytask` and `luminus` for our project. If you have existing database with same name. 
Do backup it first.
2. `mysql -uroot -p < schema.sql`
3. Enter the password

### JS dependencies
1. `cd frontend`
2. `npm install`
3. `npm run build`
4. `cd ..`

### Python virtual environment (optional)
1. `pip install virtualenv`
2. `virtualenv venv`
3. Activate base on your OS. (See Google)
4. See `(venv)` at start of your command line

### Python dependencies
1. `pip install -r requirements.txt`
2. `python manage.py migration`
3. `python manage.py runserver`

### Finally
1. Open `127.0.0.1:8000/` for login check. 
2. The hashed password is `123456` for all users
3. Possible username are `stu1`, `stu2`, `ta1`, `ta2`, `prof1`, `prof2` (See `schema.sql` for all users)
