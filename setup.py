import setuptools

with open('README.md', 'r') as fh:
    long_description = fh.read()

setuptools.setup(
    name='dmparser',
    version='0.0',
    author='Bryan Fichera',
    author_email='bfichera@anl.gov',
    description='A parser for DM3 and DM4 files',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='github.com/bfichera/dmparser',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.0',
    install_requires=[
	'numpy',
    ],
)
