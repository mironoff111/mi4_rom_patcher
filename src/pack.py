from cx_Freeze import setup, Executable   

setup(   
    name = "MIUI_patcher",   
    version = "1.0",   
    description = "MIUI v7 Mi3W/4 patcher by mironoff",   
    executables = [Executable("miui.py")])