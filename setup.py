from sys import version_info
from setuptools import setup

if version_info.major == 3 and version_info.minor < 6 or \
        version_info.major < 3:
    print('Your Python interpreter must be 3.6 or greater!')
    exit(1)

from freqtrade import __version__


setup(name='tradbot',
      version=__version__,
      description='Crypto Trading Bot',
      author='gcarq and contributors',
      author_email='pranshulgupta777@gmail.com',
      license='GPLv3',
      packages=['tradbot'],
      setup_requires=['pytest-runner', 'numpy'],
      tests_require=['pytest', 'pytest-mock', 'pytest-cov'],
      install_requires=[
          'ccxt',
          'SQLAlchemy',
          'python-telegram-bot',
          'arrow',
          'requests',
          'urllib3',
          'wrapt',
          'pandas',
          'scikit-learn',
          'scipy',
          'joblib',
          'jsonschema',
          'TA-Lib',
          'tabulate',
          'cachetools',
          'coinmarketcap',
          'scikit-optimize',
          'python-rapidjson',
          'py_find_1st'
      ],
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': [
              'freqtrade = freqtrade.main:main',
          ],
      },
      classifiers=[
          'Programming Language :: Python :: 3.6',
      ])
