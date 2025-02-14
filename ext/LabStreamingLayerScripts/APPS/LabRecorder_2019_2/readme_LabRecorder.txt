**INSTALLING LSL LABRECORDER ON WINDOWS**

0. Before installing:
- Check liblsl is built from source (if not process can be done by following the steps at https://github.com/sccn/labstreaminglayer/wiki/INSTALL)
- Check CMake is installed on Windows (tested with v3.14.4)
- Check Qt is installed on Windows (tested with v5.12.1)
- Check Microsoft Visual Studio (or Visual C++ Build Tools) is installed (tested with VS2015, recommended). If not, follow the steps on the previous link to install Visual Studio.
- Download LabRecorder source code from the LSL repository (https://github.com/labstreaminglayer/App-LabRecorder.git). Include it in the LSL source tree (recommended).
- Optional: Boost for enabling xdfz support.

1. Run CMake from GUI/command line
- Create a build directory inside the LabRecorder directory

- OPTION 1: Using CMake GUI:
 - Select source code location.
 - Select build directory.
 - Press 'Configure'. A new window will appear.
 - Select the Generator depending on the MSVC version.
 - In the 'Optional Platform for Generator' field, select or type 'x64' (without quotation marks).
 - Press 'Finish'.
 - If an error regarding the location of the Qt5 installation appears, specify manually the location of the Qt5 directory (example: C:\Qt\5.12.1\msvc2015_64\lib\cmake\Qt5). Press 'Configure' again.

- OPTION 2: Using command line:
 - In the Windows command line, go to the build directory of LabRecorder
 - Run cmake with commandline options. Add/remove/modify options as required (example with xdfz support: cmake .. -G "Visual Studio 14 2015 Win64" -DQt5_DIR=C:\Qt\5.12.1\msvc2015_64\lib\cmake\Qt5 -DBOOST_ROOT=C:\local\boost_1_65_1 -DLSLAPPS_LabRecorder=ON -DLSLAPPS_XDFBrowser=ON -DLSLAPPS_OpenVR=ON). 

2. Build project
- OPTION 1: Using MSVC
 - Still in CMake, press 'Open Project'. Visual Studio will open.
 - In the Visual Studio IDE, go to the solution configuration pull-down menu (normally in the top bar of the GUI, where it says 'Debug') and change from 'Debug' to 'Release'.
 - In the solution explorer, right click on INSTALL and click build.

- OPTION 2: Using command line
 - cmake --build . --config Release --target install

3. Open LabRecorder
- If build has been successful, go to the LabRecorder directory -> build -> install -> LabRecorder -> LabRecorder.exe. Program should open successfully!