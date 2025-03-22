from setuptools import setup, find_packages

setup(
    name="dsnlp-utils",
    version="0.1.2",
    packages=find_packages(),
    install_requires=[
        "nltk"
    ],
    author="Dnyanesh",
    description="A simple wrapper around NLTK for tokenization, POS tagging, and lemmatization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/dnyanesh-github/nlp_utils",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Topic :: Text Processing :: Linguistic"
    ],
    python_requires=">=3.7",
    include_package_data=True,
)

