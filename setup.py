from setuptools import setup

setup(
    name='weather',
    version='1.0',
    entry_points={
        'console_scripts': [
            'weather=weather.run:handle'
        ]
    },
    packages=['weather', 'weather.cli', 'weather.gui', 'weather.core'],
    url='https://github.com/BGerg/weatherProject',
    license='MIT',
    author='Cof',
    author_email='-',
    description='Get information, get and create statistics about weather.'
)
