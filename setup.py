import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csgo-menu-maker",
    version="0.2.0",
    author="Citrus",
    author_email="address@example.com",
    description="Make cool-looking menus in CSGO consoles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/citrusCS/csgo-menu-maker",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
