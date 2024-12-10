from setuptools import setup, find_packages

setup(
    name="SigProfilerToolkit",
    version="0.1.0",
    description="Unified toolkit for mutational signature analysis",
    author="Mark Barnes",
    author_email="mdbarnes@health.ucsd.edu",
    url="https://github.com/mdbarnesUCSD/SigProfilerToolkit",
    packages=find_packages(),
    py_modules=["SigProfilerToolkit"],
    entry_points={
        "console_scripts": [
            "SigProfilerToolkit=SigProfilerToolkit:main",
        ],
    },
    install_requires=[
        "SigProfilerMatrixGenerator==1.2.31",
        "SigProfilerPlotting==1.3.24",
        "SigProfilerAssignment==0.1.9",
        # "SigProfilerExtractor==1.1.25", # Do not include in early development testing
    ],
)
