from setuptools import setup
long_description = open("README.md").read()

setup(
    name='SoAuth',
    version='1.0.3',
    description='Flask middleware for SoAuth',
    url='https://github.com/sojs-coder/SoAuth-Py',
    author='SoJS',
    author_email='sojs_coder@protonmail.com',
    license='ISC',
    packages=['soauth'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=[
        'requests',
        'flask'
    ],
    zip_safe=False
)