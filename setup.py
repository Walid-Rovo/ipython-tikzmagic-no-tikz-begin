from setuptools import setup

classifiers = [
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.8",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: BSD License",
    "Topic :: Scientific/Engineering :: Visualization",
    "Topic :: Software Development :: Libraries",
    "Topic :: Utilities",
    "Framework :: IPython",
]

with open("README.md", "r") as fp:
    long_description = fp.read()

__author__ = "Walid Ismail (Original Author: Michael Kraus)"
__version__ = "0.2.0"

setup(
    name="ipython-tikzmagic",
    version=__version__,
    author=__author__,
    url="https://github.com/Walid-Rovo/ipython-tikzmagic-no-tikz-begin",
    py_modules=["tikzmagic"],
    description="IPython magics for generating figures with TikZ without an implicit inclusion"
                "of `\begin{tikzpicture[...]}`, which allows greater flexibility of the latex "
                "code (e.g. using `\tikzset` before `\begin{tikzpicture}`)",
    long_description=long_description,
    license="BSD",
    classifiers=classifiers,
    install_requires=[
        "ipython",
        "Pillow",
        "PyMuPDF",
    ],
    python_requires=">=3.8",
)
