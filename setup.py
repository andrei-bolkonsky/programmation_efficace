from setuptools import setup, find_packages

setup(
    name="programmation_efficace", # Replace with your own username
    version="0.0.1",
    author="Victor Cumer",
    author_email="victor.cumer@gmail.com",
    description="Python application of the algorithms explaned in Christoph Dürr and Jill-Jênn Vie's book: programmation efficace",
    url="https://github.com/andrei-bolkonsky/programmation_efficace",
    packages=find_packages("src"),
    package_dir={'': 'src'},
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
    tests_require=[
        "pytest==6.2.2"
    ]
)
