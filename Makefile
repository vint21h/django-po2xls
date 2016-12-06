# django-po2xls
# Makefile

docs:
	rst2html README.rst > index.html && zip docs.zip index.html

clear:
	rm -rf index.html docs.zip build dist django_po2xls.egg-info

build:
	./setup.py bdist_wheel sdist

upload:
	./setup.py bdist_wheel sdist upload
