from setuptools import setup, find_packages

def getting_dependencies():
    with open("requirements.txt", "r", encoding="utf-8") as f:
        requirements = []
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and not line.startswith("-e ."):
                requirements.append(line)
    return requirements

setup(
    name="Number_recognition",
    author="Kalyan-udd",
    author_email="kalyansaiuddagiri22@gmail.com",
    version="0.0.1",
    url="https://github.com/Kalyan-udd/Number_detection_model.git",
    packages=find_packages("src"),
    install_requires=getting_dependencies(),
    python_requires=">=3.13",
    package_dir={"":"src"} 
)