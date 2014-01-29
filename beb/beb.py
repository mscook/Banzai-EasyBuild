#!/usr/bin/env python

# Copyright 2014 Mitchell Stanton-Cook Licensed under the
# Educational Community License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may
# obtain a copy of the License at
#
# http://www.osedu.org/licenses/ECL-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an "AS IS"
# BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express
# or implied. See the License for the specific language governing
# permissions and limitations under the License.

"""
Banzai-EasyBuild (BEB) init and bootstrapping methods
"""

import sys, os, traceback, argparse
import time
import subprocess
import getpass
import config


BASE = '/home/%s/beb' % (getpass.getuser())
RECIPES_GIT = 'https://github.com/mscook/BEB-recipes.git'
BASE_EB_CONFIG = 'config/eb_config.cfg'

__title__        = 'Banzai-EasyBuild'
__version__      = '0.1'
__description__  = ("A no fuss next-generation sequencing analysis stack "
                    "bootstrapping tool")
__author__       = 'Mitchell Stanton-Cook'
__license__      = 'ECL 2.0'
__author_email__ = "m.stantoncook@gmail.com"
__url__          = 'https://github.com/mscook/Banzai-EasyBuild'

epi = "Licence: %s by %s <%s>" % (__license__,
                                  __author__,
                                  __author_email__)
__doc__ = " %s v%s - %s (%s)" % ( __title__,
                                  __version__,
                                  __description__,
                                  __url__)


def init_beb(args):
    """
    
    """
    eb_cfg = config.BanzaiEBConfig()
    check_requirements()
    setup_configs(get_eb_cfg_location(), setup_base_dirs(), eb_cfg)

def check_requirements():
    """
    Check that environment-modules and git are installed
    """
    passed = 0
    deps = ['modulecmd', 'git']
    for dep in deps:
        p = subprocess.Popen(["which", dep], stdout=subprocess.PIPE)
        if p.communicate()[0].strip().split('/')[-1] == dep:
            passed = passed+1
    if not passed == len(deps):
        print "Missing dependencies Please install %s" % (' and '.join(deps))
        sys.exit(-1)

def get_eb_cfg_location():
    """
    Determines the location of the EasyBuild configuration file
   
    :returns: the full path as a string to eb-config.cfg
    """
    p = subprocess.Popen(["which", 'beb'], stdout=subprocess.PIPE)
    return p.communicate()[0].split('bin/beb\n')[0]+BASE_EB_CONFIG

def setup_base_dirs():
    """
    Select & create the base directory and also pull down recipes
    
    :returns: the base directory
    """
    selected = raw_input(("Enter a base location (must be able to write to "
                "it) [%s]:" % (BASE)))
    if selected == '':
        selected = BASE
    selected = os.path.normpath(os.path.expanduser(selected))
    if os.path.isdir(selected):
        print "Base directory already exists. Exiting"
        sys.exit(-1)
    os.mkdir(selected)
    original = os.getcwd()
    os.chdir(selected)
    os.system("git clone %s" % (RECIPES_GIT))
    return selected
    
def setup_configs(cfg, base, cfg_obj):
    """
    Build the EasyBuild config file

    :param cfg: the full path to the EasyBuild config file with this 
                distribution
    :param base: the full path to the EastBuild base
    :param cfg_obj: a Banzai-EasyBuild config object
    """
    cfg_base = cfg.split('/')[-1]
    cfg_out = os.path.join(base, cfg_base)
    with open(cfg) as fin, open(cfg_out, 'w') as fout:
        for line in fin:
            if line.find("#buildpath=") != -1:
                cur = os.path.join(base, "easybuild/build")
                fout.write('%s%s\n' % (line[1:].strip(), cur))
            elif line.find("#installpath=") != -1:
                cur = os.path.join(base, "easybuild")
                fout.write('%s%s\n' % (line[1:].strip(), cur))
            elif line.find("#sourcepath=") != -1:
                cur = os.path.join(base, "easybuild/sources")
                fout.write('%s%s\n' % (line[1:].strip(), cur))
            elif line.find("#repositorypath=") != -1:
                cur = os.path.join(base, "BEB-recipes")
                fout.write('%s%s\n' % (line[1:].strip(), cur))
            else:
                fout.write(line)
    cfg_obj['cfg_location'] = cfg_out
    cfg_obj.write_items()
    
    ##set $MODULEPATH.

def update_beb(args):
    """
    
    """
    print "Update"


def bootstrap_beb(args):
    """
    
    """
    print "Bootstap"



if __name__ == '__main__':
    try:
        start_time = time.time()
        parser = argparse.ArgumentParser(description=__doc__, epilog=epi)
        parser.add_argument('-v', '--verbose', action='store_true',
                                        default=False, help='Verbose output')
        subparsers = parser.add_subparsers(help='Available commands:')
        
        init_parser = subparsers.add_parser('init', help=('Configure EasyBuild '
                                            'and get current build recipes.'))
        update_parser = subparsers.add_parser('update', help=('Check for '
                            'updated build recipes and rebuild required' 
                            '. Assumes init has been run.'))
        bootstrap_parser = subparsers.add_parser('bootstrap', help=('Builds '
                        'the current recipes. Assumes init has been run.'))
        init_parser.set_defaults(func=init_beb)
        update_parser.set_defaults(func=update_beb)
        bootstrap_parser.set_defaults(func=bootstrap_beb)
        args = parser.parse_args()
        if args.verbose:
            print "Executing @ " + time.asctime()
        args.func(args)
        if args.verbose:
            print "Ended @ " + time.asctime()
            print 'Exec time minutes %f:' % ((time.time() - start_time) / 60.0)
        sys.exit(0)
    except KeyboardInterrupt, e: # Ctrl-C
        raise e
    except SystemExit, e: # sys.exit()
        raise e
    except Exception, e:
        print 'ERROR, UNEXPECTED EXCEPTION'
        print str(e)
        traceback.print_exc()
        os._exit(1)
