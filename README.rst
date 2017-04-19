============================================
Cookiecutter Django Vagrant Ansible template
============================================

Build Status
-------------

.. image:: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/shield.svg
     :target: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/
     :alt: Updates
.. image:: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/python-3-shield.svg
     :target: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/
     :alt: Python 3
.. image:: https://travis-ci.org/divick/cookiecutter-django-vagrant-ansible.svg?branch=master
    :target: https://travis-ci.org/divick/cookiecutter-django-vagrant-ansible
    :alt: Linux build status on Travis CI
.. image:: https://codecov.io/gh/divick/cookiecutter-django-vagrant-ansible/branch/master/graph/badge.svg
    :target: https://codecov.io/gh/divick/cookiecutter-django-vagrant-ansible
    :alt: Code coverage status on CodeCov.io

Powered by Cookiecutter_, Cookiecutter Django Vagrant Ansible is a commandline
utility for quickly setting up a Django application for local development using
Vagrant, local replica of testing infrastructure using Vagrant and deployment
to testing, staging and production environments using ansible.

The idea is to have a complete development setup in a VM without the need to
install packages locally on your host system. Additionally, it gets you quickly
started using Ansible for devops / deployment to any local as well as remote
machine with some sensible defaults for the playbooks. The cookiecutter.json
acts as a input to generate the Vagrantfile and ansible playbooks.

Currently the stack for deployment is based on:

* nginx -- as reverse proxy server
* uwsgi -- as wsgi server
* postgres -- as DB server
* nodejs -- for running tasks using gulp task runner
* bower -- for installing frontend dependencies

* GitHub repo: https://github.com/divick/cookiecutter-django-vagrant-ansible
* Documentation: https://cookiecutter-django-vagrant-ansible.readthedocs.io/
* Free software: GLPv3 license

Features
--------

* Support for Django-1.10
* Provides local setup for development using Vagrant box.
* Provides local_testing setup for replicating testing environment using
  Vagrant.
* Provides testing, staging and production setup for setup on digital ocean
  droplets or any other hosting provider with root access.
* Uses ansible for provisioning the setups for development, testing replica
  on localhost, testing, staging and production environments.
* Testing setup with ``unittest`` and ``python setup.py test`` or ``py.test``
* Travis-CI_: Ready for Travis Continuous Integration testing
* Tox_ testing: Setup to easily test for Python 2.6, 2.7, 3.3, 3.4, 3.5
* Sphinx_ docs: Documentation ready for generation with, for example, ReadTheDocs_
* Bumpversion_: Pre-configured version bumping with a single command
* Auto-release to PyPI_ when you push a new tag to master (optional)
* Command line interface using Click (optional)


Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.5.0 or higher)

::

    pip install -U cookiecutter

Clone CookiecutterDjangoVagrantAnsible_ to ~/.cookiecutters/

Install latest VirtualBox from VirtualBox_.

Install vagrant from Vagrant_.

Download the vagrant box of your choice from VagrantBoxes_. Currently it has
   been tested only with xenial64. You can download it directly using

::

    wget https://atlas.hashicorp.com/ubuntu/boxes/xenial64/versions/20170418.0.0/providers/virtualbox.box


Modify the ~/.cookiecutters/cookiecutter-django-vagrant-ansible/cookiecutter.json
as per your needs. Typically cookiecutter asks for user input for all the input
values in cookiecutter.json but unfortunately as of now the cookiecutter.json
does not support user input for nested values in cookiecutter.json. Which is
why we download it locally so as to modify the cookiecutter.json locally
instead of directly passing the github url of CookiecutterDjangoVagrantAnsible_.
Do remember to specify the path of your Vagrant box cookiecutter.json
without which Vagrant is going to complain about the missing Vagrant box file.

Run cookiecutter to create a new project template

::

    cookiecutter ~/.cookiecutters/cookiecutter-django-vagrant-ansible

Once it is done creating the project template (defaults to current
   directory), change to the project directory and run vagrant which
   creates a Virtualbox VM using the specified Vagrant box in
   cookiecutter.json, runs the playbook for a complete Django development
   setup in the Virtualbox VM.

::

    vagrant up

This will take a while to bring up a Virtual machine and install necessary
packages using ansible on the development machine.


Once it is up and running, you can simply ssh to the Virtual machine using::

    vagrant ssh

Change directory to /vagrant which is synced to the current directory::

    cd /vagrant

Notice that:

* All the apps specified in cookiecutter.json::ansible:my_apps have been created in the project.
* All the packages specified in cookiecutter.json::ansible:requirements have been generated in requirements.txt
* All the apps listed in cookiecutter.json::ansible:installed_apps have been generated and inserted in common_settings.py
* The db has been created with name and credentials specified in cookiecutter.json::ansible:
* The settings file has been generated based on the configuration specified in cookiecutter.json


* Add the repo to your Travis-CI_ account.
* Install the dev requirements into a virtualenv. (``pip install -r requirements_dev.txt``)
* Run the script `travis_pypi_setup.py` to encrypt your PyPI password in Travis config
  and activate automated deployment on PyPI when you push a new tag to master branch.
* Add the repo to your ReadTheDocs_ account + turn on the ReadTheDocs service hook.
* Release your package by pushing a new tag to master.
* Add a `requirements.txt` file that specifies the packages you will need for
  your project and their versions. For more info see the `pip docs for requirements files`_.
* Activate your project on `pyup.io`_.

.. _`pip docs for requirements files`: https://pip.pypa.io/en/stable/user_guide/#requirements-files

Fork This / Create Your Own
~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you have differences in your preferred setup, I encourage you to fork this
to create your own version. This project itself has been created using

Cookiecutter_: https://github.com/audreyr/cookiecutter-pypackage/

customized for development on Django with Vagrant and provisioning / deployment
using ansible.

https://github.com/divick/cookiecutter-django-vagrant-ansible

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _CookiecutterDjangoVagrantAnsible: https://github.com/divick/cookiecutter-django-vagrant-ansible
.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi
.. _VirtualBox: https://www.virtualbox.org/
.. _Vagrant: https://www.vagrantup.com/downloads.html
.. _VagrantBoxes: https://atlas.hashicorp.com/boxes/search
