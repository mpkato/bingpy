from setuptools import setup, find_packages
import os
import sys

def find_scripts(scripts_path):
  base_path = os.path.abspath(scripts_path)
  return list([os.path.join(scripts_path, path) for path in [file_name for file_name in os.listdir(base_path) if os.path.isfile(
             os.path.join(base_path, file_name))]])


libdir = "lib/bingpy3"
sys.path.insert(0, libdir)

import info
import version
setup_options = info.INFO
setup_options["version"] = version.VERSION
setup_options.update(dict(
  install_requires = open('requirements.txt').read().splitlines(),
  packages         = find_packages(libdir),
  package_dir      = {"": libdir},
))

setup(**setup_options)
