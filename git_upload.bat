@echo off
REM Change directory to the folder where this script is located
cd /d "%~dp0"

echo Staging all changes...
git add .

echo.
echo Enter your commit message:
set /p commitMessage=

REM Commit with the provided message
git commit -m "%commitMessage%"

echo.
echo Pushing branch "test" to GitHub (origin)...
git push -u origin test

echo.
echo Pushing branch "test" to GitLab (gitlab)...
git push -u gitlab test

echo.
echo All done!
pause
