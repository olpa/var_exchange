import setuptools

setuptools.setup(
    name='var_exchange',
    version='1.0.0',
    license='MIT',
    author='Oleg Parashchenko',
    author_email='olpa@uucode.com',
    description='Share Python variables over Dropbox',
    url='https://github.com/olpa/var_exchange/',
    classifiers=[
        'Topic :: Software Development :: Object Brokering',
    ],
    keywords=['pickle', 'dropbox'],
    package_dir={'var_exchange': './src/var_exchange'},
    packages=['var_exchange'],
    scripts=['./scripts/kd_run.py'],
    install_requires=['dropbox'],
    python_requires='>=3.6',
)
