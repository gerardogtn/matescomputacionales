try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Proyectos de matematicas computacionales',
    'author': 'Gerardo Teruel',
    'url': 'https://github.com/gerardogtn',
    'download_url': 'https://github.com/gerardogtn/matematicascomputacionales',
    'author_email': 'gerardogtn@gmail.com',
    'version': '0.1',
    'install_requires': ['py.test'],
    'packages': ['project01', 'datastructures'],
    'scripts': [],
    'name': 'Projects'
}

setup(**config)
