from setuptools import setup

setup(
    name = 'Zipper',
    version = '1.0',
    py_modules = ['zip', 'unzip'],
    install_requires = ['Click',],
    entry_points = '''
    [console_scripts]
    zip = zip:zipFile
    unzip = unzip:unzipFile
    ''',
)