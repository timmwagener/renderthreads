
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
      version='0.2.3',
      description='Package that enables easy command-line multithreaded rendering for Nuke.',
      url='https://github.com/timmwagener/renderthreads',
      author='Timm Wagener',
      author_email='wagenertimm@gmail.com',
      license='MIT',
      keywords='Foundy TheFoundry Nuke Pipeline Compositing Filmakademie Timm Wagener Multithreading Commandline Rendering',
      packages=find_packages(),
      include_package_data=True,
      classifiers=['Development Status :: 4 - Beta',
                      'Intended Audience :: End Users/Desktop',
                      'Operating System :: Microsoft :: Windows',
                      'Programming Language :: Python',
                      'Topic :: Software Development',
                      'Topic :: Utilities',
                      'Topic :: Multimedia',
                      'Topic :: Multimedia :: Graphics',
                      'Topic :: Multimedia :: Graphics :: 3D Rendering',
                      'Topic :: Multimedia :: Graphics :: Graphics Conversion',
                      'Topic :: Multimedia :: Graphics :: Presentation',
                      'Topic :: Multimedia :: Video',
                      'Topic :: Multimedia :: Video :: Conversion',
                      'Topic :: Multimedia :: Video :: Display',
                      'Topic :: Multimedia :: Video :: Non-Linear Editor',
                      'Topic :: Documentation :: Sphinx',],
      zip_safe = False)
