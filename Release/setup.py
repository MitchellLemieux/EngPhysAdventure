# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze 

executables = [cx_Freeze.Executable("EBTA.py")]

cx_Freeze.setup( 
        name = "Eng Phys Text Adventure",
        version = "0.30",
        description = "THE GREAT ENG PHYS TEXT ADVENTURE!",
        options = {"build_exe": {"packages":["pygame"]}},
        executables = executables)




### Use this to run a build folder
#python setup.py build
### Use this to make an installer in dist folder
#python setup.py bdist_msi
