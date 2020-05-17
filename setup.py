import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='django-bulk-admin-marcusl',
    version='0.2.0',
    packages=find_packages(exclude=('example_project*', 'screenshots',)),
    include_package_data=True,
    license='BSD',
    description='Django bulk admin enables you to bulk add, bulk edit, bulk upload and bulk select in django admin.',
    long_description=README,
    url='https://github.com/marcusl/django-bulk-admin',
    author='Marcus Sonestedt',
    author_email='marcus.s.lindblom@gmail.com',
    install_requires=[
        'Django>=2.2+',
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.4',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
