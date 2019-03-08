import cx_Freeze

executables = [cx_freeze.Executable("EngPhysAdventure Alpha v0.28")]

cx_freeze.setup(
    name="EPTA",
    #include includes
    options={"build_exe":{"packages":["pygame"],
                          "included_files":[]}}, #include included files
    executables = executables
    )
