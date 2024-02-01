from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = '-e .'


def gat_requirements(requirements:str)->List[str]:
    """
    This function returns the list of requirements
    """
    requirements_list = []
    with open(requirements) as file_obj:
        requirements_list = file_obj.readlines()
        requirements_list = [req.replace("\n", "") for req in requirements_list]

        if HYPHEN_E_DOT in requirements_list:
            requirements_list.remove(HYPHEN_E_DOT)

    return requirements_list


setup(
    name='ml_project',
    version='0.0.1',
    author='molcan23',
    author_email='samuel.molcan@gmail.com',
    packages=find_packages(),
    install_requirements=gat_requirements('requirements.txt')
)
