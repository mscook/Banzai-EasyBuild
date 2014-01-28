import ez_setup
ez_setup.use_setuptools()

from setuptools import setup, find_packages
from os.path import join, dirname
import beb


setup(
    name             = 'Banzai-EasyBuild',
    version          = beb.__version__,
    author           = "Mitchell Stanton-Cook",
    author_email     = "m.stantoncook@gmail.com",
    description      = ("Banzai-EasyBuild (BEB) is for installing 3rd party "
                        "Banzai NGS pipeline dependencies"),
    packages         = find_packages(),
    long_description = open(join(dirname(__file__), 'README.rst')).read(),
    url              = "https://github.com/mscook/Banzai-EasyBuild",
    install_requires = [
        'easybuild==1.10.0'
        ]
)
