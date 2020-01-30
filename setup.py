#!/usr/bin/env python
from setuptools import setup, find_packages

long_description = "A graphical user interface for running FontBakery quality assurance checks for fonts."

setup(
    name="FontBakery-Desktop",
    use_scm_version={"write_to": "src/fontbakery-desktop/_version.py"},
    long_description=long_description,
    author="Felipe Sanches",
    author_email="juca@members.fsf.org",
    url="http://github.com/felipesanches/fontbakery-desktop",
    license="GPL 3.0",
    package_dir={"": "."},
    packages=find_packages("."),
    entry_points={"gui_scripts": ["fontbakery-desktop =  fontbakery-desktop.__main__:main"]},
    include_package_data=True,
    setup_requires=["setuptools_scm"],
    install_requires=[
        "fontbakery",
        "PyQtWebEngine"
    ],
    platforms=["Win32", "Mac OS X", "Linux"],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
        "Operating System :: POSIX :: Linux",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Intended Audience :: End Users/Desktop",
        "Topic :: Text Processing :: Fonts",
        "Topic :: Multimedia :: Graphics",
        "License :: OSI Approved",
    ],
    # test_suite="tests",
)
