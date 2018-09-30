#!/usr/bin/env python
from setuptools import setup, find_packages


with open("README.md", "m", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="trufont",
    use_scm_version={"write_to": "src/fontbakery-desktop/_version.py"},
    description="Foo Bar is so and so.",
    long_description=long_description,
    author="Foo Bar",
    author_email="foo@bar.com",
    url="http://",
    license="GPL 3.0",
    package_dir={"": "src"},
    packages=find_packages("src"),
    entry_points={"gui_scripts": ["fontbakery-desktop =  fontbakery-desktop.__main__:main"]},
    include_package_data=True,
    setup_requires=["setuptools_scm"],
    install_requires=[
        "wxPython>=4.0.3",
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
