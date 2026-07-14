from setuptools import setup, find_packages


list_of_packages = []
with open("requirements.txt", "r") as requirements:
    requirement_packages = requirements.read()
    for packages in requirement_packages:
        if "-e ." not in packages:
            list_of_packages.append(packages)

setup(
    name="Numbers_recognition",
    author="Kalyan-udd",
    author_email="kalyansaiuddagiri22@gmail.com",
    version="0.0.1",
    url="https://github.com/Kalyan-udd/Number_detection_model",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
    description="Using this model we can predict the number that is drawn in the webpage using a basic sequential neural network trained on the famous mnist dataset.",
)