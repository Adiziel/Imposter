from hashlib import md5
from setuptools import setup, find_packages


def readme():
  with open('README.md') as f:
    return f.read()

setup(
  name='im_botposter',
  version = "0.0.2",
  url='https://github.com/Adiziel/Imposter',
  description='Im_poster is a Telegram Posts Management Tool',
  long_description= readme(),
  author='Adiziel',
  author_email='aditya.pathak.plus@gmail.com',
  packages=find_packages(),
  keywords=['python', 'telegram', 'telegram bot'],
  install_requires=['requests', 'json']
)