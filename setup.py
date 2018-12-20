from setuptools import setup

setup(
    install_requires=["boto3","tabulate"],
    entry_points={
        "console_scripts": [
            "iamrolelist = iam_role_id:main"
        ]
    }
)
