"""
Setup file
"""
from distutils.core import setup
setup(name='UvaTools',
      version='0.1.0',
      packages=['UvaTools', 'UvaTools.lib', 'UvaTools.Users'],
      #py_modules=['UvaTools', 'UvaTools.lib', 'UvaTools.Users'],
      package_dir={'UvaTools': '', 'UvaTools.lib':'lib', 'UvaTools.Users':'Users'},
      description='My Uva Tools',
      author='OldNick',
      author_email='sd12582000@gmail.com',
      requires=['requests'],
     )
