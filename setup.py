from setuptools import setup

setup(
    name='soauth',
    version='1.0.0',
    description='Flask middleware for SoAuth',
    url='https://github.com/username/soauth',
    author='Your Name',
    author_email='your.email@example.com',
    license='MIT',
    packages=['soauth'],
    install_requires=[
        'requests',
        'flask'
    ],
    zip_safe=False
)
