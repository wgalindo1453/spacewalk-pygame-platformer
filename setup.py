from setuptools import setup

setup(
    name='spacewalk',
    version='1.0',
    packages=['spacewalk', 'spacewalk.music', 'spacewalk.pictures'],
    install_requires=['pygame'],
    entry_points={
        'console_scripts': ['spacewalk=spacewalk.main:main']
    },
    package_data={
        'spacewalk': ['*.wav'],
        'spacewalk.pictures': ['*.png']
    }
)
