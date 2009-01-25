from setuptools import setup, find_packages
 
version = '0.5'
 
LONG_DESCRIPTION = """

"""
 
setup(
    name='django-swaps',
    version=version,
    description="django-swaps",
    long_description=LONG_DESCRIPTION,
    classifiers=[
        "Programming Language :: Python",
        "Topic :: Other/Nonlisted Topic",
        "Framework :: Django",
        "Environment :: Web Environment",
    ],
    keywords='swaps,pinax,django',
    author='Bob Haugen',
    author_email='bob.haugen@gmail.com',
    url='http://django-swaps.googlecode.com/',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['setuptools'],
)