import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="csgo-menu-maker",
    version="0.2.4",
    author="Citrus",
    author_email="address@example.com",
    description="Make cool-looking menus in CSGO consoles",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/citrusCS/csgo-menu-maker",
    packages=setuptools.find_packages(),
    entry_points={'console_scripts': ['csgo-menu-maker=csgomenumaker:__main__']},
    install_requires=['pyyaml'],
    classifiers=[
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3 :: Only",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
