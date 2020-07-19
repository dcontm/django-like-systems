import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="django-like-systems", # Replace with your own username
    version="0.0.1",
    author="Dmitry Konstantinov",
    author_email="dcontm@gmail.com",
    description="An easy way to add feedback"
                + "'like/dislike' to any of your models.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/dcontm/django-like-system",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Framework :: Django",
        "Framework :: Django :: 2.2",
        "Framework :: Django :: 3.0",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires='>=3.6',
    install_requires=["Django>=3.0"],
)
