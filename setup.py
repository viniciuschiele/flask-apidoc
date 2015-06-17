from setuptools import setup

setup(
    name='flask-apidoc',
    version='0.5.0',
    packages=['flask_apidoc'],
    url='https://github.com/viniciuschiele/flask-apidoc',
    license='Apache 2.0',
    author='Vinicius Chiele',
    author_email='vinicius.chiele@gmail.com',
    description='Adds ApiDoc support to Flask',
    keywords=['flask', 'apidoc', 'rest', 'restful'],
    install_requires=['flask>=0.10.1'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: Implementation :: CPython'
    ]
)
