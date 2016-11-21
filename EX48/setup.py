try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'My Project',
    'author': 'Bastian_KD',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'bkdelarocque@gmail.com',
    'version': 'O.1',
    'install_requires': ['nose'],
    'packages': ['NAME'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)
