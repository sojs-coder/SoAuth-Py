from setuptools import setup

setup(
    name='soauth',
    version='1.0.0',
    description='Flask middleware for SoAuth',
    url='https://github.com/sojs-coder/SoAuth-Py',
    author='Your Name',
    author_email='sojs_coder@protonmail.com',
    license='ISC',
    packages=['soauth'],
    install_requires=[
        'requests',
        'flask'
    ],
    zip_safe=False
)