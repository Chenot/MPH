@echo off
cd /d "%~dp0"
call C:\ProgramData\anaconda3\Scripts\activate.bat C:\ProgramData\anaconda3\envs\psychopy_env
python main.py
