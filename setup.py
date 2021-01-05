import os

from setuptools import find_packages
from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_requirements(req_file):
    """
    Read requirements file and return packages and git repos separately.
    """
    requirements = []
    dependency_links = []
    lines = read(req_file).split('\n')
    for line in lines:
        if line.startswith('git+'):
            dependency_links.append(line)
        else:
            requirements.append(line)
    return requirements, dependency_links


REQ_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'pip-dep')
core_reqs, core_dependency_links = get_requirements(os.path.join(REQ_DIR, 'requirements.txt'))
dev_extras = read(os.path.join(REQ_DIR, 'requirements_dev.txt')).split('\n')
tests_require = ['pytest', 'pytest-flake8']

setup(
    name='pyfe',
    version='0.0.1',
    author='Théo Ryffel, S.P. Sharan, Sukhad Joshi',
    author_email='contact@openmined.org',
    description='Functional Encryption on Tensors',
    license='Apache-2.0',
    keywords=('cryptography privacy secure cryptography privacy secure'),
    packages=find_packages(exclude=['docs', 'examples', 'dist']),
    include_package_data=True,
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    url='https://github.com/OpenMined/PyFE',
    install_requires=core_reqs,
    extras_require={'dev': dev_extras},
    dependency_links=core_dependency_links,
    setup_requires=['pytest-runner'],
    tests_require=tests_require,
    classifiers=['Programming Language :: Python :: 3', 'Operating System :: OS Independent'],
)
