#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on juin 20, 2024, at 15:28
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

# --- Import packages ---
from psychopy import locale_setup
from psychopy import prefs
from psychopy import plugins
plugins.activatePlugins()
prefs.hardware['audioLib'] = 'ptb'
prefs.hardware['audioLatencyMode'] = '3'
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout, hardware
from psychopy.tools import environmenttools
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER, priority)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

# Run 'Before Experiment' code from language
# Check if expInfo exists and create the language variable
if 'expInfo' not in globals():
    expInfo = {}

# Set default values to English if it is missing from expInfo keys
if 'language' not in expInfo:
    expInfo['language'] = 'English'

# Create the language variable
language = expInfo.get('language')

# Define instructions based on the selected language
if language == "English":
    instructions = {
        'Text_instructions1': (
            "Welcome to the Mental Rotation Task.\n\n"
            "You will see an image of two objects on the screen. They can be the same object, but rotated, or they can be different objects. For each pair, indicate if they are the same object but rotated, or if they are different objects.\n\n"
            "Press 'd' if they are different. Press 'k' if they are the same.\n\n"
            "Now an example image with the correct answer will follow. After that, the experiment will start.\n\n"
            "Whenever you're ready, press the spacebar to continue."
        ),
        'Text_instructions2': (
            "Here, you can see that the object on the right is not the object on the left but rotated, it is a different object.\nThey would still be different after mentally rotating them to line up.\n"
            "Here you would press 'd' for different. If they were the same, you would press 'k'.\n"
            "Try to respond as accurately as you can. Also try to be fast, but emphasize being accurate.\n\n"
            "Press the spacebar to start the experiment."
        ),
        'Text_puzzle': "Puzzle ",
        'Text_keys': "press 'd' for different         press 'k' for same",
        'Text_end_task': (
            "This task is now completed.\n\n"
            "Press the space bar to end the task\n\n"
        )
    }
else:  # Default to French if any issues
    instructions = {
        'Text_instructions1': (
            "Bienvenue dans la tâche de Rotation Mentale.\n\n"
            "Vous allez voir des images de deux objets à l'écran. Ils peuvent être le même objet, mais tournés, ou ils peuvent être différents. Pour chaque paire, indiquez s'ils sont le même objet mais tournés, ou s'ils sont différents.\n\n"
            "Appuyez sur 'd' s'ils sont différents. Appuyez sur 'k' s'ils sont les mêmes.\n\n"
            "Une image d'exemple avec la réponse correcte va suivre. Après cela, l'expérience commencera.\n\n"
            "Appuyez sur la barre d'espace pour continuer."
        ),
        'Text_instructions2': (
            "Ici, vous pouvez voir que l'objet à droite n'est pas l'objet à gauche mais tourné, c'est un objet différent.\nIls seraient toujours différents après les avoir mentalement tournés pour les aligner.\n"
            "Ici, vous appuieriez sur 'd' pour différent. S'ils étaient les mêmes, vous appuieriez sur 'k'.\n"
            "Essayez de répondre aussi précisément que possible. Essayez également d'être rapide, mais mettez l'accent sur la précision.\n\n"
            "Appuyez sur la barre d'espace pour commencer l'expérience."
        ),
        'Text_puzzle': "Puzzle ",
        'Text_keys': "appuyez sur 'd' pour différent         appuyez sur 'k' pour identique",
        'Text_end_task': (
            "Cette tâche est maintenant complétée.\n\n"
            "Appuyez sur la barre d'espace pour terminer la tâche\n\n"
        )
    }

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'MentalRotationFinal'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': '',
    'session': '001',
    'date|hid': data.getDateStr(),
    'expName|hid': expName,
    'psychopyVersion|hid': psychopyVersion,
}

# --- Define some variables which will change depending on pilot mode ---
'''
To run in pilot mode, either use the run/pilot toggle in Builder, Coder and Runner, 
or run the experiment with `--pilot` as an argument. To change what pilot 
#mode does, check out the 'Pilot mode' tab in preferences.
'''
# work out from system args whether we are running in pilot mode
PILOTING = core.setPilotModeFromArgs()
# start off with values from experiment settings
_fullScr = True
_winSize = [2560, 1440]
_loggingLevel = logging.getLevel('exp')
# if in pilot mode, apply overrides according to preferences
if PILOTING:
    # force windowed mode
    if prefs.piloting['forceWindowed']:
        _fullScr = False
        # set window size
        _winSize = prefs.piloting['forcedWindowSize']
    # override logging level
    _loggingLevel = logging.getLevel(
        prefs.piloting['pilotLoggingLevel']
    )

def showExpInfoDlg(expInfo):
    """
    Show participant info dialog.
    Parameters
    ==========
    expInfo : dict
        Information about this experiment.
    
    Returns
    ==========
    dict
        Information about this experiment.
    """
    # show participant info dialog
    dlg = gui.DlgFromDict(
        dictionary=expInfo, sortKeys=False, title=expName, alwaysOnTop=True
    )
    if dlg.OK == False:
        core.quit()  # user pressed cancel
    # return expInfo
    return expInfo


def setupData(expInfo, dataDir=None):
    """
    Make an ExperimentHandler to handle trials and saving.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    dataDir : Path, str or None
        Folder to save the data to, leave as None to create a folder in the current directory.    
    Returns
    ==========
    psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    # remove dialog-specific syntax from expInfo
    for key, val in expInfo.copy().items():
        newKey, _ = data.utils.parsePipeSyntax(key)
        expInfo[newKey] = expInfo.pop(key)
    
    # data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
    if dataDir is None:
        dataDir = _thisDir
    filename = u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])
    # make sure filename is relative to dataDir
    if os.path.isabs(filename):
        dataDir = os.path.commonprefix([dataDir, filename])
        filename = os.path.relpath(filename, dataDir)
    
    # an ExperimentHandler isn't essential but helps with data saving
    thisExp = data.ExperimentHandler(
        name=expName, version='',
        extraInfo=expInfo, runtimeInfo=None,
        originPath='D:\\Google Drive\\Professionnel\\3_Post-doc_ISAE-MPH\\Experience_MPH\\project\\code\\PsychopyTasks\\Mentalrotation\\MentalRotationFinal_lastrun.py',
        savePickle=True, saveWideText=True,
        dataFileName=dataDir + os.sep + filename, sortColumns='time'
    )
    thisExp.setPriority('thisRow.t', priority.CRITICAL)
    thisExp.setPriority('expName', priority.LOW)
    # return experiment handler
    return thisExp


def setupLogging(filename):
    """
    Setup a log file and tell it what level to log at.
    
    Parameters
    ==========
    filename : str or pathlib.Path
        Filename to save log file and data files as, doesn't need an extension.
    
    Returns
    ==========
    psychopy.logging.LogFile
        Text stream to receive inputs from the logging system.
    """
    # this outputs to the screen, not a file
    logging.console.setLevel(_loggingLevel)
    # save a log file for detail verbose info
    logFile = logging.LogFile(filename+'.log', level=_loggingLevel)
    
    return logFile


def setupWindow(expInfo=None, win=None):
    """
    Setup the Window
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    win : psychopy.visual.Window
        Window to setup - leave as None to create a new window.
    
    Returns
    ==========
    psychopy.visual.Window
        Window in which to run this experiment.
    """
    if PILOTING:
        logging.debug('Fullscreen settings ignored as running in pilot mode.')
    
    if win is None:
        # if not given a window to setup, make one
        win = visual.Window(
            size=_winSize, fullscr=_fullScr, screen=0,
            winType='pyglet', allowStencil=False,
            monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [0,0,0]
        win.colorSpace = 'rgb'
        win.backgroundImage = ''
        win.backgroundFit = 'none'
        win.units = 'height'
    if expInfo is not None:
        # get/measure frame rate if not already in expInfo
        if win._monitorFrameRate is None:
            win.getActualFrameRate(infoMsg='Attempting to measure frame rate of screen, please wait...')
        expInfo['frameRate'] = win._monitorFrameRate
    win.mouseVisible = False
    win.hideMessage()
    # show a visual indicator if we're in piloting mode
    if PILOTING and prefs.piloting['showPilotingIndicator']:
        win.showPilotingIndicator()
    
    return win


def setupDevices(expInfo, thisExp, win):
    """
    Setup whatever devices are available (mouse, keyboard, speaker, eyetracker, etc.) and add them to 
    the device manager (deviceManager)
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window in which to run this experiment.
    Returns
    ==========
    bool
        True if completed successfully.
    """
    # --- Setup input devices ---
    ioConfig = {}
    
    # Setup iohub keyboard
    ioConfig['Keyboard'] = dict(use_keymap='psychopy')
    
    ioSession = '1'
    if 'session' in expInfo:
        ioSession = str(expInfo['session'])
    ioServer = io.launchHubServer(window=win, **ioConfig)
    # store ioServer object in the device manager
    deviceManager.ioServer = ioServer
    
    # create a default keyboard (e.g. to check for escape)
    if deviceManager.getDevice('defaultKeyboard') is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='iohub'
        )
    if deviceManager.getDevice('helloKey') is None:
        # initialise helloKey
        helloKey = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='helloKey',
        )
    if deviceManager.getDevice('exampKey') is None:
        # initialise exampKey
        exampKey = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='exampKey',
        )
    if deviceManager.getDevice('trialResp') is None:
        # initialise trialResp
        trialResp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='trialResp',
        )
    if deviceManager.getDevice('end_task') is None:
        # initialise end_task
        end_task = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='end_task',
        )
    # return True if completed successfully
    return True

def pauseExperiment(thisExp, win=None, timers=[], playbackComponents=[]):
    """
    Pause this experiment, preventing the flow from advancing to the next routine until resumed.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    timers : list, tuple
        List of timers to reset once pausing is finished.
    playbackComponents : list, tuple
        List of any components with a `pause` method which need to be paused.
    """
    # if we are not paused, do nothing
    if thisExp.status != PAUSED:
        return
    
    # pause any playback components
    for comp in playbackComponents:
        comp.pause()
    # prevent components from auto-drawing
    win.stashAutoDraw()
    # make sure we have a keyboard
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        defaultKeyboard = deviceManager.addKeyboard(
            deviceClass='keyboard',
            deviceName='defaultKeyboard',
            backend='ioHub',
        )
    # run a while loop while we wait to unpause
    while thisExp.status == PAUSED:
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=['escape']):
            endExperiment(thisExp, win=win)
        # flip the screen
        win.flip()
    # if stop was requested while paused, quit
    if thisExp.status == FINISHED:
        endExperiment(thisExp, win=win)
    # resume any playback components
    for comp in playbackComponents:
        comp.play()
    # restore auto-drawn components
    win.retrieveAutoDraw()
    # reset any timers
    for timer in timers:
        timer.reset()


def run(expInfo, thisExp, win, globalClock=None, thisSession=None):
    """
    Run the experiment flow.
    
    Parameters
    ==========
    expInfo : dict
        Information about this experiment, created by the `setupExpInfo` function.
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    psychopy.visual.Window
        Window in which to run this experiment.
    globalClock : psychopy.core.clock.Clock or None
        Clock to get global time from - supply None to make a new one.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    # mark experiment as started
    thisExp.status = STARTED
    # make sure variables created by exec are available globally
    exec = environmenttools.setExecEnvironment(globals())
    # get device handles from dict of input devices
    ioServer = deviceManager.ioServer
    # get/create a default keyboard (e.g. to check for escape)
    defaultKeyboard = deviceManager.getDevice('defaultKeyboard')
    if defaultKeyboard is None:
        deviceManager.addDevice(
            deviceClass='keyboard', deviceName='defaultKeyboard', backend='ioHub'
        )
    eyetracker = deviceManager.getDevice('eyetracker')
    # make sure we're running in the directory for this experiment
    os.chdir(_thisDir)
    # get filename from ExperimentHandler for convenience
    filename = thisExp.dataFileName
    frameTolerance = 0.001  # how close to onset before 'same' frame
    endExpNow = False  # flag for 'escape' or other condition => quit the exp
    # get frame duration from frame rate in expInfo
    if 'frameRate' in expInfo and expInfo['frameRate'] is not None:
        frameDur = 1.0 / round(expInfo['frameRate'])
    else:
        frameDur = 1.0 / 60.0  # could not measure, so guess
    
    # Start Code - component code to be run after the window creation
    
    # --- Initialize components for Routine "init" ---
    # Run 'Begin Experiment' code from LSL
    import socket
    import json
    import threading
    from pylsl import local_clock
    
    # Function to send markers to the LSL server
    def send_marker(marker):
        event = {
            'marker': marker,
            'timestamp': local_clock()
        }
        message = json.dumps(event)
        
        def send():
            try:
                # Connect to the socket server and send the marker with a timeout
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.settimeout(0.1)  # Set timeout to 100 milliseconds
                client_socket.connect(('localhost', 5000))
                client_socket.sendall(message.encode('utf-8'))
                client_socket.close()
            except (ConnectionRefusedError, socket.timeout):
                print("LSL server is not running or connection timed out. Continuing without sending marker.")
        
        # Create and start a thread to send the marker
        send_thread = threading.Thread(target=send)
        send_thread.start()
    
    # Run 'Begin Experiment' code from ActivateWindow
    win.winHandle.activate()  # Ensure the PsychoPy window is the primary window
    
    
    # --- Initialize components for Routine "Instruction1" ---
    helloText = visual.TextStim(win=win, name='helloText',
        text="Welcome. \n\nYou will see an image of two objects on the screen. They can be the same object, but rotated, or they can be different objects. For each pair, indicate if they are the same object but rotated, or if they are different objects.\n\nPress 'd' if they are different. Press 's' if they are the same.   \n\nNow an example image with the correct answer will follow. After that, the experiment will start.\n\nWhenever you're ready, press the 's' to continue.",
        font='Arial',
        units='height', pos=[0, 0], height=0.035, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    helloKey = keyboard.Keyboard(deviceName='helloKey')
    
    # --- Initialize components for Routine "Instruction2" ---
    exampText = visual.TextStim(win=win, name='exampText',
        text=None,
        font='Arial',
        pos=[0, -0.25], height=0.033, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    exampKey = keyboard.Keyboard(deviceName='exampKey')
    exampIm = visual.ImageStim(
        win=win,
        name='exampIm', units='height', 
        image='ressources/i43_0_R.jpg', mask=None, anchor='center',
        ori=0, pos=[0.0, 0.15], size=[0.5,0.35],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "Trial" ---
    trialStimulus = visual.ImageStim(
        win=win,
        name='trialStimulus', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0, 0], size=[0.7, 0.5],
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    textKeys = visual.TextStim(win=win, name='textKeys',
        text=None,
        font='Arial',
        pos=[0, -0.4], height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    textPuzzle = visual.TextStim(win=win, name='textPuzzle',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    trialResp = keyboard.Keyboard(deviceName='trialResp')
    
    # --- Initialize components for Routine "end" ---
    InstructionsText4 = visual.TextStim(win=win, name='InstructionsText4',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    end_task = keyboard.Keyboard(deviceName='end_task')
    
    # create some handy timers
    
    # global clock to track the time since experiment started
    if globalClock is None:
        # create a clock if not given one
        globalClock = core.Clock()
    if isinstance(globalClock, str):
        # if given a string, make a clock accoridng to it
        if globalClock == 'float':
            # get timestamps as a simple value
            globalClock = core.Clock(format='float')
        elif globalClock == 'iso':
            # get timestamps in ISO format
            globalClock = core.Clock(format='%Y-%m-%d_%H:%M:%S.%f%z')
        else:
            # get timestamps in a custom format
            globalClock = core.Clock(format=globalClock)
    if ioServer is not None:
        ioServer.syncClock(globalClock)
    logging.setDefaultClock(globalClock)
    # routine timer to track time remaining of each (possibly non-slip) routine
    routineTimer = core.Clock()
    win.flip()  # flip window to reset last flip timer
    # store the exact time the global clock started
    expInfo['expStart'] = data.getDateStr(
        format='%Y-%m-%d %Hh%M.%S.%f %z', fractionalSecondDigits=6
    )
    
    # --- Prepare to start Routine "init" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('init.started', globalClock.getTime(format='float'))
    # keep track of which components have finished
    initComponents = []
    for thisComponent in initComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "init" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        # Run 'Each Frame' code from DeactivateMouse
        event.Mouse(visible=False)
        
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in initComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "init" ---
    for thisComponent in initComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('init.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "init" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction1.started', globalClock.getTime(format='float'))
    helloKey.keys = []
    helloKey.rt = []
    _helloKey_allKeys = []
    # Run 'Begin Routine' code from code_helloText
    helloText.setText(instructions['Text_instructions1'])
    
    # Run 'Begin Routine' code from LSL_MRT_start
    send_marker('MRT_start')
    # keep track of which components have finished
    Instruction1Components = [helloText, helloKey]
    for thisComponent in Instruction1Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *helloText* updates
        
        # if helloText is starting this frame...
        if helloText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            helloText.frameNStart = frameN  # exact frame index
            helloText.tStart = t  # local t and not account for scr refresh
            helloText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(helloText, 'tStartRefresh')  # time at next scr refresh
            # update status
            helloText.status = STARTED
            helloText.setAutoDraw(True)
        
        # if helloText is active this frame...
        if helloText.status == STARTED:
            # update params
            pass
        
        # *helloKey* updates
        waitOnFlip = False
        
        # if helloKey is starting this frame...
        if helloKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            helloKey.frameNStart = frameN  # exact frame index
            helloKey.tStart = t  # local t and not account for scr refresh
            helloKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(helloKey, 'tStartRefresh')  # time at next scr refresh
            # update status
            helloKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(helloKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(helloKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if helloKey.status == STARTED and not waitOnFlip:
            theseKeys = helloKey.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _helloKey_allKeys.extend(theseKeys)
            if len(_helloKey_allKeys):
                helloKey.keys = _helloKey_allKeys[-1].name  # just the last key pressed
                helloKey.rt = _helloKey_allKeys[-1].rt
                helloKey.duration = _helloKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction1" ---
    for thisComponent in Instruction1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction1.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "Instruction2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction2.started', globalClock.getTime(format='float'))
    exampKey.keys = []
    exampKey.rt = []
    _exampKey_allKeys = []
    # Run 'Begin Routine' code from code_exampText
    exampText.setText(instructions['Text_instructions2'])
    
    # keep track of which components have finished
    Instruction2Components = [exampText, exampKey, exampIm]
    for thisComponent in Instruction2Components:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "Instruction2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *exampText* updates
        
        # if exampText is starting this frame...
        if exampText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exampText.frameNStart = frameN  # exact frame index
            exampText.tStart = t  # local t and not account for scr refresh
            exampText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exampText, 'tStartRefresh')  # time at next scr refresh
            # update status
            exampText.status = STARTED
            exampText.setAutoDraw(True)
        
        # if exampText is active this frame...
        if exampText.status == STARTED:
            # update params
            pass
        
        # *exampKey* updates
        waitOnFlip = False
        
        # if exampKey is starting this frame...
        if exampKey.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exampKey.frameNStart = frameN  # exact frame index
            exampKey.tStart = t  # local t and not account for scr refresh
            exampKey.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exampKey, 'tStartRefresh')  # time at next scr refresh
            # update status
            exampKey.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(exampKey.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(exampKey.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if exampKey.status == STARTED and not waitOnFlip:
            theseKeys = exampKey.getKeys(keyList=['space'], ignoreKeys=["escape"], waitRelease=False)
            _exampKey_allKeys.extend(theseKeys)
            if len(_exampKey_allKeys):
                exampKey.keys = _exampKey_allKeys[-1].name  # just the last key pressed
                exampKey.rt = _exampKey_allKeys[-1].rt
                exampKey.duration = _exampKey_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *exampIm* updates
        
        # if exampIm is starting this frame...
        if exampIm.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            exampIm.frameNStart = frameN  # exact frame index
            exampIm.tStart = t  # local t and not account for scr refresh
            exampIm.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(exampIm, 'tStartRefresh')  # time at next scr refresh
            # update status
            exampIm.status = STARTED
            exampIm.setAutoDraw(True)
        
        # if exampIm is active this frame...
        if exampIm.status == STARTED:
            # update params
            pass
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in Instruction2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "Instruction2" ---
    for thisComponent in Instruction2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('Instruction2.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_test
    send_marker("start_test")
    thisExp.nextEntry()
    # the Routine "Instruction2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    loop = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('mentalrotationstimuli.csv'),
        seed=None, name='loop')
    thisExp.addLoop(loop)  # add the loop to the experiment
    thisLoop = loop.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
    if thisLoop != None:
        for paramName in thisLoop:
            globals()[paramName] = thisLoop[paramName]
    
    for thisLoop in loop:
        currentLoop = loop
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisLoop.rgb)
        if thisLoop != None:
            for paramName in thisLoop:
                globals()[paramName] = thisLoop[paramName]
        
        # --- Prepare to start Routine "Trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial.started', globalClock.getTime(format='float'))
        trialStimulus.setImage(imagefile)
        textKeys.setText('')
        # Run 'Begin Routine' code from code_textKeys
        textKeys.setText(instructions['Text_keys'])
        
        # Run 'Begin Routine' code from code_textPuzzle
        # Set the text for the first set of instructions
        textPuzzle.setText(instructions['Text_puzzle'] + str(trial) + "/100")
        trialResp.keys = []
        trialResp.rt = []
        _trialResp_allKeys = []
        # keep track of which components have finished
        TrialComponents = [trialStimulus, textKeys, textPuzzle, trialResp]
        for thisComponent in TrialComponents:
            thisComponent.tStart = None
            thisComponent.tStop = None
            thisComponent.tStartRefresh = None
            thisComponent.tStopRefresh = None
            if hasattr(thisComponent, 'status'):
                thisComponent.status = NOT_STARTED
        # reset timers
        t = 0
        _timeToFirstFrame = win.getFutureFlipTime(clock="now")
        frameN = -1
        
        # --- Run Routine "Trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *trialStimulus* updates
            
            # if trialStimulus is starting this frame...
            if trialStimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialStimulus.frameNStart = frameN  # exact frame index
                trialStimulus.tStart = t  # local t and not account for scr refresh
                trialStimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialStimulus, 'tStartRefresh')  # time at next scr refresh
                # update status
                trialStimulus.status = STARTED
                trialStimulus.setAutoDraw(True)
            
            # if trialStimulus is active this frame...
            if trialStimulus.status == STARTED:
                # update params
                pass
            
            # *textKeys* updates
            
            # if textKeys is starting this frame...
            if textKeys.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textKeys.frameNStart = frameN  # exact frame index
                textKeys.tStart = t  # local t and not account for scr refresh
                textKeys.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textKeys, 'tStartRefresh')  # time at next scr refresh
                # update status
                textKeys.status = STARTED
                textKeys.setAutoDraw(True)
            
            # if textKeys is active this frame...
            if textKeys.status == STARTED:
                # update params
                pass
            
            # *textPuzzle* updates
            
            # if textPuzzle is starting this frame...
            if textPuzzle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textPuzzle.frameNStart = frameN  # exact frame index
                textPuzzle.tStart = t  # local t and not account for scr refresh
                textPuzzle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textPuzzle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textPuzzle.started')
                # update status
                textPuzzle.status = STARTED
                textPuzzle.setAutoDraw(True)
            
            # if textPuzzle is active this frame...
            if textPuzzle.status == STARTED:
                # update params
                pass
            
            # *trialResp* updates
            waitOnFlip = False
            
            # if trialResp is starting this frame...
            if trialResp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                trialResp.frameNStart = frameN  # exact frame index
                trialResp.tStart = t  # local t and not account for scr refresh
                trialResp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(trialResp, 'tStartRefresh')  # time at next scr refresh
                # update status
                trialResp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(trialResp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(trialResp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if trialResp.status == STARTED and not waitOnFlip:
                theseKeys = trialResp.getKeys(keyList=['d', 'k'], ignoreKeys=["escape"], waitRelease=False)
                _trialResp_allKeys.extend(theseKeys)
                if len(_trialResp_allKeys):
                    trialResp.keys = _trialResp_allKeys[-1].name  # just the last key pressed
                    trialResp.rt = _trialResp_allKeys[-1].rt
                    trialResp.duration = _trialResp_allKeys[-1].duration
                    # was this correct?
                    if (trialResp.keys == str(corrAns)) or (trialResp.keys == corrAns):
                        trialResp.corr = 1
                    else:
                        trialResp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # check for quit (typically the Esc key)
            if defaultKeyboard.getKeys(keyList=["escape"]):
                thisExp.status = FINISHED
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in TrialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Trial" ---
        for thisComponent in TrialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Trial.stopped', globalClock.getTime(format='float'))
        # check responses
        if trialResp.keys in ['', [], None]:  # No response was made
            trialResp.keys = None
            # was no response the correct answer?!
            if str(corrAns).lower() == 'none':
               trialResp.corr = 1;  # correct non-response
            else:
               trialResp.corr = 0;  # failed to respond (incorrectly)
        # store data for loop (TrialHandler)
        loop.addData('trialResp.keys',trialResp.keys)
        loop.addData('trialResp.corr', trialResp.corr)
        if trialResp.keys != None:  # we had a response
            loop.addData('trialResp.rt', trialResp.rt)
            loop.addData('trialResp.duration', trialResp.duration)
        # Run 'End Routine' code from save_data
        # Add the key response to the data file
        thisExp.addData('trialResp.keys', trialResp.keys)
        thisExp.addData('trialResp.corr', trialResp.corr)
        if trialResp.keys is not None:  # We had a response
            thisExp.addData('trialResp.rt', trialResp.rt)
            thisExp.addData('trialResp.duration', trialResp.duration)
        thisExp.addData('imagefile', imagefile)
        thisExp.nextEntry()  # Ensure this trial's data is saved to the CSV file
        
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'loop'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_InstructionsText4
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['Text_end_task'])
    
    # Run 'Begin Routine' code from LSL_MRT_end
    send_marker('MRT_end')
    end_task.keys = []
    end_task.rt = []
    _end_task_allKeys = []
    # keep track of which components have finished
    endComponents = [InstructionsText4, end_task]
    for thisComponent in endComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    frameN = -1
    
    # --- Run Routine "end" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsText4* updates
        
        # if InstructionsText4 is starting this frame...
        if InstructionsText4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText4.frameNStart = frameN  # exact frame index
            InstructionsText4.tStart = t  # local t and not account for scr refresh
            InstructionsText4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText4, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText4.started')
            # update status
            InstructionsText4.status = STARTED
            InstructionsText4.setAutoDraw(True)
        
        # if InstructionsText4 is active this frame...
        if InstructionsText4.status == STARTED:
            # update params
            pass
        
        # *end_task* updates
        waitOnFlip = False
        
        # if end_task is starting this frame...
        if end_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_task.frameNStart = frameN  # exact frame index
            end_task.tStart = t  # local t and not account for scr refresh
            end_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_task.started')
            # update status
            end_task.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_task.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_task.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_task.status == STARTED and not waitOnFlip:
            theseKeys = end_task.getKeys(keyList=['y','n','left','right','space'], ignoreKeys=["escape"], waitRelease=False)
            _end_task_allKeys.extend(theseKeys)
            if len(_end_task_allKeys):
                end_task.keys = _end_task_allKeys[-1].name  # just the last key pressed
                end_task.rt = _end_task_allKeys[-1].rt
                end_task.duration = _end_task_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if defaultKeyboard.getKeys(keyList=["escape"]):
            thisExp.status = FINISHED
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in endComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "end" ---
    for thisComponent in endComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('end.stopped', globalClock.getTime(format='float'))
    # check responses
    if end_task.keys in ['', [], None]:  # No response was made
        end_task.keys = None
    thisExp.addData('end_task.keys',end_task.keys)
    if end_task.keys != None:  # we had a response
        thisExp.addData('end_task.rt', end_task.rt)
        thisExp.addData('end_task.duration', end_task.duration)
    thisExp.nextEntry()
    # the Routine "end" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # mark experiment as finished
    endExperiment(thisExp, win=win)


def saveData(thisExp):
    """
    Save data from this experiment
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    """
    filename = thisExp.dataFileName
    # these shouldn't be strictly necessary (should auto-save)
    thisExp.saveAsWideText(filename + '.csv', delim='auto')
    thisExp.saveAsPickle(filename)


def endExperiment(thisExp, win=None):
    """
    End this experiment, performing final shut down operations.
    
    This function does NOT close the window or end the Python process - use `quit` for this.
    
    Parameters
    ==========
    thisExp : psychopy.data.ExperimentHandler
        Handler object for this experiment, contains the data to save and information about 
        where to save it to.
    win : psychopy.visual.Window
        Window for this experiment.
    """
    if win is not None:
        # remove autodraw from all current components
        win.clearAutoDraw()
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed
        win.flip()
    # mark experiment handler as finished
    thisExp.status = FINISHED
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()


def quit(thisExp, win=None, thisSession=None):
    """
    Fully quit, closing the window and ending the Python process.
    
    Parameters
    ==========
    win : psychopy.visual.Window
        Window to close.
    thisSession : psychopy.session.Session or None
        Handle of the Session object this experiment is being run from, if any.
    """
    thisExp.abort()  # or data files will save again on exit
    # make sure everything is closed down
    if win is not None:
        # Flip one final time so any remaining win.callOnFlip() 
        # and win.timeOnFlip() tasks get executed before quitting
        win.flip()
        win.close()
    # shut down eyetracker, if there is one
    if deviceManager.getDevice('eyetracker') is not None:
        deviceManager.removeDevice('eyetracker')
    logging.flush()
    if thisSession is not None:
        thisSession.stop()
    # terminate Python process
    core.quit()


# if running this experiment as a script...
if __name__ == '__main__':
    # call all functions in order
    expInfo = showExpInfoDlg(expInfo=expInfo)
    thisExp = setupData(expInfo=expInfo)
    logFile = setupLogging(filename=thisExp.dataFileName)
    win = setupWindow(expInfo=expInfo)
    setupDevices(expInfo=expInfo, thisExp=thisExp, win=win)
    run(
        expInfo=expInfo, 
        thisExp=thisExp, 
        win=win,
        globalClock='float'
    )
    saveData(thisExp=thisExp)
    quit(thisExp=thisExp, win=win)
