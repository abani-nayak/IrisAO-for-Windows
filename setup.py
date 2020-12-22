#--------------------------------------------------------------
# File setup.py
#
# Clement Chalumeau (SETI Institute) & Franck Marchis (Iris AO & SETI Institute)
# Date:    Apr. 20, 2016
# Modified Jun. 13, 2016
#
# used by distutils to compile the python wrapper
#--------------------------------------------------------------
#'''

from setuptools import setup,Extension
from Cython.Build import cythonize

extensions=[Extension("IrisAO_Python", [".\\DM files\\IrisAO_Python.pyx"],
                      include_dirs = [".\\DM files\\"],
                      library_dirs = [".\\DM files\\"],
                       libraries=["IrisAO.Devices"])]

setup(
    name = "irisao",
    ext_modules = cythonize(extensions),
    packages = ['DM files'],
    package_dir ={'DM files':'.\\DM files'},
    py_modules=['__init__','IrisAO_Python_MirrorControl'] 
)

#'''
'''
from setuptools.extension import Extension
from setuptools import setup, find_packages
from Cython.Distutils import build_ext

ext_modules=[
    Extension("IrisAO_Python",
              sources=["IrisAO_Python.pyx"],
              libraries=["irisao.devices.1.0.2.5"],
              library_dirs=["./"],
              include_dirs=["./"],
              language="c++"
    )
]

setup(
    name = "irisao",
    version='0.1',
    packages=find_packages(),
    license='GPL',
    author='Clement Chalumeau',
    author_email='',
    description='Modules for controlling IrisAO deformable mirror.',
    cmdclass = {"build_ext": build_ext},
    ext_modules = ext_modules,
    py_modules=['__init__','IrisAO_Python_MirrorControl']
)
'''
