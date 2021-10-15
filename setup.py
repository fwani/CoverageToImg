import setuptools

setuptools.setup(
    name="coverage_to_png",
    url="https://github.com/fwani/CoverageToPNG",
    version="0.0.1",
    author="fwani",
    author_email="seungfwani@gmail.com",
    description="This is a tool for converting coverage.json to png image.",
    long_description= open("README.md", "r").read(),
    long_description_content_type="text/markdown",
    packages=setuptools.find_packages(exclude=['tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
)
