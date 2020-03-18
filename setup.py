from setuptools import setup
from biketrauma import __version__ as current_version

setup(
  name='biketrauma',
  version=current_version,
  description='Visualization of a bicycle accident db',
  url='https://github.com/opheliecoiffier/packaging_tutorial',
  author='Ophelie coiffier',
  author_email='ophelie.coiffier@etu.umontpellier.fr',
  license='MIT',
  packages=['biketrauma','biketrauma.io', 'biketrauma.preprocess', 'biketrauma.vis'],
  zip_safe=False
)
