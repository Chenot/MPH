#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 10:42
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
expName = 'VAC'  # from the Builder filename that created this script
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Perception_visuo-auditory-conflict\\VAC_lastrun.py',
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
    if deviceManager.getDevice('startInst_2') is None:
        # initialise startInst_2
        startInst_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startInst_2',
        )
    if deviceManager.getDevice('key_response_practice') is None:
        # initialise key_response_practice
        key_response_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_response_practice',
        )
    if deviceManager.getDevice('go_2') is None:
        # initialise go_2
        go_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go_2',
        )
    if deviceManager.getDevice('go') is None:
        # initialise go
        go = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go',
        )
    if deviceManager.getDevice('key_response') is None:
        # initialise key_response
        key_response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_response',
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
    import pandas as pd
    import psychopy.logging as logging
    
    # Set logging level to WARNING to suppress INFO and DEBUG messages
    logging.console.setLevel(logging.WARNING)
    
    # Load the scenario CSV file
    scenario_df = pd.read_csv('visual_auditory_conflict_task_scenario.csv')
    
    # Filter the practice trials
    practice_indices = scenario_df.index[(scenario_df['block'] == 'practice')].tolist()
    selected_rows_practice = f"{practice_indices[0]}:{practice_indices[-1] + 1}" if practice_indices else ""
    
    # Run 'Begin Experiment' code from language
    # Check if expInfo exists and create the language variable
    if 'expInfo' not in globals():
        expInfo = {}
    
    # Set default values to English if it is missing from expInfo keys
    if 'language' not in expInfo:
        expInfo['language'] = 'English'
    
    # Create the language variable
    language = expInfo.get('language')
    
    if language == "English":
        instructions = {
            'name_task' : 'VISUAL-AUDITORY CONFLICT',
            'Text_instructions1': "Welcome to the Visual-Auditory Conflict task.\n\nIn this task, you will first need to focus on the fixation cross in the center of the screen.\nA circle will then appear on either the left or right side of the screen, while a tone will be simultaneously emitted in either the left or right speaker.\n\nYour goal is to respond to the visual stimulus (circle) in some trials and to the auditory stimulus (sound) in others.\n\nPress the spacebar to continue",
            'Text_instructions2': "Let's begin with practice.\n\nIn the practice, you will see which stimulus you need to respond with a word on the top of the screen (e.g. visual or auditory).\n\nPress 'd' when the stimulus is on the left, or 'k' when it is on the right.\n\nPress the spacebar to start the practice.",
            'Text_trainingover': "The training is now over.\nPress the spacebar to continue.",
            'Text_start_visualtask': "Now we shall begin with a visual block.\n\nIn this block, you should indicate the side where the circle appears, ignoring the sound.\nPress 'd' when it's on the left and 'k' when it's on the right.\nTry to be as quick and as accurate as possible.\n\nReady?\n\nPress the spacebar to start.",
            'Text_start_auditorytask': "We will now begin the auditory block.\n\nIn this block, you should indicate the side where the sound appears, ignoring the circle.\nPress 'd' when it's on the left and 'k' when it's on the right.\nTry to be as quick and as accurate as possible while keeping your EYES OPEN.\n\nReady?\n\nPress the spacebar to start.",
            'Text_end_task': "This task is now over.\n\nThank you!\n\nPress the space bar to continue"
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task' : 'CONFLIT VISUO-AUDITIF',
            'Text_instructions1': "Bienvenue dans la tâche de Conflit Visuo-Auditif.\n\nDans cette tâche, vous devrez d'abord vous concentrer sur la croix de fixation au centre de l'écran.\nUn cercle apparaîtra ensuite soit à gauche, soit à droite de l'écran, tandis qu'un son sera émis soit dans le haut-parleur gauche, soit dans le haut-parleur droit.\n\nVotre objectif est de répondre au stimulus visuel (cercle) dans certains essais et au stimulus auditif (son) dans d'autres.\n\nAppuez sur la barre d'espace pour continuer",
            'Text_instructions2': "Commençons par un entraînement.\n\nDans cet entraînement, vous verrez à quel stimulus vous devez répondre avec un mot en haut de l'écran (par exemple, visuel ou auditif).\n\nAppuyez sur 'd' quand le stimulus est à gauche, ou sur 'k' quand il est à droite.\n\nAppuyez sur la barre d'espace pour commencer l'entraînement.",
            'Text_trainingover': "L'entraînement est maintenant terminé.\nAppuyez sur la barre d'espace pour continuer.",
            'Text_start_visualtask': "Nous allons maintenant commencer par un bloc visuel.\n\nDans ce bloc, vous devez indiquer de quel côté le cercle apparaît, en ignorant le son. Appuyez sur 'd' quand il est à gauche et sur 'k' quand il est à droite.\nEssayez d'être aussi rapide et précis que possible.\n\nPrêt·e ?\n\nAppuyez sur la barre d'espace pour commencer.",
            'Text_start_auditorytask': "Pause\n\nNous allons maintenant commencer le bloc auditif.\n\nDans ce bloc, vous devez indiquer le côté où le son est entendu, en ignorant le cercle. Appuyez sur 'd' quand il est à gauche et sur 'k' quand il est à droite.\nEssayez d'être aussi rapide et précis que possible tout en gardant vos YEUX OUVERTS.\n\nPrêt·e ?\n\nAppuyez sur la barre d'espace pour commencer.",
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
    
    
    # --- Initialize components for Routine "instructions_practice1" ---
    startInst = keyboard.Keyboard(deviceName='startInst')
    InstructionsText = visual.TextStim(win=win, name='InstructionsText',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "instructions_practice2" ---
    startInst_2 = keyboard.Keyboard(deviceName='startInst_2')
    InstructionsText_2 = visual.TextStim(win=win, name='InstructionsText_2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    nametask_2 = visual.TextStim(win=win, name='nametask_2',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    # Run 'Begin Experiment' code from define_block_rows_practice
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_practice = True
    
    # --- Initialize components for Routine "ITI_practice" ---
    cross_ITI_practice = visual.TextStim(win=win, name='cross_ITI_practice',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_ITI_practice = visual.TextStim(win=win, name='text_ITI_practice',
        text=None,
        font='Arial',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "main_practice" ---
    cross_practice = visual.TextStim(win=win, name='cross_practice',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    visual_stim_practice = visual.ShapeStim(
        win=win, name='visual_stim_practice',
        size=(0.2, 0.2), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    key_response_practice = keyboard.Keyboard(deviceName='key_response_practice')
    # Run 'Begin Experiment' code from code_stimulus_practice
    # At the beginning of the experiment
    from psychopy import prefs
    prefs.hardware['audioLib'] = ['pyo']
    from psychopy import sound
    
    # Paths to the sound files
    left_sound_file = 'ressources/left.wav'
    right_sound_file = 'ressources/right.wav'
    
    # Load the sound files
    left_stim = sound.Sound(left_sound_file, stereo=True)
    right_stim = sound.Sound(right_sound_file, stereo=True)
    
    text_main_practice = visual.TextStim(win=win, name='text_main_practice',
        text=None,
        font='Arial',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "training_over" ---
    trainingover_text = visual.TextStim(win=win, name='trainingover_text',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go_2 = keyboard.Keyboard(deviceName='go_2')
    
    # --- Initialize components for Routine "block_counter" ---
    # Run 'Begin Experiment' code from LSL_start_testblock
    send_marker("start_VAC_block")
    
    # --- Initialize components for Routine "instructions_test" ---
    InstructionsTextTask = visual.TextStim(win=win, name='InstructionsTextTask',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go = keyboard.Keyboard(deviceName='go')
    
    # --- Initialize components for Routine "ITI" ---
    cross_ITI = visual.TextStim(win=win, name='cross_ITI',
        text='+',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "main" ---
    cross = visual.TextStim(win=win, name='cross',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    visual_stim = visual.ShapeStim(
        win=win, name='visual_stim',
        size=(0.2, 0.2), vertices='circle',
        ori=0.0, pos=[0,0], anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    key_response = keyboard.Keyboard(deviceName='key_response')
    # Run 'Begin Experiment' code from code_stimulus
    # At the beginning of the experiment
    from psychopy import prefs
    prefs.hardware['audioLib'] = ['pyo']
    from psychopy import sound
    
    # Paths to the sound files
    left_sound_file = 'ressources/left.wav'
    right_sound_file = 'ressources/right.wav'
    
    # Load the sound files
    left_stim = sound.Sound(left_sound_file, stereo=True)
    right_stim = sound.Sound(right_sound_file, stereo=True)
    
    
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
    
    # --- Prepare to start Routine "instructions_practice1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_practice1.started', globalClock.getTime(format='float'))
    startInst.keys = []
    startInst.rt = []
    _startInst_allKeys = []
    InstructionsText.setText('')
    # Run 'Begin Routine' code from code_InstructionsText
    # Set the text for the first set of instructions
    InstructionsText.setText(instructions['Text_instructions1'])
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # Run 'Begin Routine' code from LSL_start_VAC
    send_marker('VAC_start')
    # keep track of which components have finished
    instructions_practice1Components = [startInst, InstructionsText, nametask]
    for thisComponent in instructions_practice1Components:
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
    
    # --- Run Routine "instructions_practice1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *InstructionsText* updates
        
        # if InstructionsText is starting this frame...
        if InstructionsText.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText.frameNStart = frameN  # exact frame index
            InstructionsText.tStart = t  # local t and not account for scr refresh
            InstructionsText.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText.started')
            # update status
            InstructionsText.status = STARTED
            InstructionsText.setAutoDraw(True)
        
        # if InstructionsText is active this frame...
        if InstructionsText.status == STARTED:
            # update params
            pass
        
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
        for thisComponent in instructions_practice1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_practice1" ---
    for thisComponent in instructions_practice1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_practice1.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_VAC
    send_marker('VAC_practice_start')
    thisExp.nextEntry()
    # the Routine "instructions_practice1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_practice2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_practice2.started', globalClock.getTime(format='float'))
    startInst_2.keys = []
    startInst_2.rt = []
    _startInst_2_allKeys = []
    InstructionsText_2.setText('')
    # Run 'Begin Routine' code from code_InstructionsText_2
    # Set the text for the first set of instructions
    InstructionsText_2.setText(instructions['Text_instructions2'])
    # Run 'Begin Routine' code from code_nametask_2
    nametask_2.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions_practice2Components = [startInst_2, InstructionsText_2, nametask_2]
    for thisComponent in instructions_practice2Components:
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
    
    # --- Run Routine "instructions_practice2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
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
        
        # *InstructionsText_2* updates
        
        # if InstructionsText_2 is starting this frame...
        if InstructionsText_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsText_2.frameNStart = frameN  # exact frame index
            InstructionsText_2.tStart = t  # local t and not account for scr refresh
            InstructionsText_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsText_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsText_2.started')
            # update status
            InstructionsText_2.status = STARTED
            InstructionsText_2.setAutoDraw(True)
        
        # if InstructionsText_2 is active this frame...
        if InstructionsText_2.status == STARTED:
            # update params
            pass
        
        # *nametask_2* updates
        
        # if nametask_2 is starting this frame...
        if nametask_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            nametask_2.frameNStart = frameN  # exact frame index
            nametask_2.tStart = t  # local t and not account for scr refresh
            nametask_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(nametask_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'nametask_2.started')
            # update status
            nametask_2.status = STARTED
            nametask_2.setAutoDraw(True)
        
        # if nametask_2 is active this frame...
        if nametask_2.status == STARTED:
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
        for thisComponent in instructions_practice2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_practice2" ---
    for thisComponent in instructions_practice2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_practice2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instructions_practice2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceTrials = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('visual_auditory_conflict_task_scenario.csv', selection=selected_rows_practice),
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
        
        # --- Prepare to start Routine "ITI_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('ITI_practice.started', globalClock.getTime(format='float'))
        cross_ITI_practice.setText('+')
        text_ITI_practice.setText('')
        # Run 'Begin Routine' code from code_text_ITI_practice
        # Check if expInfo exists and create the language variable
        if 'expInfo' not in globals():
            expInfo = {}
        
        # Set default values to English if it is missing from expInfo keys
        if 'language' not in expInfo:
            expInfo['language'] = 'English'
        
        # Create the language variable
        language = expInfo.get('language')
        
        # Determine the block type for the current block
        current_block_type = scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)]['block_type'].values[0]
        
        if language == "English":
            if current_block_type == 'visual':
                text_ITI_practice.text = 'visual'
            elif current_block_type == 'auditory':
                text_ITI_practice.text = 'auditory'
        else:
            if current_block_type == 'visual':
                text_ITI_practice.text = 'visuel'
            elif current_block_type == 'auditory':
                text_ITI_practice.text = 'auditif'
        # keep track of which components have finished
        ITI_practiceComponents = [cross_ITI_practice, text_ITI_practice]
        for thisComponent in ITI_practiceComponents:
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
        
        # --- Run Routine "ITI_practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_ITI_practice* updates
            
            # if cross_ITI_practice is starting this frame...
            if cross_ITI_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                cross_ITI_practice.frameNStart = frameN  # exact frame index
                cross_ITI_practice.tStart = t  # local t and not account for scr refresh
                cross_ITI_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_ITI_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_ITI_practice.started')
                # update status
                cross_ITI_practice.status = STARTED
                cross_ITI_practice.setAutoDraw(True)
            
            # if cross_ITI_practice is active this frame...
            if cross_ITI_practice.status == STARTED:
                # update params
                pass
            
            # if cross_ITI_practice is stopping this frame...
            if cross_ITI_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross_ITI_practice.tStartRefresh + ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    cross_ITI_practice.tStop = t  # not accounting for scr refresh
                    cross_ITI_practice.tStopRefresh = tThisFlipGlobal  # on global time
                    cross_ITI_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_ITI_practice.stopped')
                    # update status
                    cross_ITI_practice.status = FINISHED
                    cross_ITI_practice.setAutoDraw(False)
            
            # *text_ITI_practice* updates
            
            # if text_ITI_practice is starting this frame...
            if text_ITI_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_ITI_practice.frameNStart = frameN  # exact frame index
                text_ITI_practice.tStart = t  # local t and not account for scr refresh
                text_ITI_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_ITI_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_ITI_practice.started')
                # update status
                text_ITI_practice.status = STARTED
                text_ITI_practice.setAutoDraw(True)
            
            # if text_ITI_practice is active this frame...
            if text_ITI_practice.status == STARTED:
                # update params
                pass
            
            # if text_ITI_practice is stopping this frame...
            if text_ITI_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > text_ITI_practice.tStartRefresh + ITI-frameTolerance:
                    # keep track of stop time/frame for later
                    text_ITI_practice.tStop = t  # not accounting for scr refresh
                    text_ITI_practice.tStopRefresh = tThisFlipGlobal  # on global time
                    text_ITI_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_ITI_practice.stopped')
                    # update status
                    text_ITI_practice.status = FINISHED
                    text_ITI_practice.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in ITI_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "ITI_practice" ---
        for thisComponent in ITI_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('ITI_practice.stopped', globalClock.getTime(format='float'))
        # the Routine "ITI_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "main_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('main_practice.started', globalClock.getTime(format='float'))
        cross_practice.setText('+')
        visual_stim_practice.setPos((0, 0))
        key_response_practice.keys = []
        key_response_practice.rt = []
        _key_response_practice_allKeys = []
        # Run 'Begin Routine' code from LSL_stimulus_practice
        marker = f"stimulus_{position_visual}_{position_auditory}_{congruence}"
        send_marker(marker)  # Function to send the LSL marker
        
        
        
        # Run 'Begin Routine' code from code_stimulus_practice
        # Set the position of the visual stimulus
        if position_visual == 'left':
            visual_stim_practice.pos = (-0.5, 0)
        else:
            visual_stim_practice.pos = (0.5, 0)
        
        # Play the appropriate auditory stimulus
        if position_auditory == 'left':
            left_stim.play()
        else:
            right_stim.play()
        
        text_main_practice.setText('')
        # Run 'Begin Routine' code from code_text_main_practice
        # Check if expInfo exists and create the language variable
        if 'expInfo' not in globals():
            expInfo = {}
        
        # Set default values to English if it is missing from expInfo keys
        if 'language' not in expInfo:
            expInfo['language'] = 'English'
        
        # Create the language variable
        language = expInfo.get('language')
        
        # Determine the block type for the current block
        current_block_type = scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)]['block_type'].values[0]
        
        if language == "English":
            if current_block_type == 'visual':
                text_main_practice.text = 'visual'
            elif current_block_type == 'auditory':
                text_main_practice.text = 'auditory'
        else:
            if current_block_type == 'visual':
                text_main_practice.text = 'visuel'
            elif current_block_type == 'auditory':
                text_main_practice.text = 'auditif'
        # keep track of which components have finished
        main_practiceComponents = [cross_practice, visual_stim_practice, key_response_practice, text_main_practice]
        for thisComponent in main_practiceComponents:
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
        
        # --- Run Routine "main_practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *cross_practice* updates
            
            # if cross_practice is starting this frame...
            if cross_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                cross_practice.frameNStart = frameN  # exact frame index
                cross_practice.tStart = t  # local t and not account for scr refresh
                cross_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(cross_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'cross_practice.started')
                # update status
                cross_practice.status = STARTED
                cross_practice.setAutoDraw(True)
            
            # if cross_practice is active this frame...
            if cross_practice.status == STARTED:
                # update params
                pass
            
            # *visual_stim_practice* updates
            
            # if visual_stim_practice is starting this frame...
            if visual_stim_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                visual_stim_practice.frameNStart = frameN  # exact frame index
                visual_stim_practice.tStart = t  # local t and not account for scr refresh
                visual_stim_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(visual_stim_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'visual_stim_practice.started')
                # update status
                visual_stim_practice.status = STARTED
                visual_stim_practice.setAutoDraw(True)
            
            # if visual_stim_practice is active this frame...
            if visual_stim_practice.status == STARTED:
                # update params
                pass
            
            # if visual_stim_practice is stopping this frame...
            if visual_stim_practice.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > visual_stim_practice.tStartRefresh + 0.2-frameTolerance:
                    # keep track of stop time/frame for later
                    visual_stim_practice.tStop = t  # not accounting for scr refresh
                    visual_stim_practice.tStopRefresh = tThisFlipGlobal  # on global time
                    visual_stim_practice.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'visual_stim_practice.stopped')
                    # update status
                    visual_stim_practice.status = FINISHED
                    visual_stim_practice.setAutoDraw(False)
            
            # *key_response_practice* updates
            waitOnFlip = False
            
            # if key_response_practice is starting this frame...
            if key_response_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                key_response_practice.frameNStart = frameN  # exact frame index
                key_response_practice.tStart = t  # local t and not account for scr refresh
                key_response_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(key_response_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'key_response_practice.started')
                # update status
                key_response_practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(key_response_practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(key_response_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if key_response_practice.status == STARTED and not waitOnFlip:
                theseKeys = key_response_practice.getKeys(keyList=['d','k'], ignoreKeys=None, waitRelease=False)
                _key_response_practice_allKeys.extend(theseKeys)
                if len(_key_response_practice_allKeys):
                    key_response_practice.keys = _key_response_practice_allKeys[0].name  # just the first key pressed
                    key_response_practice.rt = _key_response_practice_allKeys[0].rt
                    key_response_practice.duration = _key_response_practice_allKeys[0].duration
                    # was this correct?
                    if (key_response_practice.keys == str(correct_resp)) or (key_response_practice.keys == correct_resp):
                        key_response_practice.corr = 1
                    else:
                        key_response_practice.corr = 0
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_main_practice* updates
            
            # if text_main_practice is starting this frame...
            if text_main_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_main_practice.frameNStart = frameN  # exact frame index
                text_main_practice.tStart = t  # local t and not account for scr refresh
                text_main_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_main_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_main_practice.started')
                # update status
                text_main_practice.status = STARTED
                text_main_practice.setAutoDraw(True)
            
            # if text_main_practice is active this frame...
            if text_main_practice.status == STARTED:
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
            for thisComponent in main_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "main_practice" ---
        for thisComponent in main_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('main_practice.stopped', globalClock.getTime(format='float'))
        # check responses
        if key_response_practice.keys in ['', [], None]:  # No response was made
            key_response_practice.keys = None
            # was no response the correct answer?!
            if str(correct_resp).lower() == 'none':
               key_response_practice.corr = 1;  # correct non-response
            else:
               key_response_practice.corr = 0;  # failed to respond (incorrectly)
        # store data for practiceTrials (TrialHandler)
        practiceTrials.addData('key_response_practice.keys',key_response_practice.keys)
        practiceTrials.addData('key_response_practice.corr', key_response_practice.corr)
        if key_response_practice.keys != None:  # we had a response
            practiceTrials.addData('key_response_practice.rt', key_response_practice.rt)
            practiceTrials.addData('key_response_practice.duration', key_response_practice.duration)
        # Run 'End Routine' code from LSL_stimulus_practice
        answer_corr = f"response_{key_response.corr}"
        send_marker(answer_corr)  # Function to send the LSL marker
        
        
        # the Routine "main_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'practiceTrials'
    
    
    # --- Prepare to start Routine "training_over" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('training_over.started', globalClock.getTime(format='float'))
    trainingover_text.setText('')
    go_2.keys = []
    go_2.rt = []
    _go_2_allKeys = []
    # Run 'Begin Routine' code from code_trainingover_text
    trainingover_text.text = instructions['Text_trainingover']
    
    # Run 'Begin Routine' code from define_block_rows
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_test = True
    # keep track of which components have finished
    training_overComponents = [trainingover_text, go_2]
    for thisComponent in training_overComponents:
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
    
    # --- Run Routine "training_over" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *trainingover_text* updates
        
        # if trainingover_text is starting this frame...
        if trainingover_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            trainingover_text.frameNStart = frameN  # exact frame index
            trainingover_text.tStart = t  # local t and not account for scr refresh
            trainingover_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(trainingover_text, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'trainingover_text.started')
            # update status
            trainingover_text.status = STARTED
            trainingover_text.setAutoDraw(True)
        
        # if trainingover_text is active this frame...
        if trainingover_text.status == STARTED:
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
        if thisExp.status == FINISHED or endExpNow:
            endExperiment(thisExp, win=win)
            return
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            routineForceEnded = True
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in training_overComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "training_over" ---
    for thisComponent in training_overComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('training_over.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "training_over" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('visual_auditory_conflict_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        # block_type = 'test'
        if block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
            # Skip the remaining test blocks
            testblocks.finished = True
            continueRoutine = False
        else:
            block_n = block_index  # block_n in CSV starts from 1
        
        
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
        
        # --- Prepare to start Routine "instructions_test" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructions_test.started', globalClock.getTime(format='float'))
        InstructionsTextTask.setText('')
        go.keys = []
        go.rt = []
        _go_allKeys = []
        # Run 'Begin Routine' code from code_Instructions
        # Extract block_type for the current block
        current_block_type = scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)]['block_type'].values[0]
        
        # Set the instruction text based on the block type
        if current_block_type == 'visual':
            InstructionsTextTask.text = instructions['Text_start_visualtask']
        elif current_block_type == 'auditory':
            InstructionsTextTask.text = instructions['Text_start_auditorytask']
        
        
        
        # keep track of which components have finished
        instructions_testComponents = [InstructionsTextTask, go]
        for thisComponent in instructions_testComponents:
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
        
        # --- Run Routine "instructions_test" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *InstructionsTextTask* updates
            
            # if InstructionsTextTask is starting this frame...
            if InstructionsTextTask.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                InstructionsTextTask.frameNStart = frameN  # exact frame index
                InstructionsTextTask.tStart = t  # local t and not account for scr refresh
                InstructionsTextTask.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstructionsTextTask, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionsTextTask.started')
                # update status
                InstructionsTextTask.status = STARTED
                InstructionsTextTask.setAutoDraw(True)
            
            # if InstructionsTextTask is active this frame...
            if InstructionsTextTask.status == STARTED:
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
            for thisComponent in instructions_testComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "instructions_test" ---
        for thisComponent in instructions_testComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('instructions_test.stopped', globalClock.getTime(format='float'))
        # the Routine "instructions_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        testTrials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('visual_auditory_conflict_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "ITI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ITI.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            ITIComponents = [cross_ITI]
            for thisComponent in ITIComponents:
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
            
            # --- Run Routine "ITI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cross_ITI* updates
                
                # if cross_ITI is starting this frame...
                if cross_ITI.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    cross_ITI.frameNStart = frameN  # exact frame index
                    cross_ITI.tStart = t  # local t and not account for scr refresh
                    cross_ITI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross_ITI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross_ITI.started')
                    # update status
                    cross_ITI.status = STARTED
                    cross_ITI.setAutoDraw(True)
                
                # if cross_ITI is active this frame...
                if cross_ITI.status == STARTED:
                    # update params
                    pass
                
                # if cross_ITI is stopping this frame...
                if cross_ITI.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cross_ITI.tStartRefresh + ITI-frameTolerance:
                        # keep track of stop time/frame for later
                        cross_ITI.tStop = t  # not accounting for scr refresh
                        cross_ITI.tStopRefresh = tThisFlipGlobal  # on global time
                        cross_ITI.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cross_ITI.stopped')
                        # update status
                        cross_ITI.status = FINISHED
                        cross_ITI.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ITIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ITI" ---
            for thisComponent in ITIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ITI.stopped', globalClock.getTime(format='float'))
            # the Routine "ITI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('main.started', globalClock.getTime(format='float'))
            cross.setText('+')
            visual_stim.setPos((0, 0))
            key_response.keys = []
            key_response.rt = []
            _key_response_allKeys = []
            # Run 'Begin Routine' code from LSL_stimulus
            marker = f"stimulus_{position_visual}_{position_auditory}_{congruence}"
            send_marker(marker)  # Function to send the LSL marker
            
            
            
            # Run 'Begin Routine' code from code_stimulus
            # Set the position of the visual stimulus
            if position_visual == 'left':
                visual_stim.pos = (-0.5, 0)
            else:
                visual_stim.pos = (0.5, 0)
            
            # Play the appropriate auditory stimulus
            if position_auditory == 'left':
                left_stim.play()
            else:
                right_stim.play()
            
            # keep track of which components have finished
            mainComponents = [cross, visual_stim, key_response]
            for thisComponent in mainComponents:
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
            
            # --- Run Routine "main" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *cross* updates
                
                # if cross is starting this frame...
                if cross.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    cross.frameNStart = frameN  # exact frame index
                    cross.tStart = t  # local t and not account for scr refresh
                    cross.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(cross, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.started')
                    # update status
                    cross.status = STARTED
                    cross.setAutoDraw(True)
                
                # if cross is active this frame...
                if cross.status == STARTED:
                    # update params
                    pass
                
                # *visual_stim* updates
                
                # if visual_stim is starting this frame...
                if visual_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    visual_stim.frameNStart = frameN  # exact frame index
                    visual_stim.tStart = t  # local t and not account for scr refresh
                    visual_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(visual_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'visual_stim.started')
                    # update status
                    visual_stim.status = STARTED
                    visual_stim.setAutoDraw(True)
                
                # if visual_stim is active this frame...
                if visual_stim.status == STARTED:
                    # update params
                    pass
                
                # if visual_stim is stopping this frame...
                if visual_stim.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > visual_stim.tStartRefresh + 0.2-frameTolerance:
                        # keep track of stop time/frame for later
                        visual_stim.tStop = t  # not accounting for scr refresh
                        visual_stim.tStopRefresh = tThisFlipGlobal  # on global time
                        visual_stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'visual_stim.stopped')
                        # update status
                        visual_stim.status = FINISHED
                        visual_stim.setAutoDraw(False)
                
                # *key_response* updates
                waitOnFlip = False
                
                # if key_response is starting this frame...
                if key_response.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    key_response.frameNStart = frameN  # exact frame index
                    key_response.tStart = t  # local t and not account for scr refresh
                    key_response.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(key_response, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'key_response.started')
                    # update status
                    key_response.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(key_response.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(key_response.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if key_response.status == STARTED and not waitOnFlip:
                    theseKeys = key_response.getKeys(keyList=['d','k'], ignoreKeys=None, waitRelease=False)
                    _key_response_allKeys.extend(theseKeys)
                    if len(_key_response_allKeys):
                        key_response.keys = _key_response_allKeys[0].name  # just the first key pressed
                        key_response.rt = _key_response_allKeys[0].rt
                        key_response.duration = _key_response_allKeys[0].duration
                        # was this correct?
                        if (key_response.keys == str(correct_resp)) or (key_response.keys == correct_resp):
                            key_response.corr = 1
                        else:
                            key_response.corr = 0
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
                for thisComponent in mainComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "main" ---
            for thisComponent in mainComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('main.stopped', globalClock.getTime(format='float'))
            # check responses
            if key_response.keys in ['', [], None]:  # No response was made
                key_response.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   key_response.corr = 1;  # correct non-response
                else:
                   key_response.corr = 0;  # failed to respond (incorrectly)
            # store data for testTrials (TrialHandler)
            testTrials.addData('key_response.keys',key_response.keys)
            testTrials.addData('key_response.corr', key_response.corr)
            if key_response.keys != None:  # we had a response
                testTrials.addData('key_response.rt', key_response.rt)
                testTrials.addData('key_response.duration', key_response.duration)
            # Run 'End Routine' code from LSL_stimulus
            answer_corr = f"response_{key_response.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # the Routine "main" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'testTrials'
        
    # completed 1.0 repeats of 'testblocks'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
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
    # Run 'End Routine' code from LSL_VAC_end
    send_marker('VAC_end')
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
