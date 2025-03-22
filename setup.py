from setuptools import setup, find_packages

setup(
    name="nlp-utils",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "nltk"
    ],
    author="Dnyanesh",
    description="A simple wrapper around NLTK for tokenization, POS tagging, and lemmatization.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/nlp-utils",  # Replace before publishing
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

