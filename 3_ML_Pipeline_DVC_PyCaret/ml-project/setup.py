from setuptools import find_packages, setup

setup(
    name="ml_project",
    packages=find_packages(exclude=["ml_project_tests"]),
    install_requires=[
        "dagster",
        "dagster-cloud",
        "dagster-webserver",
        "mlflow==2.7.1",
        "pandas==1.5.3",
        "scikit-learn==1.3.0",
    ],
    extras_require={"dev": ["dagster-webserver", "pytest"]},
)
