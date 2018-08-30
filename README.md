# Introduction
Smena is simple django application for keeping a log of duties.
## Installation

1. Clone the repository:
```
git clone https://github.com/manzhakdotcom/tceh.git
```
2. In the current work directory creating virtual environments:
```
python -m venv venv
```
3. Activate virtual environment::
```
source venv/Scripts/activate
```
4. Install all dependencies:
```
pip install -r requirements.txt
```
5. Prepare the database:
```
python manage.py migrate
```
6. Start the development server:
```
python manage.py runserver
```