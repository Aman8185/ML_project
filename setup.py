from setuptools import find_packages, setup, Require
from typing import List

def get_requirements(file_path:str)->List[str]:
    '''
    this function will restur the list of all requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n',"") for req in requirements]
    return requirements


setup(
    name='ml_project',
    version='0.0.1',
    author='aman',
    author_email='upadhyay1.aman@gmail.com',
    install_requires=get_requirements('requirement.txt')
)


