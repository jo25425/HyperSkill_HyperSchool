# HyperSkill_HyperSchool

Basic implementation of the HyperSchool project for the "Intoduction to Django" track on the platform HyperSkill.

## Table of Contents

- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [AI contributions](#ai-contributions)

## Project Structure

Here are the main components of the project. What isn't listed is just standard Django boilerplate and wasn't modified for this project:

```
/HyperSkill_HyperSchool
    /HyperSchool
        settings.py
        urls.py
    /schedule
        /templates
            /schedule
        admin.py
        apps.py
        forms.py
        models.py
        urls.py
        views.py
    /scripts
    /templates
    manage.py
    requirements.txt
```

The main app is called `schedule`. The templates relating to this app are found within the `templates/schedule` folder in that folder. The other templates just relate to the general functioning of the site and not the app itself. The folder `scripts` contains a script that can be executed to generate some artificial data. See the Django extension [`runscript`](https://django-extensions.readthedocs.io/en/latest/runscript.html) for more information. More details on the content of that script can be found in the [AI contributions](#ai_contributions) section.

## Installation

These are step-by-step instructions on how to install and set up the project locally:

```bash
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runscript populate_db
python manage.py runserver
```

## Usage

Explain how to use the basic features of your Django site. Include examples if necessary. For example:

- Visit the home page at `http://localhost:8000/schedule/main/`
- Login and sign-up at pages `http://localhost:8000/login/` and `http://localhost:8000/signup/` respectively. No logout ☠️
- Access the admin panel at `http://localhost:8000/admin/`. You'll first need to create a superuser with `python manage.py createsuperuser`.

## AI Contributions

Parts of this project were generated via Chat GPT. 

- Synthetic data: After being passed the models to generate data for, Chat GPT was asked to generate some sample entries for each model at a time, each time specifying how these models are related (e.g. many to many relation). The outcome of this chat, after some small tweaks, is what is stored in the script `populate_db.py`.
- README.md: Chat GPT also provided the template for this README. Due to the simplicity of the project, the original "Configuration", "Contributing" and "License" sections were removed. The section "AI contributions" was also added.
