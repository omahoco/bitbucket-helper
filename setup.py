import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="bitbucket-helper",
    version="0.1.1",
    author="Cormac O'Mahony",
    author_email="cormac@omahony.id.au",
    description="A bitbucket server helper for working with lots of repos.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/omahoco/bitbucket-helper",
    packages=setuptools.find_packages(),
    scripts=['bitbucket-helper'],
    install_requires=['stashy >=0.6',
                      'pybitbucket >=0.12.0', 'PyInquirer >=1.0.3'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
