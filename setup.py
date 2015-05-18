from setuptools import setup, find_packages


setup(
    name='ansible_testing',
    packages=find_packages(exclude=['tests', 'tests.*']),
    install_requires=[
        'ansible',
    ],
    entry_points={
        'console_scripts': [
            'ansible-validate-modules=ansible_testing.modules:main',
        ]
    }
)
