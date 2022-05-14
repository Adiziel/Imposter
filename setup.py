from hashlib import md5
from setuptools import setup, find_packages

setup(
  name='im_poster',
  version = 0.0.1,
  url='https://github.com/Adiziel/Imposter',
  description='Im_poster is a Telegram Posts Management Tool',
  long_description= file: README.md,
  long_description_content_type= text/markdown,
  author='Adiziel',
  author_email='aditya.pathak.plus@gmail.com',
  packages=find_packages(),
  keywords=['python', 'telegram', 'telegram bot'],
)