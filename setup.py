from setuptools import setup, find_packages

setup(
    name='my project',
    version='1.0.0',
    description='My Python project',
    author='Erosha Paudel',
    packages=find_packages(),
    install_requires=[
        'pytest',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
