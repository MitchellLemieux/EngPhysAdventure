# THIS SCRIPT SHOULD BE CALLED SETUP.PY
import cx_Freeze 

executables = [cx_Freeze.Executable("EBTA.py")]

cx_Freeze.setup( 
        name = "Eng Phys Text Adventure",
        version = "0.30",
        description = "THE GREAT ENG PHYS TEXT ADVENTURE!",
        options = {"build_exe": {"packages":["pygame"]}},
        executables = executables)


#python setup.py build
#python setup.py bdist_msi

