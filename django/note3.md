## How to write reusable apps [Django]
[link](https://docs.djangoproject.com/en/2.2/intro/whatsnext/)


- The Python Package Index (PyPI) have a vast range of packages you can use in your own Python programs
- Package it to be use by others 
- easier to reuse
- Package
    - containes one or more files of Python code (modules)
    - can be imported
    - must contain a `__init__.py`
        - can be empty

- decouple URL using an **include**


### Package and make it easy for others to install
#### Prerequisites
- setuptools: to build package
- pip
#### Packaging
1. Create a parent Dir `django-polls` outside the project
2. move `polls` dir into `django-polls` 
3. create a file `django-polls/README.rst`

```txt
=====
Polls
=====

Polls is a simple Django app to conduct Web-based polls. For each
question, visitors can choose between a fixed number of answers.

Detailed documentation is in the "docs" directory.

Quick start
-----------

1. Add "polls" to your INSTALLED_APPS setting like this::

    INSTALLED_APPS = [
        ...
        'polls',
    ]

2. Include the polls URLconf in your project urls.py like this::

    path('polls/', include('polls.urls')),

3. Run `python manage.py migrate` to create the polls models.

4. Start the development server and visit http://127.0.0.1:8000/admin/
   to create a poll (you'll need the Admin app enabled).

5. Visit http://127.0.0.1:8000/polls/ to participate in the poll.
```
4. Create a ` django-polls/LICENSE` file and choose a license (will affect who is able to use your code)
5.  create a `django-polls/setup.py`
```
import os
from setuptools import find_packages, setup

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-polls',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    license='BSD License',  # example license
    description='A simple Django app to conduct Web-based polls.',
    long_description=README,
    url='https://www.example.com/',
    author='Your Name',
    author_email='yourname@example.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: X.Y',  # replace "X.Y" as appropriate
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',  # example license
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
```
6. Create `django-polls/MANIFEST.in` to include all the additional files
```
include LICENSE
include README.rst
recursive-include polls/static *
recursive-include polls/templates *

[optional, step 7]
recursive-include docs *
```
7. [optional] create a `django-polls/docs` folder
8. build Package
[inside `django-polls` dir]
> python setup.py sdist
- will creates a `dist` dir 
- and a build `django-polls-0.1.tar.gz`



## Using 
- install as user library
> pip install --user django-polls/dist/django-polls-0.1.tar.gz


# Publish
- send, upload
- post on public repository: Eg. PyPI