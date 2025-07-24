from setuptools import setup, find_packages

setup(
    name='keylogger_uv',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pynput',
        'cryptography'
    ],
    entry_points={
        'console_scripts': [
            'keyvi=keylogger_uv.clic:main',
        ],
    },
)






