#!/usr/bin/env python
import os
import sys
from setuptools import setup

# Prepare and send a new release to PyPI
if "release" in sys.argv[-1]:
    os.system("python setup.py sdist")
    os.system("twine upload dist/ansibleblog_sphinx_theme*")
    os.system("rm -rf dist/ansibleblog_sphinx_theme*")
    sys.exit()

# Load the __version__ variable without importing the package already
exec(open('ansibleblog_sphinx_theme/version.py').read())

setup(name='ansibleblog_sphinx_theme',
      version=__version__,
      description="A beautiful, minimalist, and responsive theme for your Sphinx projects.",
      long_description=open('README.rst').read(),
      url='https://barentsen.github.io/ansibleblog-sphinx-theme/',
      author='Gonéri Le Bouder',
      author_email='goneri@lebouder.net',
      license='BSD',
      packages=['ansibleblog_sphinx_theme'],
      include_package_data=True,
      # See http://www.sphinx-doc.org/en/stable/theming.html#distribute-your-theme-as-a-python-package
      entry_points={"sphinx.html_themes": ["ansibleblog_sphinx_theme = ansibleblog_sphinx_theme"]},
      classifiers=[
          "Development Status :: 5 - Production/Stable",
          "Intended Audience :: Developers",
          "License :: OSI Approved :: BSD License",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Topic :: Documentation",
          "Topic :: Software Development :: Documentation",
          ],
      )
