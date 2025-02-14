﻿#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 17:58
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Speed_Symbols\\symbols_lastrun.py',
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
    if deviceManager.getDevice('startInst') is None:
        # initialise startInst
        startInst = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startInst',
        )
    if deviceManager.getDevice('response') is None:
        # initialise response
        response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response',
        )
    if deviceManager.getDevice('go') is None:
        # initialise go
        go = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go',
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
    scenario_df = pd.read_csv('symbols_scenario.csv')
    
    # Filter the practice trials for mouse and keyboard
    practice_indices = scenario_df.index[(scenario_df['block'] == 'practice')].tolist()
    
    # Convert indices to PsychoPy's format (string of ranges)
    selected_rows_practice = f"{practice_indices[0]}:{practice_indices[-1] + 1}" if practice_indices else ""
    
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
            'name_task' : 'SYMBOL SEARCH',
            'Text_instructions': "Welcome to the symbol search task.\n\nIn this task, your goal is to determine if either of the displayed symbols on the right is present in the row of six symbols on the right.\n\nPress 'k' if at least one symbol is present (the symbol must be EXACTLY the same, with the same orientation) in the row.\nPress 'd' if neither is present.\n\nFirst, we shall have a practice session.\nPress the space bar to begin.",
            'Text_start_task': "The practice session is finished. Now we shall begin the actual experiment.\n\nReady?\n\nPress the space bar to begin.",
            'Text_pause_between_blocks': "Pause\n\nPress the space bar when you are ready to continue.",
            'Text_end_task': "This task is now over.\n\nThank you!\n\nPress the space bar to continue"
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task' : 'RECHERCHE DE SYMBOLES',
            'Text_instructions': "Bienvenue dans la tâche de recherche de symboles.\n\nDans cette tâche, votre objectif est de déterminer si l'un des symboles affichés à gauche est présent dans la rangée de six symboles à droite.\n\nAppuyez sur 'k' si au moins l'un des deux symboles est présent (le symbole doit être EXACTEMENT le même, avec la même orientation).\n Appuyez sur 'd' si aucun n'est présent.\n\nD'abord, nous allons faire une séance d'entraînement.\nAppuyez sur la barre d'espace pour commencer.",
            'Text_start_task': "L'entraînement est terminé. Nous allons maintenant commencer la vraie tâche.\n\nPrêt·e ?\n\nAppuyez sur la barre d'espace pour commencer.",
            'Text_pause_between_blocks': "Pause\n\nAppuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer.",
            'Text_end_task': "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer"
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
    
    
    # --- Initialize components for Routine "instructions1" ---
    InstructionsText1 = visual.TextStim(win=win, name='InstructionsText1',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst = keyboard.Keyboard(deviceName='startInst')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "pre_stim" ---
    nothing = visual.TextStim(win=win, name='nothing',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_cross = visual.TextStim(win=win, name='text_cross',
        text='+',
        font='Arial',
        pos=(-0.6, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.5, 0.2)[0], height=(0.5, 0.2)[1],
        ori=0.0, pos=(-0.6, 0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "symbols" ---
    stim1 = visual.ImageStim(
        win=win,
        name='stim1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.7, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    stim2 = visual.ImageStim(
        win=win,
        name='stim2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    symbol1_img = visual.ImageStim(
        win=win,
        name='symbol1_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    symbol2_img = visual.ImageStim(
        win=win,
        name='symbol2_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    symbol3_img = visual.ImageStim(
        win=win,
        name='symbol3_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    symbol4_img = visual.ImageStim(
        win=win,
        name='symbol4_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    symbol5_img = visual.ImageStim(
        win=win,
        name='symbol5_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-6.0)
    polygon_2 = visual.Rect(
        win=win, name='polygon_2',
        width=(0.5, 0.2)[0], height=(0.5, 0.2)[1],
        ori=0.0, pos=(-0.6, 0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    response = keyboard.Keyboard(deviceName='response')
    
    # --- Initialize components for Routine "startTask" ---
    InstructionsText2 = visual.TextStim(win=win, name='InstructionsText2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go = keyboard.Keyboard(deviceName='go')
    
    # --- Initialize components for Routine "block_counter" ---
    
    # --- Initialize components for Routine "pre_stim" ---
    nothing = visual.TextStim(win=win, name='nothing',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_cross = visual.TextStim(win=win, name='text_cross',
        text='+',
        font='Arial',
        pos=(-0.6, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    polygon = visual.Rect(
        win=win, name='polygon',
        width=(0.5, 0.2)[0], height=(0.5, 0.2)[1],
        ori=0.0, pos=(-0.6, 0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-2.0, interpolate=True)
    
    # --- Initialize components for Routine "symbols" ---
    stim1 = visual.ImageStim(
        win=win,
        name='stim1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.7, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=0.0)
    stim2 = visual.ImageStim(
        win=win,
        name='stim2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    symbol1_img = visual.ImageStim(
        win=win,
        name='symbol1_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-2.0)
    symbol2_img = visual.ImageStim(
        win=win,
        name='symbol2_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-3.0)
    symbol3_img = visual.ImageStim(
        win=win,
        name='symbol3_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-4.0)
    symbol4_img = visual.ImageStim(
        win=win,
        name='symbol4_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-5.0)
    symbol5_img = visual.ImageStim(
        win=win,
        name='symbol5_img', units='height', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=[0,0], size=(0.1, 0.1),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=-6.0)
    polygon_2 = visual.Rect(
        win=win, name='polygon_2',
        width=(0.5, 0.2)[0], height=(0.5, 0.2)[1],
        ori=0.0, pos=(-0.6, 0), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-7.0, interpolate=True)
    response = keyboard.Keyboard(deviceName='response')
    
    # --- Initialize components for Routine "pause" ---
    InstructionsText3 = visual.TextStim(win=win, name='InstructionsText3',
        text='',
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
    
    # --- Prepare to start Routine "instructions1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions1.started', globalClock.getTime(format='float'))
    InstructionsText1.setText('')
    startInst.keys = []
    startInst.rt = []
    _startInst_allKeys = []
    # Run 'Begin Routine' code from code_InstructionsText1
    # Set the text for the first set of instructions
    InstructionsText1.setText(instructions['Text_instructions'])
    # Run 'Begin Routine' code from LSL_Symbols_start
    send_marker('symbols_start')
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions1Components = [InstructionsText1, startInst, nametask]
    for thisComponent in instructions1Components:
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
    
    # --- Run Routine "instructions1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsText1* updates
        
        # if InstructionsText1 is starting this frame...
        if InstructionsText1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText1.frameNStart = frameN  # exact frame index
            InstructionsText1.tStart = t  # local t and not account for scr refresh
            InstructionsText1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText1.started')
            # update status
            InstructionsText1.status = STARTED
            InstructionsText1.setAutoDraw(True)
        
        # if InstructionsText1 is active this frame...
        if InstructionsText1.status == STARTED:
            # update params
            pass
        
        # *startInst* updates
        waitOnFlip = False
        
        # if startInst is starting this frame...
        if startInst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst.frameNStart = frameN  # exact frame index
            startInst.tStart = t  # local t and not account for scr refresh
            startInst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst.started')
            # update status
            startInst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst.status == STARTED and not waitOnFlip:
            theseKeys = startInst.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _startInst_allKeys.extend(theseKeys)
            if len(_startInst_allKeys):
                startInst.keys = _startInst_allKeys[-1].name  # just the last key pressed
                startInst.rt = _startInst_allKeys[-1].rt
                startInst.duration = _startInst_allKeys[-1].duration
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
        for thisComponent in instructions1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions1" ---
    for thisComponent in instructions1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions1.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_practice
    send_marker('practice')
    thisExp.nextEntry()
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('symbols_scenario.csv', selection=selected_rows_practice),
        seed=None, name='practiceTrials')
    thisExp.addLoop(practiceTrials)  # add the loop to the experiment
    thisPracticeTrial = practiceTrials.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
    if thisPracticeTrial != None:
        for paramName in thisPracticeTrial:
            globals()[paramName] = thisPracticeTrial[paramName]
    
    for thisPracticeTrial in practiceTrials:
        currentLoop = practiceTrials
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeTrial.rgb)
        if thisPracticeTrial != None:
            for paramName in thisPracticeTrial:
                globals()[paramName] = thisPracticeTrial[paramName]
        
        # --- Prepare to start Routine "pre_stim" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pre_stim.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        pre_stimComponents = [nothing, text_cross, polygon]
        for thisComponent in pre_stimComponents:
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
        
        # --- Run Routine "pre_stim" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *nothing* updates
            
            # if nothing is starting this frame...
            if nothing.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                nothing.frameNStart = frameN  # exact frame index
                nothing.tStart = t  # local t and not account for scr refresh
                nothing.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(nothing, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'nothing.started')
                # update status
                nothing.status = STARTED
                nothing.setAutoDraw(True)
            
            # if nothing is active this frame...
            if nothing.status == STARTED:
                # update params
                pass
            
            # if nothing is stopping this frame...
            if nothing.status == STARTED:
                if frameN >= 30:
                    # keep track of stop time/frame for later
                    nothing.tStop = t  # not accounting for scr refresh
                    nothing.tStopRefresh = tThisFlipGlobal  # on global time
                    nothing.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'nothing.stopped')
                    # update status
                    nothing.status = FINISHED
                    nothing.setAutoDraw(False)
            
            # *text_cross* updates
            
            # if text_cross is starting this frame...
            if text_cross.status == NOT_STARTED and frameN >= 30:
                # keep track of start time/frame for later
                text_cross.frameNStart = frameN  # exact frame index
                text_cross.tStart = t  # local t and not account for scr refresh
                text_cross.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_cross, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_cross.started')
                # update status
                text_cross.status = STARTED
                text_cross.setAutoDraw(True)
            
            # if text_cross is active this frame...
            if text_cross.status == STARTED:
                # update params
                pass
            
            # if text_cross is stopping this frame...
            if text_cross.status == STARTED:
                if frameN >= 60:
                    # keep track of stop time/frame for later
                    text_cross.tStop = t  # not accounting for scr refresh
                    text_cross.tStopRefresh = tThisFlipGlobal  # on global time
                    text_cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_cross.stopped')
                    # update status
                    text_cross.status = FINISHED
                    text_cross.setAutoDraw(False)
            
            # *polygon* updates
            
            # if polygon is starting this frame...
            if polygon.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                polygon.frameNStart = frameN  # exact frame index
                polygon.tStart = t  # local t and not account for scr refresh
                polygon.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon.started')
                # update status
                polygon.status = STARTED
                polygon.setAutoDraw(True)
            
            # if polygon is active this frame...
            if polygon.status == STARTED:
                # update params
                pass
            
            # if polygon is stopping this frame...
            if polygon.status == STARTED:
                if frameN >= (polygon.frameNStart + 60):
                    # keep track of stop time/frame for later
                    polygon.tStop = t  # not accounting for scr refresh
                    polygon.tStopRefresh = tThisFlipGlobal  # on global time
                    polygon.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.stopped')
                    # update status
                    polygon.status = FINISHED
                    polygon.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in pre_stimComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pre_stim" ---
        for thisComponent in pre_stimComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pre_stim.stopped', globalClock.getTime(format='float'))
        # the Routine "pre_stim" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "symbols" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('symbols.started', globalClock.getTime(format='float'))
        stim1.setImage(stimulus1)
        stim2.setImage(stimulus2)
        symbol1_img.setPos((-0.1, 0))
        symbol1_img.setImage(symbol1)
        symbol2_img.setPos((0.1, 0))
        symbol2_img.setImage(symbol2)
        symbol3_img.setPos((0.3, 0))
        symbol3_img.setImage(symbol3)
        symbol4_img.setPos((0.5, 0))
        symbol4_img.setImage(symbol4)
        symbol5_img.setPos((0.7, 0))
        symbol5_img.setImage(symbol5)
        # Run 'Begin Routine' code from LSL_stimulus_2
        marker = f"stimulus_trial_{trial}"
        send_marker(marker)
        response.keys = []
        response.rt = []
        _response_allKeys = []
        # keep track of which components have finished
        symbolsComponents = [stim1, stim2, symbol1_img, symbol2_img, symbol3_img, symbol4_img, symbol5_img, polygon_2, response]
        for thisComponent in symbolsComponents:
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
        
        # --- Run Routine "symbols" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *stim1* updates
            
            # if stim1 is starting this frame...
            if stim1.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                stim1.frameNStart = frameN  # exact frame index
                stim1.tStart = t  # local t and not account for scr refresh
                stim1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim1.started')
                # update status
                stim1.status = STARTED
                stim1.setAutoDraw(True)
            
            # if stim1 is active this frame...
            if stim1.status == STARTED:
                # update params
                pass
            
            # *stim2* updates
            
            # if stim2 is starting this frame...
            if stim2.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                stim2.frameNStart = frameN  # exact frame index
                stim2.tStart = t  # local t and not account for scr refresh
                stim2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'stim2.started')
                # update status
                stim2.status = STARTED
                stim2.setAutoDraw(True)
            
            # if stim2 is active this frame...
            if stim2.status == STARTED:
                # update params
                pass
            
            # *symbol1_img* updates
            
            # if symbol1_img is starting this frame...
            if symbol1_img.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                symbol1_img.frameNStart = frameN  # exact frame index
                symbol1_img.tStart = t  # local t and not account for scr refresh
                symbol1_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol1_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol1_img.started')
                # update status
                symbol1_img.status = STARTED
                symbol1_img.setAutoDraw(True)
            
            # if symbol1_img is active this frame...
            if symbol1_img.status == STARTED:
                # update params
                pass
            
            # *symbol2_img* updates
            
            # if symbol2_img is starting this frame...
            if symbol2_img.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                symbol2_img.frameNStart = frameN  # exact frame index
                symbol2_img.tStart = t  # local t and not account for scr refresh
                symbol2_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol2_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol2_img.started')
                # update status
                symbol2_img.status = STARTED
                symbol2_img.setAutoDraw(True)
            
            # if symbol2_img is active this frame...
            if symbol2_img.status == STARTED:
                # update params
                pass
            
            # *symbol3_img* updates
            
            # if symbol3_img is starting this frame...
            if symbol3_img.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                symbol3_img.frameNStart = frameN  # exact frame index
                symbol3_img.tStart = t  # local t and not account for scr refresh
                symbol3_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol3_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol3_img.started')
                # update status
                symbol3_img.status = STARTED
                symbol3_img.setAutoDraw(True)
            
            # if symbol3_img is active this frame...
            if symbol3_img.status == STARTED:
                # update params
                pass
            
            # *symbol4_img* updates
            
            # if symbol4_img is starting this frame...
            if symbol4_img.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                symbol4_img.frameNStart = frameN  # exact frame index
                symbol4_img.tStart = t  # local t and not account for scr refresh
                symbol4_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol4_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol4_img.started')
                # update status
                symbol4_img.status = STARTED
                symbol4_img.setAutoDraw(True)
            
            # if symbol4_img is active this frame...
            if symbol4_img.status == STARTED:
                # update params
                pass
            
            # *symbol5_img* updates
            
            # if symbol5_img is starting this frame...
            if symbol5_img.status == NOT_STARTED and frameN >= 0:
                # keep track of start time/frame for later
                symbol5_img.frameNStart = frameN  # exact frame index
                symbol5_img.tStart = t  # local t and not account for scr refresh
                symbol5_img.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(symbol5_img, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'symbol5_img.started')
                # update status
                symbol5_img.status = STARTED
                symbol5_img.setAutoDraw(True)
            
            # if symbol5_img is active this frame...
            if symbol5_img.status == STARTED:
                # update params
                pass
            
            # *polygon_2* updates
            
            # if polygon_2 is starting this frame...
            if polygon_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                polygon_2.frameNStart = frameN  # exact frame index
                polygon_2.tStart = t  # local t and not account for scr refresh
                polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'polygon_2.started')
                # update status
                polygon_2.status = STARTED
                polygon_2.setAutoDraw(True)
            
            # if polygon_2 is active this frame...
            if polygon_2.status == STARTED:
                # update params
                pass
            
            # *response* updates
            waitOnFlip = False
            
            # if response is starting this frame...
            if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                response.frameNStart = frameN  # exact frame index
                response.tStart = t  # local t and not account for scr refresh
                response.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'response.started')
                # update status
                response.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if response.status == STARTED and not waitOnFlip:
                theseKeys = response.getKeys(keyList=['d','k'], ignoreKeys=None, waitRelease=False)
                _response_allKeys.extend(theseKeys)
                if len(_response_allKeys):
                    response.keys = _response_allKeys[-1].name  # just the last key pressed
                    response.rt = _response_allKeys[-1].rt
                    response.duration = _response_allKeys[-1].duration
                    # was this correct?
                    if (response.keys == str(correct_resp)) or (response.keys == correct_resp):
                        response.corr = 1
                    else:
                        response.corr = 0
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
            for thisComponent in symbolsComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "symbols" ---
        for thisComponent in symbolsComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('symbols.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from LSL_stimulus_2
        answer_corr = f"response_{response.corr}"
        send_marker(answer_corr)  # Function to send the LSL marker
        
        
        # check responses
        if response.keys in ['', [], None]:  # No response was made
            response.keys = None
            # was no response the correct answer?!
            if str(correct_resp).lower() == 'none':
               response.corr = 1;  # correct non-response
            else:
               response.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceTrials (TrialHandler)
        practiceTrials.addData('response.keys',response.keys)
        practiceTrials.addData('response.corr', response.corr)
        if response.keys != None:  # we had a response
            practiceTrials.addData('response.rt', response.rt)
            practiceTrials.addData('response.duration', response.duration)
        # the Routine "symbols" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1 repeats of 'practiceTrials'
    
    
    # --- Prepare to start Routine "startTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('startTask.started', globalClock.getTime(format='float'))
    InstructionsText2.setText('')
    go.keys = []
    go.rt = []
    _go_allKeys = []
    # Run 'Begin Routine' code from code_InstructionsText2
    # Set the text for the second set of instructions
    InstructionsText2.setText(instructions['Text_start_task'])
    # Run 'Begin Routine' code from define_block_rows
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_test = True
    # keep track of which components have finished
    startTaskComponents = [InstructionsText2, go]
    for thisComponent in startTaskComponents:
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
    
    # --- Run Routine "startTask" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *InstructionsText2* updates
        
        # if InstructionsText2 is starting this frame...
        if InstructionsText2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText2.frameNStart = frameN  # exact frame index
            InstructionsText2.tStart = t  # local t and not account for scr refresh
            InstructionsText2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText2.started')
            # update status
            InstructionsText2.status = STARTED
            InstructionsText2.setAutoDraw(True)
        
        # if InstructionsText2 is active this frame...
        if InstructionsText2.status == STARTED:
            # update params
            pass
        
        # *go* updates
        waitOnFlip = False
        
        # if go is starting this frame...
        if go.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            go.frameNStart = frameN  # exact frame index
            go.tStart = t  # local t and not account for scr refresh
            go.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(go, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'go.started')
            # update status
            go.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(go.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(go.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if go.status == STARTED and not waitOnFlip:
            theseKeys = go.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _go_allKeys.extend(theseKeys)
            if len(_go_allKeys):
                go.keys = _go_allKeys[-1].name  # just the last key pressed
                go.rt = _go_allKeys[-1].rt
                go.duration = _go_allKeys[-1].duration
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
        for thisComponent in startTaskComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "startTask" ---
    for thisComponent in startTaskComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('startTask.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_test_blocks
    send_marker("start_test_blocks")
    thisExp.nextEntry()
    # the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('symbols_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
        seed=None, name='testblocks')
    thisExp.addLoop(testblocks)  # add the loop to the experiment
    thisTestblock = testblocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTestblock.rgb)
    if thisTestblock != None:
        for paramName in thisTestblock:
            globals()[paramName] = thisTestblock[paramName]
    
    for thisTestblock in testblocks:
        currentLoop = testblocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTestblock.rgb)
        if thisTestblock != None:
            for paramName in thisTestblock:
                globals()[paramName] = thisTestblock[paramName]
        
        # --- Prepare to start Routine "block_counter" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block_counter.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from blockSetup
        # Increment block counter
        block_index += 1
        
        # Determine the current block type and number
        if block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
            # Skip the remaining test blocks
            testblocks.finished = True
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
        testTrials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('symbols_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
            seed=None, name='testTrials')
        thisExp.addLoop(testTrials)  # add the loop to the experiment
        thisTestTrial = testTrials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
        if thisTestTrial != None:
            for paramName in thisTestTrial:
                globals()[paramName] = thisTestTrial[paramName]
        
        for thisTestTrial in testTrials:
            currentLoop = testTrials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTestTrial.rgb)
            if thisTestTrial != None:
                for paramName in thisTestTrial:
                    globals()[paramName] = thisTestTrial[paramName]
            
            # --- Prepare to start Routine "pre_stim" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('pre_stim.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            pre_stimComponents = [nothing, text_cross, polygon]
            for thisComponent in pre_stimComponents:
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
            
            # --- Run Routine "pre_stim" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *nothing* updates
                
                # if nothing is starting this frame...
                if nothing.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    nothing.frameNStart = frameN  # exact frame index
                    nothing.tStart = t  # local t and not account for scr refresh
                    nothing.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(nothing, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'nothing.started')
                    # update status
                    nothing.status = STARTED
                    nothing.setAutoDraw(True)
                
                # if nothing is active this frame...
                if nothing.status == STARTED:
                    # update params
                    pass
                
                # if nothing is stopping this frame...
                if nothing.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        nothing.tStop = t  # not accounting for scr refresh
                        nothing.tStopRefresh = tThisFlipGlobal  # on global time
                        nothing.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'nothing.stopped')
                        # update status
                        nothing.status = FINISHED
                        nothing.setAutoDraw(False)
                
                # *text_cross* updates
                
                # if text_cross is starting this frame...
                if text_cross.status == NOT_STARTED and frameN >= 30:
                    # keep track of start time/frame for later
                    text_cross.frameNStart = frameN  # exact frame index
                    text_cross.tStart = t  # local t and not account for scr refresh
                    text_cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_cross.started')
                    # update status
                    text_cross.status = STARTED
                    text_cross.setAutoDraw(True)
                
                # if text_cross is active this frame...
                if text_cross.status == STARTED:
                    # update params
                    pass
                
                # if text_cross is stopping this frame...
                if text_cross.status == STARTED:
                    if frameN >= 60:
                        # keep track of stop time/frame for later
                        text_cross.tStop = t  # not accounting for scr refresh
                        text_cross.tStopRefresh = tThisFlipGlobal  # on global time
                        text_cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_cross.stopped')
                        # update status
                        text_cross.status = FINISHED
                        text_cross.setAutoDraw(False)
                
                # *polygon* updates
                
                # if polygon is starting this frame...
                if polygon.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    polygon.frameNStart = frameN  # exact frame index
                    polygon.tStart = t  # local t and not account for scr refresh
                    polygon.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon.started')
                    # update status
                    polygon.status = STARTED
                    polygon.setAutoDraw(True)
                
                # if polygon is active this frame...
                if polygon.status == STARTED:
                    # update params
                    pass
                
                # if polygon is stopping this frame...
                if polygon.status == STARTED:
                    if frameN >= (polygon.frameNStart + 60):
                        # keep track of stop time/frame for later
                        polygon.tStop = t  # not accounting for scr refresh
                        polygon.tStopRefresh = tThisFlipGlobal  # on global time
                        polygon.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'polygon.stopped')
                        # update status
                        polygon.status = FINISHED
                        polygon.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in pre_stimComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "pre_stim" ---
            for thisComponent in pre_stimComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('pre_stim.stopped', globalClock.getTime(format='float'))
            # the Routine "pre_stim" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "symbols" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('symbols.started', globalClock.getTime(format='float'))
            stim1.setImage(stimulus1)
            stim2.setImage(stimulus2)
            symbol1_img.setPos((-0.1, 0))
            symbol1_img.setImage(symbol1)
            symbol2_img.setPos((0.1, 0))
            symbol2_img.setImage(symbol2)
            symbol3_img.setPos((0.3, 0))
            symbol3_img.setImage(symbol3)
            symbol4_img.setPos((0.5, 0))
            symbol4_img.setImage(symbol4)
            symbol5_img.setPos((0.7, 0))
            symbol5_img.setImage(symbol5)
            # Run 'Begin Routine' code from LSL_stimulus_2
            marker = f"stimulus_trial_{trial}"
            send_marker(marker)
            response.keys = []
            response.rt = []
            _response_allKeys = []
            # keep track of which components have finished
            symbolsComponents = [stim1, stim2, symbol1_img, symbol2_img, symbol3_img, symbol4_img, symbol5_img, polygon_2, response]
            for thisComponent in symbolsComponents:
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
            
            # --- Run Routine "symbols" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *stim1* updates
                
                # if stim1 is starting this frame...
                if stim1.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    stim1.frameNStart = frameN  # exact frame index
                    stim1.tStart = t  # local t and not account for scr refresh
                    stim1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim1.started')
                    # update status
                    stim1.status = STARTED
                    stim1.setAutoDraw(True)
                
                # if stim1 is active this frame...
                if stim1.status == STARTED:
                    # update params
                    pass
                
                # *stim2* updates
                
                # if stim2 is starting this frame...
                if stim2.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    stim2.frameNStart = frameN  # exact frame index
                    stim2.tStart = t  # local t and not account for scr refresh
                    stim2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stim2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stim2.started')
                    # update status
                    stim2.status = STARTED
                    stim2.setAutoDraw(True)
                
                # if stim2 is active this frame...
                if stim2.status == STARTED:
                    # update params
                    pass
                
                # *symbol1_img* updates
                
                # if symbol1_img is starting this frame...
                if symbol1_img.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    symbol1_img.frameNStart = frameN  # exact frame index
                    symbol1_img.tStart = t  # local t and not account for scr refresh
                    symbol1_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symbol1_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'symbol1_img.started')
                    # update status
                    symbol1_img.status = STARTED
                    symbol1_img.setAutoDraw(True)
                
                # if symbol1_img is active this frame...
                if symbol1_img.status == STARTED:
                    # update params
                    pass
                
                # *symbol2_img* updates
                
                # if symbol2_img is starting this frame...
                if symbol2_img.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    symbol2_img.frameNStart = frameN  # exact frame index
                    symbol2_img.tStart = t  # local t and not account for scr refresh
                    symbol2_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symbol2_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'symbol2_img.started')
                    # update status
                    symbol2_img.status = STARTED
                    symbol2_img.setAutoDraw(True)
                
                # if symbol2_img is active this frame...
                if symbol2_img.status == STARTED:
                    # update params
                    pass
                
                # *symbol3_img* updates
                
                # if symbol3_img is starting this frame...
                if symbol3_img.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    symbol3_img.frameNStart = frameN  # exact frame index
                    symbol3_img.tStart = t  # local t and not account for scr refresh
                    symbol3_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symbol3_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'symbol3_img.started')
                    # update status
                    symbol3_img.status = STARTED
                    symbol3_img.setAutoDraw(True)
                
                # if symbol3_img is active this frame...
                if symbol3_img.status == STARTED:
                    # update params
                    pass
                
                # *symbol4_img* updates
                
                # if symbol4_img is starting this frame...
                if symbol4_img.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    symbol4_img.frameNStart = frameN  # exact frame index
                    symbol4_img.tStart = t  # local t and not account for scr refresh
                    symbol4_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symbol4_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'symbol4_img.started')
                    # update status
                    symbol4_img.status = STARTED
                    symbol4_img.setAutoDraw(True)
                
                # if symbol4_img is active this frame...
                if symbol4_img.status == STARTED:
                    # update params
                    pass
                
                # *symbol5_img* updates
                
                # if symbol5_img is starting this frame...
                if symbol5_img.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    symbol5_img.frameNStart = frameN  # exact frame index
                    symbol5_img.tStart = t  # local t and not account for scr refresh
                    symbol5_img.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(symbol5_img, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'symbol5_img.started')
                    # update status
                    symbol5_img.status = STARTED
                    symbol5_img.setAutoDraw(True)
                
                # if symbol5_img is active this frame...
                if symbol5_img.status == STARTED:
                    # update params
                    pass
                
                # *polygon_2* updates
                
                # if polygon_2 is starting this frame...
                if polygon_2.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    polygon_2.frameNStart = frameN  # exact frame index
                    polygon_2.tStart = t  # local t and not account for scr refresh
                    polygon_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(polygon_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'polygon_2.started')
                    # update status
                    polygon_2.status = STARTED
                    polygon_2.setAutoDraw(True)
                
                # if polygon_2 is active this frame...
                if polygon_2.status == STARTED:
                    # update params
                    pass
                
                # *response* updates
                waitOnFlip = False
                
                # if response is starting this frame...
                if response.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    response.frameNStart = frameN  # exact frame index
                    response.tStart = t  # local t and not account for scr refresh
                    response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response.started')
                    # update status
                    response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if response.status == STARTED and not waitOnFlip:
                    theseKeys = response.getKeys(keyList=['d','k'], ignoreKeys=None, waitRelease=False)
                    _response_allKeys.extend(theseKeys)
                    if len(_response_allKeys):
                        response.keys = _response_allKeys[-1].name  # just the last key pressed
                        response.rt = _response_allKeys[-1].rt
                        response.duration = _response_allKeys[-1].duration
                        # was this correct?
                        if (response.keys == str(correct_resp)) or (response.keys == correct_resp):
                            response.corr = 1
                        else:
                            response.corr = 0
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
                for thisComponent in symbolsComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "symbols" ---
            for thisComponent in symbolsComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('symbols.stopped', globalClock.getTime(format='float'))
            # Run 'End Routine' code from LSL_stimulus_2
            answer_corr = f"response_{response.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # check responses
            if response.keys in ['', [], None]:  # No response was made
                response.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   response.corr = 1;  # correct non-response
                else:
                   response.corr = 0;  # failed to respond (incorrectly)
            # store data for testTrials (TrialHandler)
            testTrials.addData('response.keys',response.keys)
            testTrials.addData('response.corr', response.corr)
            if response.keys != None:  # we had a response
                testTrials.addData('response.rt', response.rt)
                testTrials.addData('response.duration', response.duration)
            # the Routine "symbols" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'testTrials'
        
        
        # --- Prepare to start Routine "pause" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pause.started', globalClock.getTime(format='float'))
        InstructionsText3.setText("# Set the text for the third set of instructions\nInstructionsText3.text = instructions['Text3']\n")
        go2.keys = []
        go2.rt = []
        _go2_allKeys = []
        # Run 'Begin Routine' code from code_InstructionsText3
        # Set the text for the third set of instructions
        InstructionsText3.setText(instructions['Text_pause_between_blocks'])
        
        # Run 'Begin Routine' code from check_block_counter
        # Check if the block is test and block_n is to skip the loop
        if is_test and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
            testblocks.finished = True  # Skip the loop
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
        testblocks.addData('go2.keys',go2.keys)
        if go2.keys != None:  # we had a response
            testblocks.addData('go2.rt', go2.rt)
            testblocks.addData('go2.duration', go2.duration)
        # the Routine "pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'testblocks'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from LSL_Symbols_end
    send_marker('symbols_end')
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
