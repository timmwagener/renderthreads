
"""
renderthreads
==========================================

Package that enables easy command-line
multithreaded rendering for Nuke.
"""

# Import
# ------------------------------------------------------------------
from setuptools import setup
from setuptools import find_packages

# Setup
# ------------------------------------------------------------------
setup(name='renderthreads',
      version='0.2.1',
      description='Package that enables easy command-line multithreaded rendering for Nuke.',
      url='https://github.com/timmwagener/renderthreads',
      author='Timm Wagener',
      author_email='wagenertimm@gmail.com',
      license='MIT',
      keywords='Foundy TheFoundry Nuke Pipeline Compositing Filmakademie Timm Wagener Multithreading Commandline Rendering',
      packages=find_packages(),
      package_data = {'renderthreads.media.ui': ['*'],
      					'renderthreads.media.fonts': ['*'],
      					'renderthreads.media.icons': ['*'],
      					'renderthreads.lib.third_party.pysideuic': ['*'],
      					'renderthreads.lib.third_party.pysideuic.Compiler': ['*'],
      					'renderthreads.lib.third_party.pysideuic.port_v2': ['*'],
      					'renderthreads.lib.third_party.pysideuic.widget-plugins': ['*']},
      zip_safe=False)
