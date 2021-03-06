from setuptools import setup, find_packages

setup(
    name="python-hsmath",
    version="0.1.0",
    author="ysk.univ.1007@gmail.com",
    url="https://github.com/yskuniv/python-hsmath",
    packages=find_packages(),
    python_requires='>=3.8, <4',
    install_requires=[
    ],
    extras_require={
        'lint': [
            'flake8',
        ],
        'test': [
        ],
        'dev': [
            'autopep8',
            'rope',
        ],
    },
)
