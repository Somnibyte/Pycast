from setuptools import setup

setup(
    name =  "Pycast",
    version= "1.0",
    author= "Guled",
    py_modules = ['pycast'],
    install_requires=[
        'Click',
        'pyglet',
        'soundcloud'
    ],
    entry_points='''
        [console_scripts]
        pycast=pycast:cli
    ''',
    extras_require={
        'security': ['pyOpenSSL', 'ndg-httpsclient', 'pyasn1'],
    },

)
