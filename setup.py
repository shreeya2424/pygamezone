import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    # The name of your package
    name="gamezone",
    
    # The version of your package
    version="0.0.1",
    
    # The project's URL and author info
    author="Shreeya Singh",
    author_email="shreeyasingh2404.com",
    description="A collection of classic Python games.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shreeya2424/pygamezone",
    
    # The main package directory
    packages=setuptools.find_packages(),
    
    # List of required dependencies
    install_requires=[
        'turtle', # For the game's graphics
    ],
    
    # Classifiers help users find your project
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha",
        "Topic :: Games/Entertainment",
    ],
    
    # Set the minimum required Python version
    python_requires='>=3.6',
)
