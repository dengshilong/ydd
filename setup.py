from setuptools import setup, find_packages

setup(
    name='ydd',
    version='0.1',
    author='dengshilong',
    author_email='dengshilong1988@gmail.com',
    description="python youdao dict terminal",
    keywords="python youdao dict terminal",
    url='https://github.com/dengshilong/ydd',
    zip_safe=False,
    py_modules=['ydd'],
    install_requires=[
        'Click',
        'colorama',
        'requests',
    ],
    entry_points={
        "console_scripts": [
            "ydd=ydd:translate",
        ]
    },
)