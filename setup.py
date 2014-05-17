from setuptools import setup

setup(
    name='boatd_client',
    version='0.1',
    author='Louis Taylor',
    author_email='kragniz@gmail.com',
    description=('Python wrapper for the boatd API, used to write behavior scripts.'),
    license='GPL',
    keywords='boat sailing wrapper rest',
    url='https://github.com/boatd/python-boatd',
    packages=['boatd_client'],
    test_requires=['nose', 'HTTPretty'],
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
    ],
)
