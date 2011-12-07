# LADITools - Linux Audio Desktop Integration Tools
# Copyright (C) 2007-2010, Marc-Olivier Barre <marco@marcochapeau.org>
# Copyright (C) 2007-2009, Nedko Arnaudov <nedko@arnaudov.name>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import yaml

# Let's make sure we'll place the file in an existing dir
from os import environ, sep, mkdir
from os.path import exists
config_dir = environ['HOME'] + sep + ".config" + sep + "laditools" + sep
config_filename = config_dir + "laditools.conf"
if not exists (config_dir):
    mkdir (config_dir, 0755)

# Note to users of the config class. Only applications should create an instance
# of the config object. The ladimenu is *NOT* an application...
class config:
    def __init__ (self):
        try:
	    config_file = open (config_filename)
            self.appdict = yaml.load (config_file)
	    config_file.close ()
        except:
	    print "Config file doesn't exist, creating a new one..."
            self.appdict = dict ()

    # Returns the section named <app_name> from the global config
    def get_config_section (self, app_name):
        if app_name in self.appdict:
            return self.appdict[app_name]
        else:
            return None

    # Saves the section named <app_name> into the global config
    def set_config_section (self, app_name, param_dict):
	self.appdict[app_name] = param_dict

    # This writes the config file to the disk
    def save (self):
        config_file = open (config_filename, 'w')
        yaml.dump (self.appdict, config_file, default_flow_style=False)
	config_file.close ()