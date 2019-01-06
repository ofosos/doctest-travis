

import setuptools

long_description = '''Example code
'''

setuptools.setup(
    name="doctest_travis",
    version="0.1",
    author="Mark Meyer",
    author_email="mark@ofosos.org",
    description="Sample code for doctesting on Travis",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ofosos/doctest-travis",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

