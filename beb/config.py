# Copyright 2013 Mitchell Stanton-Cook Licensed under the
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


import os
import sys

class BanzaiEBConfig():
    """
    Banzai-EasyBuild configuration class
    """

    def __init__(self):
        self.config = self.read_config()

    def __getitem__(self, key):
        try:
            return self.config[key]
        except KeyError:
            msg = "Trying to get config option that does not exist.\n"
            sys.stderr.write(msg)
            return None

    def __setitem__(self, key, item):
        self.config[key] = item

    def read_config(self):
        """
        Read a Banzai-EasyBuild configuration file
    
        Currently only supports:
            * cfg_location = [def = '']
    """
        cfg = {}
        cfg['cfg_location'] = ''
        try:
            with open(os.path.expanduser('~/')+'.BanzaiEB.cfg') as fin:
                colors = []
                for line in fin:
                    if line.startswith('cfg_location'):
                        option, val = line.split('=')
                        cfg[option.strip()] = val.strip()
        except IOError:
            print "Banzai-EasyBuild config file NOT FOUND"
        return cfg

    def dump_items(self):
        """
        Prints all set configuration options to STDOUT
        """
        for key, value in self.config.items():
            print "%s = %s\n" % (str(key), str(value))

    def write_items(self):
        """
        Writes the config options to ~/.BanzaiEB.cfg
        """
        if os.path.isfile(os.path.expanduser('~/')+'.BanzaiEB.cfg'):
            print "Banzai-Easybuild config file exists. Not overwriting"
            sys.exit(-1)
        else:
            with open(os.path.expanduser('~/')+'.BanzaiEB.cfg', 'w') as fout:
                for key, value in self.config.items():
                    fout.write("%s = %s\n" % (str(key), str(value)))
