#!/usr/bin/env python

from pybuilder.core import init, use_plugin

name = "WoeUSB-ng"
version = "0.1.0"

use_plugin("python.core")
use_plugin("python.stdeb")
use_plugin("python.flake8")
use_plugin("python.distutils")
use_plugin("python.install_dependencies")

default_task = "publish"


@init
def initialize(project):
    project.build_depends_on('flake8')
    project.build_depends_on('stdeb')
    project.build_depends_on('dpkg-buildpackage')

    project.depends_on('wxPython')

    project.set_property('dir_source_main_python', 'src')
