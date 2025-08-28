from setuptools import find_packages,setup

HYPHEN_E_DOT='-e .'
def get_requirements(file_path:str)->list[str]:
    '''
    this function will return the list of requirements
    
    '''
    requirements=[]
    with open(file_path) as obj_file:
        requirements=obj_file.readlines()
        requirements=[req.replace("\n"," ") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements         

setup(
    name='mlproject',
    version='0.0.1',
    author='komendra',
    author_email='sahukomendra721@gmail.com',
    packages=find_packages(),
    # install_requires=["pandas","numpy","seaborn","matplotlib"]    # not fesible to write all requirement like this so we have a different way for it
    install_requires=get_requirements("requirement.txt")
    
)