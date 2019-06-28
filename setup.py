import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="ssh_multitunnel",
    version="0.0.1",
    author="Dvir Rassovsky",
    author_email="dviros7@gmail.com",
    description="Create ssh tunnels with multiple hops",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dvir42/ssh_multitunnel",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
