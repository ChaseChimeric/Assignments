from cx_Freeze import setup, Executable
setup(name = 'ExecutablePy' ,
	version = '0.1' ,
	description = 'nay' ,
	executables = [Executable('a07.py')]
	)
