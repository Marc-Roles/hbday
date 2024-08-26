from setuptools import setup

setup(
    name="hbday",
    author="Marc Roles",
    version="0.1",
    py_modules=['hbday'],
    entry_points={
        'console_scripts': [
            'hbday=hbday:main',
        ],
    },
)
