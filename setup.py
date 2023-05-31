from setuptools import setup, find_packages
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements_list(filepath:str) -> List[str]:
    """
    This function will return list of requirements
    """
    requirement_list = []
    with open(filepath) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [i.replace ('\n','') for i in requirement_list]
        
        if HYPEN_E_DOT in requirement_list:
            requirement_list.remove(HYPEN_E_DOT)

setup(name='ml_pipeline',
      version='0.0.1',
      description='machine learning pipeline project',
      author='Bharatbhushan',
      author_email='aiwalabro@gmail.com',
      packages=find_packages(),
      install_requires=get_requirements_list('requirements.txt')
      
     )