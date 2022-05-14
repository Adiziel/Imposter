from hashlib import md5
from setuptools import setup, find_packages

setup(
  name='im_botposter',
  version = "0.0.1",
  url='https://github.com/Adiziel/Imposter',
  description='Im_poster is a Telegram Posts Management Tool',
  long_description= 'Imposter is a telegram bot which creates a post with title and message with and index to track that post, in telegram channel or group in which this bot has been added.',
  author='Adiziel',
  author_email='aditya.pathak.plus@gmail.com',
  packages=find_packages(),
  keywords=['python', 'telegram', 'telegram bot'],
)