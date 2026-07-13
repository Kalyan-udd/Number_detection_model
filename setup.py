from setuptools import setup, find_packages

setup(
    name="Number_recognition_model",
    version="0.0.1",
    description="This model will be used to predict a single digit number when any user write any single digit number on a space in the browser application, and then our model will make some prediction on the hand written single digit number.",
    author="Kalyan-udd",
    author_email="kalyansaiuddagiri22@gmail.com",
    url="https://github.com/Kalyan-udd/Number_detection_model.git",
    packages=find_packages(where="src"),
    package_dir={"":"src"},
)