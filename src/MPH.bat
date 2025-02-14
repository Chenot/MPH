@echo off
:: Change to the script's directory (optional if the .bat file is in the same directory)
cd %~dp0

:: Launch a new Command Prompt, activate the Conda environment, and run the Python script
%windir%\System32\cmd.exe /K "C:\ProgramData\anaconda3\Scripts\activate.bat psychopy_env & python main.py"
