Banzai-EasyBuild
================

**Banzai-EasyBuild (BEB) is for installing 3rd Party Banzai dependencies**

We use the awesome EasyBuild software package to manage/install required 3rd
party bioinformatic pacakages. For more information on EasyBuild software
please see: http://hpcugent.github.io/easybuild/

By default we have set easybuild==1.10.0 as a requirement and should be
installed during the Banzai-EasyBuild install process.


Boostrapping all requirements with EasyBuild
--------------------------------------------

Preliminary software:
    * Your cluster/system will have to have the "modules" package installed. It 
      is available at: http://modules.sourceforge.net/
    * PIP >= 1.52. Please use: *pip --version*. If pip exists use: pip install
      --upgrade pip otherwise: wget
      https://raw.github.com/pypa/pip/master/contrib/get-pip.py; python
      get-pip.py


The modules package allows you to:: 

    $ module avail
    $ module list
    $ module del


You'll next have to clone this repository::

    $ git clone https://github.com/mscook/Banzai-EasyBuild.git


Now::
    $ cd 



            By default EasyBuild should have been installed with Banzai. To
            test this::

                $ which eb # should print the full path the the eb binary.


                What you will need to do:

                Update your MODULEPATH & EASYBUILD_INSTALLPATH environamental
                variables.

                --sourcepath
                --buildpath
                --installpath
                $MODULEPATH
                --repository, --repositorypath



                /work2/UQ/Science/SCMB/Beatson/bin/easybuild/1.10.0/lib/python2.7/site-packages/easybuild_easyconfigs-1.10.0.0-py2.7.egg/easybuild/easyconfigs
