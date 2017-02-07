from setuptools import setup, find_packages

setup(
    name='ydd',
    version='0.2',
    author='dengshilong',
    author_email='dengshilong1988@gmail.com',
    description="youdao dict terminal",
    keywords="youdao dict terminal",
    url='https://github.com/dengshilong/ydd',
    zip_safe=False,
    py_modules=['ydd'],
    install_requires=[
        'Click',
        'colorama',
        'requests',
        'six',
    ],
    entry_points={
        "console_scripts": [
            "ydd=ydd:translate",
        ]
    },
)
