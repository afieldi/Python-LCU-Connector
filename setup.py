from setuptools import setup

from os import path
this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='lcu_connector_python',
      version='1.0',
      description='Connects to the LCU',
      long_description=long_description,
      long_description_content_type='text/markdown',
      url='https://github.com/Earleking/Python-LCU-Connector',
      author='Earleking',
      author_email='arek.fielding@gmail.com',
      license='MIT',
      packages=['lcu_connector_python'],
      zip_safe=False)