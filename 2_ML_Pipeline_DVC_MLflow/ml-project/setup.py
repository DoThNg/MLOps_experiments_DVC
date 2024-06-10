from setuptools import find_packages, setup

setup(
    name="ml_project",
    packages=find_packages(exclude=["ml_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-webserver==1.5.1",
        "mlflow==~> 2.8.1",
        "pandas==2.1.1",
        "matplotlib==3.8.0",
        "scikit-learn==1.3.1",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
