from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open('requirement.txt') as file_obj:
        requirements=file_obj.readlines()
        requirements=[req.replace('\n','')for req in requirements]

        if '-e .' in requirements:
            requirements.remove('-e .')


setup(
    name='data_science_project',
    version='0.0.1',
    author='Victor Ivan',
    author_email='victor.pilot16@gmail.com',
    package=find_packages(),
    install_requires=get_requirements('requirement.txt')#['pandas','numpy','searborn']
)