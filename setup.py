try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Proyectos de matematicas computacionales',
    'author': 'Gerardo Teruel',
    'url': 'https://github.com/gerardogtn',
    'download_url': 'https://github.com/gerardogtn/matematicascomputacionales',
    'author_email': 'gerardogtn@gmail.com',
    'version': '0.1',
    'install_requires': ['pytest', 'python-igraph'],
    'packages': find_packages(exclude=('tests', 'docs', 'bin')),
    'scripts': [],
    'name': 'Matematicas computacionales'
}

setup(**config)
