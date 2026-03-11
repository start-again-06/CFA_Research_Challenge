from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="cfa_research_challenge_project",
    version="1.0.0",
    author="Anjan Mahapatra",
    author_email="anjanmahapatra10@gmail.com",
    description="Institutional-grade equity research and valuation system inspired by CFA Research Challenge reports",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/start-again-06/CFA_Research_Challenge",

    packages=find_packages(exclude=["tests*", "notebooks*"]),

    python_requires=">=3.9",

    install_requires=[
        "numpy>=1.23",
        "pandas>=1.5",
        "matplotlib>=3.7",
        "seaborn>=0.12",
        "scipy>=1.10",
        "scikit-learn>=1.3",
        "statsmodels>=0.14",
        "yfinance>=0.2",
        "pyyaml>=6.0",
        "reportlab>=4.0"
    ],

    extras_require={
        "dev": [
            "pytest",
            "black",
            "flake8"
        ]
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Office/Business :: Financial :: Investment",
        "Topic :: Scientific/Engineering :: Artificial Intelligence"
    ],

    entry_points={
        "console_scripts": [
            "cfa-research=main:main"
        ]
    },

    include_package_data=True,
    zip_safe=False
)
