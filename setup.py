"""
Setup file
"""
from distutils.core import setup
setup(name='UvaTools',
      version='0.0.1',
      packages=['UvaTools', 'UvaTools.lib'],
      package_dir={'UvaTools': '', 'UvaTools.lib':'lib'},
      description='My Uva Tools',
      author='OldNick',
      author_email='sd12582000@gmail.com',
      requires=['requests'],
     )
