======================
Cookiecutter PyPackage
======================

.. image:: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/shield.svg
     :target: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/
     :alt: Updates
.. image:: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/python-3-shield.svg
     :target: https://pyup.io/repos/github/divick/cookiecutter-django-vagrant-ansible/
     :alt: Python 3

Powered by Cookiecutter_, Cookiecutter Django Vagrant Ansible is a commandline
utility for quickly setting up a Django application for local development using
Vagrant, local replica of testing infrastructure using Vagrant and deployment
to testing, staging and production environments using ansible.

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

.. _Cookiecutter Django Vagrant Ansible: https://github.com/divick/cookiecutter-django-vagrant-ansible

Build Status
-------------

Linux:

.. image:: https://img.shields.io/travis/audreyr/cookiecutter-pypackage.svg
    :target: https://travis-ci.org/audreyr/cookiecutter-pypackage
    :alt: Linux build status on Travis CI

Quickstart
----------

Install the latest Cookiecutter if you haven't installed it yet (this requires
Cookiecutter 1.5.0 or higher)::

    pip install -U cookiecutter

Generate a Django project::

    cookiecutter https://github.com/divick/cookiecutter-django-vagrant-ansible

Then:

* Create a repo and put it there.
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
to create your own version. This project itself has created using

Cookiecutter_: https://github.com/audreyr/cookiecutter-pypackage/

customized for development on Django with Vagrant and provisioning / deployment
using ansible.

https://github.com/divick/cookiecutter-django-vagrant-ansible

Or Submit a Pull Request
~~~~~~~~~~~~~~~~~~~~~~~~

I also accept pull requests on this, if they're small, atomic, and if they
make my own packaging experience better.


.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _Travis-CI: http://travis-ci.org/
.. _Tox: http://testrun.org/tox/
.. _Sphinx: http://sphinx-doc.org/
.. _ReadTheDocs: https://readthedocs.io/
.. _`pyup.io`: https://pyup.io/
.. _Bumpversion: https://github.com/peritus/bumpversion
.. _PyPi: https://pypi.python.org/pypi
.. _`ardydedase/cookiecutter-pypackage`: https://github.com/ardydedase/cookiecutter-pypackage
