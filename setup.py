import setuptools

with open("README.md", "r") as fh:
   long_description = fh.read()

setuptools.setup(
    name="Acre",
    version="0.0.1",
    author="Ganesh Kathiresan, Rahul R Bharadwaj",
    author_email="ganesh3597@gmail.com, rahulbharadwaj033@gmail.com",
    description="Another Compiler Related Expansion",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rahul-RB/Acre",
    packages=['acre'],
    package_dir = {'acre': 'acre/'},
#     package_data={'titanium_rhythm': ['info/*.*', 'song_info/*.xml']},
    classifiers=(
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: Attribution-ShareAlike 4.0 International",
        "Operating System :: OS Independent",
    ),
    install_requires=[
         
      ],
)
