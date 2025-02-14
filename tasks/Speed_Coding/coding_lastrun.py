#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 18:00
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
prefs.hardware['audioLatencyMode'] = '1'
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

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'symbols'  # from the Builder filename that created this script
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
_winSize = [1920, 1080]
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Speed_Coding\\coding_lastrun.py',
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
    if deviceManager.getDevice('startInst_2') is None:
        # initialise startInst_2
        startInst_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startInst_2',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('go_2') is None:
        # initialise go_2
        go_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go_2',
        )
    if deviceManager.getDevice('go2') is None:
        # initialise go2
        go2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go2',
        )
    if deviceManager.getDevice('key_resp_end') is None:
        # initialise key_resp_end
        key_resp_end = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_end',
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
    # Run 'Begin Experiment' code from define_block
    from psychopy import core
    import pandas as pd
    from psychopy import logging as psychoLogging
    
    # Set logging level to WARNING to suppress INFO and DEBUG messages
    psychoLogging.console.setLevel(logging.ERROR)
    pd.options.mode.chained_assignment = None  # default='warn'
    
    # Load the scenario CSV file
    scenario_df = pd.read_csv('coding_scenario.csv')
    
    # Filter the practice trials for mouse and keyboard
    practice_indices_keyboard = scenario_df.index[(scenario_df['block'] == 'practice_keyboard')].tolist()
    
    # Convert indices to PsychoPy's format (string of ranges)
    selected_rows_practice_keyboard = f"{practice_indices_keyboard[0]}:{practice_indices_keyboard[-1] + 1}" if practice_indices_keyboard else ""
    
    # Start clock
    stimulus_clock = core.Clock()
    
    # Run 'Begin Experiment' code from language
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
            'name_task': 'CODING',
            'Text_instructions_keyboard': "Welcome to the coding task.\n\nIn this task, your goal is to press the number on the numeric keypad that corresponds to the displayed symbol as quickly as possible.\n\nFirst, we shall have a practice session.\n\nPress the space bar to begin the practice session.",
            'Text_start_task_keyboard': "The practice is finished. Now we shall begin the actual experiment.\n\nReady?\n\nPress the space bar to begin.",
            'Text_pause_between_blocks': "Pause\n\nPress the space bar when you are ready to continue.",
            'Text_end_task': "This task is now over.\n\nThank you!\n\nPress the space bar to continue."
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task': 'CODAGE',
            'Text_instructions_keyboard': "Bienvenue dans la tâche de codage.\n\nDans cette tâche, votre objectif est d'appuyer sur le numéro du pavé numérique correspondant au symbole affiché aussi rapidement que possible.\n\nD'abord, nous allons faire une séance d'entraînement.\n\nAppuyez sur la barre d'espace pour commencer la séance d'entraînement.",
            'Text_start_task_keyboard': "L'entraînement est terminé. Nous allons maintenant commencer la tâche réelle.\n\nPrêt·e ?\n\nAppuyez sur la barre d'espace pour commencer.",
            'Text_pause_between_blocks': "Pause\n\nAppuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer.",
            'Text_end_task': "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer."
        }
    
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
    
    
    # --- Initialize components for Routine "instructions_keyboard" ---
    InstructionsText1_2 = visual.TextStim(win=win, name='InstructionsText1_2',
        text='',
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst_2 = keyboard.Keyboard(deviceName='startInst_2')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "cross" ---
    Main_symbols_k_cross = visual.ImageStim(
        win=win,
        name='Main_symbols_k_cross', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.9, 0.24),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    text = visual.TextStim(win=win, name='text',
        text='+',
        font='Arial',
        pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "main_keyboard" ---
    stim_k = visual.ImageStim(
        win=win,
        name='stim_k', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(0.1, 0.12),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Main_symbols_k = visual.ImageStim(
        win=win,
        name='Main_symbols_k', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.9, 0.24),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Arial',
        pos=(0, -0.05), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    Main_symbols_k_feedback = visual.ImageStim(
        win=win,
        name='Main_symbols_k_feedback', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.9, 0.24),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    
    # --- Initialize components for Routine "startTask_keyboard" ---
    InstructionsText2_2 = visual.TextStim(win=win, name='InstructionsText2_2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go_2 = keyboard.Keyboard(deviceName='go_2')
    
    # --- Initialize components for Routine "block_counter" ---
    
    # --- Initialize components for Routine "cross" ---
    Main_symbols_k_cross = visual.ImageStim(
        win=win,
        name='Main_symbols_k_cross', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.9, 0.24),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    text = visual.TextStim(win=win, name='text',
        text='+',
        font='Arial',
        pos=(0, -0.05), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "main_keyboard" ---
    stim_k = visual.ImageStim(
        win=win,
        name='stim_k', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.05), size=(0.1, 0.12),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    Main_symbols_k = visual.ImageStim(
        win=win,
        name='Main_symbols_k', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.9, 0.24),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-1.0)
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "pause" ---
    InstructionsText3 = visual.TextStim(win=win, name='InstructionsText3',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    go2 = keyboard.Keyboard(deviceName='go2')
    
    # --- Initialize components for Routine "thanks" ---
    InstructionsText4 = visual.TextStim(win=win, name='InstructionsText4',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_end = keyboard.Keyboard(deviceName='key_resp_end')
    
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
    
    # --- Prepare to start Routine "instructions_keyboard" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_keyboard.started', globalClock.getTime(format='float'))
    InstructionsText1_2.setText('hey')
    startInst_2.keys = []
    startInst_2.rt = []
    _startInst_2_allKeys = []
    # Run 'Begin Routine' code from code_InstructionsText1_2
    # Set the text for the first set of instructions
    InstructionsText1_2.setText(instructions['Text_instructions_keyboard'])
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # Run 'Begin Routine' code from LSL_start_coding
    send_marker('coding_start')
    # keep track of which components have finished
    instructions_keyboardComponents = [InstructionsText1_2, startInst_2, nametask]
    for thisComponent in instructions_keyboardComponents:
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
    
    # --- Run Routine "instructions_keyboard" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsText1_2* updates
        
        # if InstructionsText1_2 is starting this frame...
        if InstructionsText1_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText1_2.frameNStart = frameN  # exact frame index
            InstructionsText1_2.tStart = t  # local t and not account for scr refresh
            InstructionsText1_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText1_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText1_2.started')
            # update status
            InstructionsText1_2.status = STARTED
            InstructionsText1_2.setAutoDraw(True)
        
        # if InstructionsText1_2 is active this frame...
        if InstructionsText1_2.status == STARTED:
            # update params
            pass
        
        # *startInst_2* updates
        waitOnFlip = False
        
        # if startInst_2 is starting this frame...
        if startInst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst_2.frameNStart = frameN  # exact frame index
            startInst_2.tStart = t  # local t and not account for scr refresh
            startInst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst_2.started')
            # update status
            startInst_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst_2.status == STARTED and not waitOnFlip:
            theseKeys = startInst_2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _startInst_2_allKeys.extend(theseKeys)
            if len(_startInst_2_allKeys):
                startInst_2.keys = _startInst_2_allKeys[-1].name  # just the last key pressed
                startInst_2.rt = _startInst_2_allKeys[-1].rt
                startInst_2.duration = _startInst_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *nametask* updates
        
        # if nametask is starting this frame...
        if nametask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nametask.frameNStart = frameN  # exact frame index
            nametask.tStart = t  # local t and not account for scr refresh
            nametask.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nametask, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nametask.started')
            # update status
            nametask.status = STARTED
            nametask.setAutoDraw(True)
        
        # if nametask is active this frame...
        if nametask.status == STARTED:
            # update params
            pass
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in instructions_keyboardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_keyboard" ---
    for thisComponent in instructions_keyboardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_keyboard.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_practice_2
    send_marker('practice_keyboard')
    thisExp.nextEntry()
    # the Routine "instructions_keyboard" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    PracticeTrials_keyboard = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('coding_scenario.csv', selection=selected_rows_practice_keyboard),
        seed=None, name='PracticeTrials_keyboard')
    thisExp.addLoop(PracticeTrials_keyboard)  # add the loop to the experiment
    thisPracticeTrials_keyboard = PracticeTrials_keyboard.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrials_keyboard.rgb)
    if thisPracticeTrials_keyboard != None:
        for paramName in thisPracticeTrials_keyboard:
            globals()[paramName] = thisPracticeTrials_keyboard[paramName]
    
    for thisPracticeTrials_keyboard in PracticeTrials_keyboard:
        currentLoop = PracticeTrials_keyboard
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrials_keyboard.rgb)
        if thisPracticeTrials_keyboard != None:
            for paramName in thisPracticeTrials_keyboard:
                globals()[paramName] = thisPracticeTrials_keyboard[paramName]
        
        # --- Prepare to start Routine "cross" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('cross.started', globalClock.getTime(format='float'))
        Main_symbols_k_cross.setImage(grid)
        # keep track of which components have finished
        crossComponents = [Main_symbols_k_cross, text]
        for thisComponent in crossComponents:
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
        
        # --- Run Routine "cross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *Main_symbols_k_cross* updates
            
            # if Main_symbols_k_cross is starting this frame...
            if Main_symbols_k_cross.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                Main_symbols_k_cross.frameNStart = frameN  # exact frame index
                Main_symbols_k_cross.tStart = t  # local t and not account for scr refresh
                Main_symbols_k_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_symbols_k_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_symbols_k_cross.started')
                # update status
                Main_symbols_k_cross.status = STARTED
                Main_symbols_k_cross.setAutoDraw(True)
            
            # if Main_symbols_k_cross is active this frame...
            if Main_symbols_k_cross.status == STARTED:
                # update params
                pass
            
            # if Main_symbols_k_cross is stopping this frame...
            if Main_symbols_k_cross.status == STARTED:
                if frameN >= (Main_symbols_k_cross.frameNStart + 60):
                    # keep track of stop time/frame for later
                    Main_symbols_k_cross.tStop = t  # not accounting for scr refresh
                    Main_symbols_k_cross.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_symbols_k_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_symbols_k_cross.stopped')
                    # update status
                    Main_symbols_k_cross.status = FINISHED
                    Main_symbols_k_cross.setAutoDraw(False)
            
            # *text* updates
            
            # if text is starting this frame...
            if text.status == NOT_STARTED and frameN >= 30:
                # keep track of start time/frame for later
                text.frameNStart = frameN  # exact frame index
                text.tStart = t  # local t and not account for scr refresh
                text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text.started')
                # update status
                text.status = STARTED
                text.setAutoDraw(True)
            
            # if text is active this frame...
            if text.status == STARTED:
                # update params
                pass
            
            # if text is stopping this frame...
            if text.status == STARTED:
                if frameN >= 60:
                    # keep track of stop time/frame for later
                    text.tStop = t  # not accounting for scr refresh
                    text.tStopRefresh = tThisFlipGlobal  # on global time
                    text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.stopped')
                    # update status
                    text.status = FINISHED
                    text.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "cross" ---
        for thisComponent in crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('cross.stopped', globalClock.getTime(format='float'))
        # the Routine "cross" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "main_keyboard" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_keyboard.started', globalClock.getTime(format='float'))
        stim_k.setImage(stimulus)
        Main_symbols_k.setImage(grid)
        # Run 'Begin Routine' code from LSL_stimulus_k
        #Visible mouse
        send_marker("stimulus")
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        main_keyboardComponents = [stim_k, Main_symbols_k, key_resp]
        for thisComponent in main_keyboardComponents:
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
        
        # --- Run Routine "main_keyboard" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim_k* updates
            
            # if stim_k is starting this frame...
            if stim_k.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                stim_k.frameNStart = frameN  # exact frame index
                stim_k.tStart = t  # local t and not account for scr refresh
                stim_k.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim_k, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim_k.started')
                # update status
                stim_k.status = STARTED
                stim_k.setAutoDraw(True)
            
            # if stim_k is active this frame...
            if stim_k.status == STARTED:
                # update params
                pass
            
            # *Main_symbols_k* updates
            
            # if Main_symbols_k is starting this frame...
            if Main_symbols_k.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                Main_symbols_k.frameNStart = frameN  # exact frame index
                Main_symbols_k.tStart = t  # local t and not account for scr refresh
                Main_symbols_k.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_symbols_k, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_symbols_k.started')
                # update status
                Main_symbols_k.status = STARTED
                Main_symbols_k.setAutoDraw(True)
            
            # if Main_symbols_k is active this frame...
            if Main_symbols_k.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                key_resp.frameNStart = frameN  # exact frame index
                key_resp.tStart = t  # local t and not account for scr refresh
                key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_resp.started')
                # update status
                key_resp.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_resp.status == STARTED and not waitOnFlip:
                theseKeys = key_resp.getKeys(keyList=['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9'], ignoreKeys=None, waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
                    # was this correct?
                    if (key_resp.keys == str(correct_resp)) or (key_resp.keys == correct_resp):
                        key_resp.corr = 1
                    else:
                        key_resp.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in main_keyboardComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_keyboard" ---
        for thisComponent in main_keyboardComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_keyboard.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from LSL_stimulus_k
        answer_corr = f"response_{key_resp.corr}"
        send_marker(answer_corr)  # Function to send the LSL marker
        
        
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
            # was no response the correct answer?!
            if str(correct_resp).lower() == 'none':
               key_resp.corr = 1;  # correct non-response
            else:
               key_resp.corr = 0;  # failed to respond (incorrectly)
        # store data for PracticeTrials_keyboard (TrialHandler)
        PracticeTrials_keyboard.addData('key_resp.keys',key_resp.keys)
        PracticeTrials_keyboard.addData('key_resp.corr', key_resp.corr)
        if key_resp.keys != None:  # we had a response
            PracticeTrials_keyboard.addData('key_resp.rt', key_resp.rt)
            PracticeTrials_keyboard.addData('key_resp.duration', key_resp.duration)
        # the Routine "main_keyboard" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "feedback" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('feedback.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from set_feedback
        # Check if the response is incorrect
        if key_resp.corr != 1:
            feedback_message = 'X'  # Set the feedback message to a red cross
            feedback_text.color = 'red'  # Set the color to red
        else:
            feedback_message = ''  # No feedback if correct
        
        feedback_text.setText(feedback_message)
        Main_symbols_k_feedback.setImage(grid)
        # keep track of which components have finished
        feedbackComponents = [feedback_text, Main_symbols_k_feedback]
        for thisComponent in feedbackComponents:
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
        
        # --- Run Routine "feedback" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *feedback_text* updates
            
            # if feedback_text is starting this frame...
            if feedback_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                feedback_text.frameNStart = frameN  # exact frame index
                feedback_text.tStart = t  # local t and not account for scr refresh
                feedback_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(feedback_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'feedback_text.started')
                # update status
                feedback_text.status = STARTED
                feedback_text.setAutoDraw(True)
            
            # if feedback_text is active this frame...
            if feedback_text.status == STARTED:
                # update params
                pass
            
            # if feedback_text is stopping this frame...
            if feedback_text.status == STARTED:
                if frameN >= 30:
                    # keep track of stop time/frame for later
                    feedback_text.tStop = t  # not accounting for scr refresh
                    feedback_text.tStopRefresh = tThisFlipGlobal  # on global time
                    feedback_text.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text.stopped')
                    # update status
                    feedback_text.status = FINISHED
                    feedback_text.setAutoDraw(False)
            
            # *Main_symbols_k_feedback* updates
            
            # if Main_symbols_k_feedback is starting this frame...
            if Main_symbols_k_feedback.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                Main_symbols_k_feedback.frameNStart = frameN  # exact frame index
                Main_symbols_k_feedback.tStart = t  # local t and not account for scr refresh
                Main_symbols_k_feedback.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Main_symbols_k_feedback, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Main_symbols_k_feedback.started')
                # update status
                Main_symbols_k_feedback.status = STARTED
                Main_symbols_k_feedback.setAutoDraw(True)
            
            # if Main_symbols_k_feedback is active this frame...
            if Main_symbols_k_feedback.status == STARTED:
                # update params
                pass
            
            # if Main_symbols_k_feedback is stopping this frame...
            if Main_symbols_k_feedback.status == STARTED:
                if frameN >= 30:
                    # keep track of stop time/frame for later
                    Main_symbols_k_feedback.tStop = t  # not accounting for scr refresh
                    Main_symbols_k_feedback.tStopRefresh = tThisFlipGlobal  # on global time
                    Main_symbols_k_feedback.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_symbols_k_feedback.stopped')
                    # update status
                    Main_symbols_k_feedback.status = FINISHED
                    Main_symbols_k_feedback.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in feedbackComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "feedback" ---
        for thisComponent in feedbackComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('feedback.stopped', globalClock.getTime(format='float'))
        # the Routine "feedback" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'PracticeTrials_keyboard'
    
    
    # --- Prepare to start Routine "startTask_keyboard" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('startTask_keyboard.started', globalClock.getTime(format='float'))
    InstructionsText2_2.setText('')
    go_2.keys = []
    go_2.rt = []
    _go_2_allKeys = []
    # Run 'Begin Routine' code from code_InstructionsText2_2
    # Set the text for the second set of instructions
    InstructionsText2_2.setText(instructions['Text_start_task_keyboard'])
    # Run 'Begin Routine' code from define_block_rows_keyboard
    # Initialize block variables
    block_index = 0
    block_type = 'keyboard' 
    is_test = True
    
    # keep track of which components have finished
    startTask_keyboardComponents = [InstructionsText2_2, go_2]
    for thisComponent in startTask_keyboardComponents:
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
    
    # --- Run Routine "startTask_keyboard" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsText2_2* updates
        
        # if InstructionsText2_2 is starting this frame...
        if InstructionsText2_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText2_2.frameNStart = frameN  # exact frame index
            InstructionsText2_2.tStart = t  # local t and not account for scr refresh
            InstructionsText2_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText2_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText2_2.started')
            # update status
            InstructionsText2_2.status = STARTED
            InstructionsText2_2.setAutoDraw(True)
        
        # if InstructionsText2_2 is active this frame...
        if InstructionsText2_2.status == STARTED:
            # update params
            pass
        
        # *go_2* updates
        waitOnFlip = False
        
        # if go_2 is starting this frame...
        if go_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            go_2.frameNStart = frameN  # exact frame index
            go_2.tStart = t  # local t and not account for scr refresh
            go_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'go_2.started')
            # update status
            go_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(go_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(go_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if go_2.status == STARTED and not waitOnFlip:
            theseKeys = go_2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _go_2_allKeys.extend(theseKeys)
            if len(_go_2_allKeys):
                go_2.keys = _go_2_allKeys[-1].name  # just the last key pressed
                go_2.rt = _go_2_allKeys[-1].rt
                go_2.duration = _go_2_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        # Run 'Each Frame' code from define_block_rows_keyboard
        #Visible mouse
        event.Mouse(visible=False)
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in startTask_keyboardComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startTask_keyboard" ---
    for thisComponent in startTask_keyboardComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('startTask_keyboard.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_test_blocks_2
    send_marker("start_test_blocks")
    thisExp.nextEntry()
    # the Routine "startTask_keyboard" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testblocksKeyboard = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('coding_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test_keyboard') & (scenario_df['block_n'] == block_index)].index.tolist()),
        seed=None, name='testblocksKeyboard')
    thisExp.addLoop(testblocksKeyboard)  # add the loop to the experiment
    thisTestblocksKeyboard = testblocksKeyboard.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestblocksKeyboard.rgb)
    if thisTestblocksKeyboard != None:
        for paramName in thisTestblocksKeyboard:
            globals()[paramName] = thisTestblocksKeyboard[paramName]
    
    for thisTestblocksKeyboard in testblocksKeyboard:
        currentLoop = testblocksKeyboard
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTestblocksKeyboard.rgb)
        if thisTestblocksKeyboard != None:
            for paramName in thisTestblocksKeyboard:
                globals()[paramName] = thisTestblocksKeyboard[paramName]
        
        # --- Prepare to start Routine "block_counter" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block_counter.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from blockSetup
        # Increment block counter
        block_index += 1
        
        # Determine the current block type and number
        if block_type == 'mouse':
            if block_index >= len(scenario_df[scenario_df['block'] == 'test_mouse']['block_n'].unique()):
                # Skip the remaining test blocks
                testblocksMouse.finished = True
                continueRoutine = False
            else:
                block_n = block_index  # block_n in CSV starts from 1
        
        elif block_type == 'keyboard':
            if block_index >= len(scenario_df[scenario_df['block'] == 'test_keyboard']['block_n'].unique()):
                # Skip the remaining test blocks
                testblocksKeyboard.finished = True
                continueRoutine = False
            else:
                block_n = block_index  # block_n in CSV starts from 1
        
        # Run 'Begin Routine' code from LSL_start_testblock
        send_marker("start_block")
        # keep track of which components have finished
        block_counterComponents = []
        for thisComponent in block_counterComponents:
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
        
        # --- Run Routine "block_counter" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from LSL_start_testblock
            #Visible mouse
            event.Mouse(visible=False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in block_counterComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_counter" ---
        for thisComponent in block_counterComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block_counter.stopped', globalClock.getTime(format='float'))
        # the Routine "block_counter" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        testTrialsKeyboard = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('coding_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test_keyboard') & (scenario_df['block_n'] == block_index)].index.tolist()),
            seed=None, name='testTrialsKeyboard')
        thisExp.addLoop(testTrialsKeyboard)  # add the loop to the experiment
        thisTestTrialsKeyboard = testTrialsKeyboard.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTestTrialsKeyboard.rgb)
        if thisTestTrialsKeyboard != None:
            for paramName in thisTestTrialsKeyboard:
                globals()[paramName] = thisTestTrialsKeyboard[paramName]
        
        for thisTestTrialsKeyboard in testTrialsKeyboard:
            currentLoop = testTrialsKeyboard
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTestTrialsKeyboard.rgb)
            if thisTestTrialsKeyboard != None:
                for paramName in thisTestTrialsKeyboard:
                    globals()[paramName] = thisTestTrialsKeyboard[paramName]
            
            # --- Prepare to start Routine "cross" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('cross.started', globalClock.getTime(format='float'))
            Main_symbols_k_cross.setImage(grid)
            # keep track of which components have finished
            crossComponents = [Main_symbols_k_cross, text]
            for thisComponent in crossComponents:
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
            
            # --- Run Routine "cross" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *Main_symbols_k_cross* updates
                
                # if Main_symbols_k_cross is starting this frame...
                if Main_symbols_k_cross.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    Main_symbols_k_cross.frameNStart = frameN  # exact frame index
                    Main_symbols_k_cross.tStart = t  # local t and not account for scr refresh
                    Main_symbols_k_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Main_symbols_k_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_symbols_k_cross.started')
                    # update status
                    Main_symbols_k_cross.status = STARTED
                    Main_symbols_k_cross.setAutoDraw(True)
                
                # if Main_symbols_k_cross is active this frame...
                if Main_symbols_k_cross.status == STARTED:
                    # update params
                    pass
                
                # if Main_symbols_k_cross is stopping this frame...
                if Main_symbols_k_cross.status == STARTED:
                    if frameN >= (Main_symbols_k_cross.frameNStart + 60):
                        # keep track of stop time/frame for later
                        Main_symbols_k_cross.tStop = t  # not accounting for scr refresh
                        Main_symbols_k_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        Main_symbols_k_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'Main_symbols_k_cross.stopped')
                        # update status
                        Main_symbols_k_cross.status = FINISHED
                        Main_symbols_k_cross.setAutoDraw(False)
                
                # *text* updates
                
                # if text is starting this frame...
                if text.status == NOT_STARTED and frameN >= 30:
                    # keep track of start time/frame for later
                    text.frameNStart = frameN  # exact frame index
                    text.tStart = t  # local t and not account for scr refresh
                    text.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text.started')
                    # update status
                    text.status = STARTED
                    text.setAutoDraw(True)
                
                # if text is active this frame...
                if text.status == STARTED:
                    # update params
                    pass
                
                # if text is stopping this frame...
                if text.status == STARTED:
                    if frameN >= 60:
                        # keep track of stop time/frame for later
                        text.tStop = t  # not accounting for scr refresh
                        text.tStopRefresh = tThisFlipGlobal  # on global time
                        text.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text.stopped')
                        # update status
                        text.status = FINISHED
                        text.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in crossComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "cross" ---
            for thisComponent in crossComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('cross.stopped', globalClock.getTime(format='float'))
            # the Routine "cross" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "main_keyboard" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('main_keyboard.started', globalClock.getTime(format='float'))
            stim_k.setImage(stimulus)
            Main_symbols_k.setImage(grid)
            # Run 'Begin Routine' code from LSL_stimulus_k
            #Visible mouse
            send_marker("stimulus")
            key_resp.keys = []
            key_resp.rt = []
            _key_resp_allKeys = []
            # keep track of which components have finished
            main_keyboardComponents = [stim_k, Main_symbols_k, key_resp]
            for thisComponent in main_keyboardComponents:
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
            
            # --- Run Routine "main_keyboard" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stim_k* updates
                
                # if stim_k is starting this frame...
                if stim_k.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    stim_k.frameNStart = frameN  # exact frame index
                    stim_k.tStart = t  # local t and not account for scr refresh
                    stim_k.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim_k, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim_k.started')
                    # update status
                    stim_k.status = STARTED
                    stim_k.setAutoDraw(True)
                
                # if stim_k is active this frame...
                if stim_k.status == STARTED:
                    # update params
                    pass
                
                # *Main_symbols_k* updates
                
                # if Main_symbols_k is starting this frame...
                if Main_symbols_k.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    Main_symbols_k.frameNStart = frameN  # exact frame index
                    Main_symbols_k.tStart = t  # local t and not account for scr refresh
                    Main_symbols_k.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(Main_symbols_k, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'Main_symbols_k.started')
                    # update status
                    Main_symbols_k.status = STARTED
                    Main_symbols_k.setAutoDraw(True)
                
                # if Main_symbols_k is active this frame...
                if Main_symbols_k.status == STARTED:
                    # update params
                    pass
                
                # *key_resp* updates
                waitOnFlip = False
                
                # if key_resp is starting this frame...
                if key_resp.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    key_resp.frameNStart = frameN  # exact frame index
                    key_resp.tStart = t  # local t and not account for scr refresh
                    key_resp.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_resp.started')
                    # update status
                    key_resp.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_resp.status == STARTED and not waitOnFlip:
                    theseKeys = key_resp.getKeys(keyList=['num_1', 'num_2', 'num_3', 'num_4', 'num_5', 'num_6', 'num_7', 'num_8', 'num_9'], ignoreKeys=None, waitRelease=False)
                    _key_resp_allKeys.extend(theseKeys)
                    if len(_key_resp_allKeys):
                        key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                        key_resp.rt = _key_resp_allKeys[-1].rt
                        key_resp.duration = _key_resp_allKeys[-1].duration
                        # was this correct?
                        if (key_resp.keys == str(correct_resp)) or (key_resp.keys == correct_resp):
                            key_resp.corr = 1
                        else:
                            key_resp.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in main_keyboardComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "main_keyboard" ---
            for thisComponent in main_keyboardComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('main_keyboard.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from LSL_stimulus_k
            answer_corr = f"response_{key_resp.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # check responses
            if key_resp.keys in ['', [], None]:  # No response was made
                key_resp.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_resp.corr = 1;  # correct non-response
                else:
                   key_resp.corr = 0;  # failed to respond (incorrectly)
            # store data for testTrialsKeyboard (TrialHandler)
            testTrialsKeyboard.addData('key_resp.keys',key_resp.keys)
            testTrialsKeyboard.addData('key_resp.corr', key_resp.corr)
            if key_resp.keys != None:  # we had a response
                testTrialsKeyboard.addData('key_resp.rt', key_resp.rt)
                testTrialsKeyboard.addData('key_resp.duration', key_resp.duration)
            # the Routine "main_keyboard" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'testTrialsKeyboard'
        
        
        # --- Prepare to start Routine "pause" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pause.started', globalClock.getTime(format='float'))
        InstructionsText3.setText('')
        go2.keys = []
        go2.rt = []
        _go2_allKeys = []
        # Run 'Begin Routine' code from code_InstructionsText3
        # Set the text for the third set of instructions
        InstructionsText3.setText(instructions['Text_pause_between_blocks'])
        
        # Run 'Begin Routine' code from check_block_counter
        # Determine the current block type and number
        
        if block_index >= len(scenario_df[scenario_df['block'] == 'test_keyboard']['block_n'].unique()):
            # Skip the remaining test blocks
            testblocksKeyboard.finished = True
            continueRoutine = False
        else:
            block_n = block_index  # block_n in CSV starts from 1
        
        # keep track of which components have finished
        pauseComponents = [InstructionsText3, go2]
        for thisComponent in pauseComponents:
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
        
        # --- Run Routine "pause" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *InstructionsText3* updates
            
            # if InstructionsText3 is starting this frame...
            if InstructionsText3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                InstructionsText3.frameNStart = frameN  # exact frame index
                InstructionsText3.tStart = t  # local t and not account for scr refresh
                InstructionsText3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstructionsText3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionsText3.started')
                # update status
                InstructionsText3.status = STARTED
                InstructionsText3.setAutoDraw(True)
            
            # if InstructionsText3 is active this frame...
            if InstructionsText3.status == STARTED:
                # update params
                pass
            
            # *go2* updates
            waitOnFlip = False
            
            # if go2 is starting this frame...
            if go2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go2.frameNStart = frameN  # exact frame index
                go2.tStart = t  # local t and not account for scr refresh
                go2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'go2.started')
                # update status
                go2.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(go2.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(go2.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if go2.status == STARTED and not waitOnFlip:
                theseKeys = go2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _go2_allKeys.extend(theseKeys)
                if len(_go2_allKeys):
                    go2.keys = _go2_allKeys[-1].name  # just the last key pressed
                    go2.rt = _go2_allKeys[-1].rt
                    go2.duration = _go2_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            # Run 'Each Frame' code from check_block_counter
            #Visible mouse
            event.Mouse(visible=False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pauseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause" ---
        for thisComponent in pauseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pause.stopped', globalClock.getTime(format='float'))
        # check responses
        if go2.keys in ['', [], None]:  # No response was made
            go2.keys = None
        testblocksKeyboard.addData('go2.keys',go2.keys)
        if go2.keys != None:  # we had a response
            testblocksKeyboard.addData('go2.rt', go2.rt)
            testblocksKeyboard.addData('go2.duration', go2.duration)
        # the Routine "pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'testblocksKeyboard'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from LSL_Coding_end
    send_marker('coding_end')
    # Run 'Begin Routine' code from code_InstructionsText4
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['Text_end_task'])
    
    key_resp_end.keys = []
    key_resp_end.rt = []
    _key_resp_end_allKeys = []
    # keep track of which components have finished
    thanksComponents = [InstructionsText4, key_resp_end]
    for thisComponent in thanksComponents:
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
    
    # --- Run Routine "thanks" ---
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
        
        # *key_resp_end* updates
        waitOnFlip = False
        
        # if key_resp_end is starting this frame...
        if key_resp_end.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_end.frameNStart = frameN  # exact frame index
            key_resp_end.tStart = t  # local t and not account for scr refresh
            key_resp_end.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_end, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'key_resp_end.started')
            # update status
            key_resp_end.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_end.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_end.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_end.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_end.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _key_resp_end_allKeys.extend(theseKeys)
            if len(_key_resp_end_allKeys):
                key_resp_end.keys = _key_resp_end_allKeys[-1].name  # just the last key pressed
                key_resp_end.rt = _key_resp_end_allKeys[-1].rt
                key_resp_end.duration = _key_resp_end_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in thanksComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "thanks" ---
    for thisComponent in thanksComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('thanks.stopped', globalClock.getTime(format='float'))
    # check responses
    if key_resp_end.keys in ['', [], None]:  # No response was made
        key_resp_end.keys = None
    thisExp.addData('key_resp_end.keys',key_resp_end.keys)
    if key_resp_end.keys != None:  # we had a response
        thisExp.addData('key_resp_end.rt', key_resp_end.rt)
        thisExp.addData('key_resp_end.duration', key_resp_end.duration)
    thisExp.nextEntry()
    # the Routine "thanks" was not non-slip safe, so reset the non-slip timer
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
