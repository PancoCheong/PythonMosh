This is the homepage of our project.

Choose an open source license template from
https://choosealicense.com/

eg. GNU General Public License v3.0

pip install setuptools wheel twine

# generate source distribution and build distribution

python setup.py sdist bdist_wheel

reference: https://packaging.python.org/tutorials/packaging-projects/

upload:
twine upload dist/\*

install:
pipenv install pancopackage
