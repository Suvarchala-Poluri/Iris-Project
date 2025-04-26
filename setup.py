from setuptools import setup, find_packages

setup(
    name="IrisAnalysis",
    version="1.0.0",
    author="Suvarchala poluri",
    description="A project to analyze the Iris dataset using linear regression and visualize correlations.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/YourUsername/IrisAnalysis",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "pandas==1.5.3",
        "scikit-learn==1.2.2",
        "numpy==1.24.3",
        "matplotlib==3.7.1",
        "seaborn==0.12.2"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)
