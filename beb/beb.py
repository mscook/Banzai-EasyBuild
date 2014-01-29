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

RECIPES_GIT = 'https://github.com/mscook/BEB-recipes.git'

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
    check_requirements()


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
