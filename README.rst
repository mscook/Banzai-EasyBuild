Banzai-EasyBuild (BEB)
======================

**Banzai-EasyBuild (BEB) is for installing 3rd Party Banzai dependencies**.

We use the awesome EasyBuild_ software package to manage/install required 3rd
party bioinformatic packages. This is done in relatively automated manner-

.. image:: http://imgs.xkcd.com/comics/automation.png
   :align: center

.. _EasyBuild: http://hpcugent.github.io/easybuild/

This is essentially a no fuss next-generation sequencing analysis stack
bootstrapping tool.


Boostrapping all requirements with EasyBuild
--------------------------------------------

Preliminary software:
    * Your cluster/system will have to have **the modules package installed**. 
      For Ubuntu or derivaties: *sudo apt-get install environment-modules* 
      should do the trick. Source is available here_.
    * **PIP >= 1.52**. Please use: *pip --version*. If pip exists use: *pip 
      install --upgrade pip otherwise: wget
      https://raw.github.com/pypa/pip/master/contrib/get-pip.py; python
      get-pip.py*. More info on PIP_ here.
    * git_.  For Ubuntu or derivaties: *sudo apt-get install git*.

.. _here: http://modules.sourceforge.net
.. _PIP: http://www.pip-installer.org/en/latest/installing.html
.. _git: http://git-scm.com
.. _environment-modules: http://modules.sourceforge.net

The _environment-modules package allows you to:: 

    $ module avail
    $ module list
    $ module del

The PIP_ package allows you to install and manage Python packages::

    $ pip install some-python-package

The git_ software allows you to clone and manage source code. 


Install instructions
--------------------

**1)** Ensure you have installed/upgraded the 3 requirements listed above.


**2)** You'll next have to clone this repository::

    $ mkdir ~/REPOS
    $ cd !$
    $ git clone https://github.com/mscook/Banzai-EasyBuild.git


**3a)** Install the Banzai-EasyBuild (with root)::
    
    $ pip install ~/REPOS/Banzai-EasyBuild


**3b)** Install the Banzai-EasyBuild (without root)::
    
    $ pip install ~/REPOS/Banzai-EasyBuild --user


**4)** Testing the install::
    
    $ which eb
    $ which beb


**5)** Set some initial configuration paramaters::
    
    $ beb init


Here we set EasyBuild_ sourcepath, buildpath, installpath (--repository,
--repositorypath) and set $MODULEPATH.


**5)** Boostrapping the required software::

    $ beb bootstrap 


Updating packages
-----------------

Assumes that you have already performed a *beb init* and *beb bootstrap*::

    $ beb update


beb help listing
----------------

**$ beb -h**::

    usage: beb.py [-h] [-v] {init,update,bootstrap} ...

    Banzai-EasyBuild v0.1 - A no fuss next-generation sequencing analysis stack
    bootstrapping tool (https://github.com/mscook/Banzai-EasyBuild)

    positional arguments:
      {init,update,bootstrap}
                            Available commands:
        init                Configure EasyBuild and get current build recipes.
        update              Check for updated build recipes and rebuild required.
                            Assumes init has been run.
        bootstrap           Builds the current recipes. Assumes init has been run.

    optional arguments:
      -h, --help            show this help message and exit
      -v, --verbose         Verbose output

    Licence: ECL 2.0 by Mitchell Stanton-Cook <m.stantoncook@gmail.com>
