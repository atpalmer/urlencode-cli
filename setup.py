from setuptools import setup


setup(
    name='urlquote',
    packages=['urlquote_cli'],
    entry_points=dict(console_scripts=[
        'urlquote=urlquote_cli.main:main',
    ]),
)
