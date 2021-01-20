import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="mccalc-Tomodachi49", # Replace with your own username
    version="0.0.1",
    author="Tomodachi94",
    author_email="tomodachi94@pm.me",
    description="Minecraft-related math functions, in an API or GUI.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Tomodachi94/mccalc",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)