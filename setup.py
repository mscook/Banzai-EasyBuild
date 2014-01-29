import os, sys
from os.path import join, dirname

try:
    from setuptools import setup, find_packages
except ImportError:
    # Bootstrap if we don't have setuptools available
    from ez_setup import use_setuptools
    use_setuptools()

import beb


if sys.argv[-1] == 'publish':
    os.system('python setup.py sdist upload')
    sys.exit()

os.system("rm -rf build/ dist/ Banzai_EasyBuild.egg-info/")

setup(
    name                 = beb.__title__,
    version              = beb.__version__,
    author               = beb.__author__,
    author_email         = beb.__author_email__,
    description          = (beb.__description__+". Banzai-EasyBuild (BEB) is "
                            "for installing 3rd party Banzai NGS pipeline "
                            "dependencies"),
    packages             = find_packages(),
    long_description     = open(join(dirname(__file__), 'README.rst')).read(),
    url                  = beb.__url__,
    install_requires     = [
            'easybuild==1.10.0'
            ],
    include_package_data = True,
    license              = "Educational Community License, v2.0 (ECL-2.0)",
    zip_safe             = False,
    classifiers          = (
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 2 :: Only',
        'Topic :: Scientific/Engineering :: Bio-Informatics',
    ),
)
