#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 17:59
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
expName = 'TowerOfHanoi'  # from the Builder filename that created this script
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Planning_TowerOfHanoi\\TowerOfHanoi_lastrun.py',
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
    if deviceManager.getDevice('StartPractice') is None:
        # initialise StartPractice
        StartPractice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='StartPractice',
        )
    if deviceManager.getDevice('StartTest') is None:
        # initialise StartTest
        StartTest = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='StartTest',
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
    # Run 'Begin Experiment' code from logging
    import psychopy.logging as logging
    
    # Set logging level to WARNING to suppress INFO and DEBUG messages
    logging.console.setLevel(logging.WARNING)
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
            'name_task' : 'TOWER OF HANOI',
            'Text_instructions': (
                "Welcome to the Tower of Hanoi task.\n\n\n"
                "The goal of this task is to move disks in a rod from a start position to an end position (see example below), following these rules:\n\n"
                "1. You can only move one disk at a time.\n"
                "2. You can only move the top disk of any rod.\n"
                "3. No disk may be placed on top of a smaller disk.\n\n"
                "The goal is to complete the task in the FEWEST number of moves possible.\n\n"
                "Press the space bar to continue."
            ),
            'Text_tower_start' : "Start position",
            'Text_tower_end' : "End position",
            'Text_practice': (
                "You will now practice with a 3-disk example.\n\n"
                "Using the mouse, try to move all the disks to the end position following the rules explained earlier.\n\n"
                "Press the space bar to begin the practice trial."
            ),
            'Text_MinMoves' : "Minimal number of moves: ",
            'Text_nMoves' : "Number of moves: ",
            'Text_puzzle' : "Puzzle ",
            'Text_start_task': (
                "The training is now over.\n\n"
                "We will now start the actual task wich will always contains 4 disks.\n"
                "It will be constituted of 22 trials with a time limit of 90 second per trial.\n\n"
                "Remember that the goal is to complete the task in the FEWEST number of moves.\n"
                "So try to plan mentally before moving the disks to make as few moves as possible.\n\n"
                "Press the space bar to begin the task."
            ),
            'Text_end_task': (
                "This task is now over.\n\nThank you!\n\nPress the space bar to continue"
            )
        }
    else: 
        instructions = {
            'name_task' : 'TOUR DE HANOI',
            'Text_instructions': (
                "Bienvenue dans la tâche de la Tour de Hanoï.\n\n\n"
                "Le but de cette tâche est de déplacer les disques d'une tour d'une position de départ à une position de fin (voir exemple ci-dessous), en suivant ces règles:\n\n"
                "1. Vous ne pouvez déplacer qu'un seul disque à la fois.\n"
                "2. Vous ne pouvez déplacer que le disque supérieur de chaque tour.\n"
                "3. Aucun disque ne peut être placé sur un disque plus petit.\n\n"
                "L'objectif est de compléter la tâche avec le MOINS de mouvements possible.\n\n"
                "Appuyez sur la barre d'espace pour continuer."
            ),
            'Text_tower_start': "Position de départ",
            'Text_tower_end': "Position de fin",
            'Text_practice': (
                "Vous allez maintenant vous entraîner avec un exemple à 3 disques.\n\n"
                "En utilisant la souris, essayez de déplacer tous les disques vers la position de fin en suivant les règles expliquées précédemment.\n\n"
                "Appuyez sur la barre d'espace pour commencer l'entraînement."
            ),
            'Text_MinMoves': "Nombre minimal de mouvements: ",
            'Text_nMoves': "Nombre de mouvements: ",
            'Text_puzzle': "Puzzle ",
            'Text_start_task': (
                "L'entraînement est maintenant terminé.\n\n"
                "Nous allons maintenant commencer la tâche réelle qui contiendra toujours 4 disques.\n"
                "Elle sera constituée de 22 essais avec une limite de temps de 90 secondes par essai.\n\n"
                "N'oubliez pas que l'objectif est de compléter la tâche avec le MOINS de mouvements possible.\n"
                "Essayez donc de planifier mentalement avant de déplacer les disques pour faire le moins de mouvements possible.\n\n"
                "Appuyez sur la barre d'espace pour commencer la tâche."
            ),
            'Text_end_task': (
                "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer"
            )
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
    
    
    # --- Initialize components for Routine "instructions_global" ---
    InstructionsText1 = visual.TextStim(win=win, name='InstructionsText1',
        text=None,
        font='Arial',
        units='height', pos=(0, 0.15), height=0.03, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    InstructionsTowerStart = visual.TextStim(win=win, name='InstructionsTowerStart',
        text=None,
        font='Arial',
        units='height', pos=(-0.45, -0.2), height=0.03, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-1.0);
    InstructionsTowerEnd = visual.TextStim(win=win, name='InstructionsTowerEnd',
        text=None,
        font='Arial',
        units='height', pos=(0.45, -0.2), height=0.03, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-2.0);
    tower_instruction_start_img = visual.ImageStim(
        win=win,
        name='tower_instruction_start_img', 
        image='ressources/instruction_tower_start.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.45, -0.35), size=(0.781, 0.2424),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-6.0)
    tower_instruction_end_img = visual.ImageStim(
        win=win,
        name='tower_instruction_end_img', 
        image='ressources/instruction_tower_end.png', mask=None, anchor='center',
        ori=0.0, pos=(0.45, -0.35), size=(0.781, 0.2424),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-7.0)
    arrow = visual.ShapeStim(
        win=win, name='arrow', vertices='arrow',
        size=(0.1,0.1),
        ori=90.0, pos=(0, -0.35), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-8.0, interpolate=True)
    startInst = keyboard.Keyboard(deviceName='startInst')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-12.0);
    
    # --- Initialize components for Routine "instructions_practice" ---
    Instructions_TextPractice = visual.TextStim(win=win, name='Instructions_TextPractice',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.03, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    StartPractice = keyboard.Keyboard(deviceName='StartPractice')
    nametask_2 = visual.TextStim(win=win, name='nametask_2',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "towertask" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    towers = visual.ImageStim(
        win=win,
        name='towers', 
        image='ressources/towers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(1.8, 1.06),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    disk1 = visual.ImageStim(
        win=win,
        name='disk1', 
        image='ressources/disk1.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.24, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    disk2 = visual.ImageStim(
        win=win,
        name='disk2', 
        image='ressources/disk2.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.18, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    disk3 = visual.ImageStim(
        win=win,
        name='disk3', 
        image='ressources/disk3.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.12, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    disk4 = visual.ImageStim(
        win=win,
        name='disk4', 
        image='ressources/disk4.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.06, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    # Run 'Begin Experiment' code from code_movingdisks
    # Define target positions
    tower_positions = {
        'J1': (-0.5, -0.290), 'J2': (-0.5, -0.254), 'J3': (-0.5, -0.218), 'J4': (-0.5, -0.182),
        'K1': (0, -0.290), 'K2': (0, -0.254), 'K3': (0, -0.218), 'K4': (0, -0.182),
        'L1': (0.5, -0.290), 'L2': (0.5, -0.254), 'L3': (0.5, -0.218), 'L4': (0.5, -0.182),
        'nodisk' : (2, 2)
    }
    
    # Initialize tower stacks
    tower_stacks = {
        'J': [],
        'K': [],
        'L': []
    }
    
    selected_disk = None
    original_tower = None
    
    # Run 'Begin Experiment' code from code_targetdisks
    # Define coordinates for target disk positions
    tower_target_positions = {
        'J1': (-0.25, 0.204), 'J2': (-0.25, 0.222), 'J3': (-0.25, 0.240), 'J4': (-0.25, 0.258),
        'K1': (0, 0.204), 'K2': (0, 0.222), 'K3': (0, 0.240), 'K4': (0, 0.258),
        'L1': (0.25, 0.204), 'L2': (0.25, 0.222), 'L3': (0.25, 0.240), 'L4': (0.25, 0.258),
        'nodisk' : (2, 2)
    }
    
    # Initialize tower stacks
    tower_target_stacks = {
        'J': [],
        'K': [],
        'L': []
    }
    
    towers_target = visual.ImageStim(
        win=win,
        name='towers_target', 
        image='ressources/towers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.3), size=(0.9, 0.53),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    disk1target = visual.ImageStim(
        win=win,
        name='disk1target', 
        image='ressources/disk1.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.12, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    disk2target = visual.ImageStim(
        win=win,
        name='disk2target', 
        image='ressources/disk2.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.09, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    disk3target = visual.ImageStim(
        win=win,
        name='disk3target', 
        image='ressources/disk3.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.06, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    disk4target = visual.ImageStim(
        win=win,
        name='disk4target', 
        image='ressources/disk4.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.03, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    square_target = visual.Rect(
        win=win, name='square_target',
        width=(0.7, 0.3)[0], height=(0.7, 0.3)[1],
        ori=0.0, pos=(0, 0.3), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    text_min_moves = visual.TextStim(win=win, name='text_min_moves',
        text=None,
        font='Arial',
        pos=(0, 0.42), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    text_timer = visual.TextStim(win=win, name='text_timer',
        text=None,
        font='Arial',
        pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    # Run 'Begin Experiment' code from code_text_timer
    # Initialize the timer (in seconds)
    timer_task = 90
    move_counter_text = visual.TextStim(win=win, name='move_counter_text',
        text=None,
        font='Arial',
        pos=(0, 0.075), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    
    # --- Initialize components for Routine "startTask" ---
    InstructionsText2 = visual.TextStim(win=win, name='InstructionsText2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from initialize_trial_index_test
    # Initialize trial variables
    trial_index = 0  # Start with the first block for test
    is_practice = False
    is_test = True
    StartTest = keyboard.Keyboard(deviceName='StartTest')
    
    # --- Initialize components for Routine "Npuzzle" ---
    TextPuzzle = visual.TextStim(win=win, name='TextPuzzle',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    
    # --- Initialize components for Routine "towertask" ---
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    towers = visual.ImageStim(
        win=win,
        name='towers', 
        image='ressources/towers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, -0.1), size=(1.8, 1.06),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    disk1 = visual.ImageStim(
        win=win,
        name='disk1', 
        image='ressources/disk1.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.24, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    disk2 = visual.ImageStim(
        win=win,
        name='disk2', 
        image='ressources/disk2.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.18, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    disk3 = visual.ImageStim(
        win=win,
        name='disk3', 
        image='ressources/disk3.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.12, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    disk4 = visual.ImageStim(
        win=win,
        name='disk4', 
        image='ressources/disk4.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.06, 0.036),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-5.0)
    # Run 'Begin Experiment' code from code_movingdisks
    # Define target positions
    tower_positions = {
        'J1': (-0.5, -0.290), 'J2': (-0.5, -0.254), 'J3': (-0.5, -0.218), 'J4': (-0.5, -0.182),
        'K1': (0, -0.290), 'K2': (0, -0.254), 'K3': (0, -0.218), 'K4': (0, -0.182),
        'L1': (0.5, -0.290), 'L2': (0.5, -0.254), 'L3': (0.5, -0.218), 'L4': (0.5, -0.182),
        'nodisk' : (2, 2)
    }
    
    # Initialize tower stacks
    tower_stacks = {
        'J': [],
        'K': [],
        'L': []
    }
    
    selected_disk = None
    original_tower = None
    
    # Run 'Begin Experiment' code from code_targetdisks
    # Define coordinates for target disk positions
    tower_target_positions = {
        'J1': (-0.25, 0.204), 'J2': (-0.25, 0.222), 'J3': (-0.25, 0.240), 'J4': (-0.25, 0.258),
        'K1': (0, 0.204), 'K2': (0, 0.222), 'K3': (0, 0.240), 'K4': (0, 0.258),
        'L1': (0.25, 0.204), 'L2': (0.25, 0.222), 'L3': (0.25, 0.240), 'L4': (0.25, 0.258),
        'nodisk' : (2, 2)
    }
    
    # Initialize tower stacks
    tower_target_stacks = {
        'J': [],
        'K': [],
        'L': []
    }
    
    towers_target = visual.ImageStim(
        win=win,
        name='towers_target', 
        image='ressources/towers.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0.3), size=(0.9, 0.53),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    disk1target = visual.ImageStim(
        win=win,
        name='disk1target', 
        image='ressources/disk1.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.12, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    disk2target = visual.ImageStim(
        win=win,
        name='disk2target', 
        image='ressources/disk2.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.09, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-10.0)
    disk3target = visual.ImageStim(
        win=win,
        name='disk3target', 
        image='ressources/disk3.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.06, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-11.0)
    disk4target = visual.ImageStim(
        win=win,
        name='disk4target', 
        image='ressources/disk4.png', mask=None, anchor='center',
        ori=0.0, pos=None, size=(0.03, 0.018),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-12.0)
    square_target = visual.Rect(
        win=win, name='square_target',
        width=(0.7, 0.3)[0], height=(0.7, 0.3)[1],
        ori=0.0, pos=(0, 0.3), anchor='center',
        lineWidth=2.0,     colorSpace='rgb',  lineColor='white', fillColor=None,
        opacity=None, depth=-13.0, interpolate=True)
    text_min_moves = visual.TextStim(win=win, name='text_min_moves',
        text=None,
        font='Arial',
        pos=(0, 0.42), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-14.0);
    text_timer = visual.TextStim(win=win, name='text_timer',
        text=None,
        font='Arial',
        pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-16.0);
    # Run 'Begin Experiment' code from code_text_timer
    # Initialize the timer (in seconds)
    timer_task = 90
    move_counter_text = visual.TextStim(win=win, name='move_counter_text',
        text=None,
        font='Arial',
        pos=(0, 0.075), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-18.0);
    
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
        # Run 'Each Frame' code from ActivateMouse
        event.Mouse(visible=True)
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
    
    # --- Prepare to start Routine "instructions_global" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_global.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_InstructionsText1
    # Set the text for the first set of instructions
    InstructionsText1.setText(instructions['Text_instructions'])
    
    # Run 'Begin Routine' code from code_InstructionsTowerStart
    # Set the text for instructions
    InstructionsTowerStart.setText(instructions['Text_tower_start'])
    # Run 'Begin Routine' code from code_InstructionsTowerEnd
    # Set the text for instructions
    InstructionsTowerEnd.setText(instructions['Text_tower_end'])
    # Run 'Begin Routine' code from LSL_TOH_start
    send_marker('TOH_start')
    startInst.keys = []
    startInst.rt = []
    _startInst_allKeys = []
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions_globalComponents = [InstructionsText1, InstructionsTowerStart, InstructionsTowerEnd, tower_instruction_start_img, tower_instruction_end_img, arrow, startInst, nametask]
    for thisComponent in instructions_globalComponents:
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
    
    # --- Run Routine "instructions_global" ---
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
        
        # *InstructionsTowerStart* updates
        
        # if InstructionsTowerStart is starting this frame...
        if InstructionsTowerStart.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsTowerStart.frameNStart = frameN  # exact frame index
            InstructionsTowerStart.tStart = t  # local t and not account for scr refresh
            InstructionsTowerStart.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsTowerStart, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsTowerStart.started')
            # update status
            InstructionsTowerStart.status = STARTED
            InstructionsTowerStart.setAutoDraw(True)
        
        # if InstructionsTowerStart is active this frame...
        if InstructionsTowerStart.status == STARTED:
            # update params
            pass
        
        # *InstructionsTowerEnd* updates
        
        # if InstructionsTowerEnd is starting this frame...
        if InstructionsTowerEnd.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            InstructionsTowerEnd.frameNStart = frameN  # exact frame index
            InstructionsTowerEnd.tStart = t  # local t and not account for scr refresh
            InstructionsTowerEnd.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(InstructionsTowerEnd, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'InstructionsTowerEnd.started')
            # update status
            InstructionsTowerEnd.status = STARTED
            InstructionsTowerEnd.setAutoDraw(True)
        
        # if InstructionsTowerEnd is active this frame...
        if InstructionsTowerEnd.status == STARTED:
            # update params
            pass
        
        # *tower_instruction_start_img* updates
        
        # if tower_instruction_start_img is starting this frame...
        if tower_instruction_start_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tower_instruction_start_img.frameNStart = frameN  # exact frame index
            tower_instruction_start_img.tStart = t  # local t and not account for scr refresh
            tower_instruction_start_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tower_instruction_start_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tower_instruction_start_img.started')
            # update status
            tower_instruction_start_img.status = STARTED
            tower_instruction_start_img.setAutoDraw(True)
        
        # if tower_instruction_start_img is active this frame...
        if tower_instruction_start_img.status == STARTED:
            # update params
            pass
        
        # *tower_instruction_end_img* updates
        
        # if tower_instruction_end_img is starting this frame...
        if tower_instruction_end_img.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            tower_instruction_end_img.frameNStart = frameN  # exact frame index
            tower_instruction_end_img.tStart = t  # local t and not account for scr refresh
            tower_instruction_end_img.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(tower_instruction_end_img, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'tower_instruction_end_img.started')
            # update status
            tower_instruction_end_img.status = STARTED
            tower_instruction_end_img.setAutoDraw(True)
        
        # if tower_instruction_end_img is active this frame...
        if tower_instruction_end_img.status == STARTED:
            # update params
            pass
        
        # *arrow* updates
        
        # if arrow is starting this frame...
        if arrow.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            arrow.frameNStart = frameN  # exact frame index
            arrow.tStart = t  # local t and not account for scr refresh
            arrow.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(arrow, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'arrow.started')
            # update status
            arrow.status = STARTED
            arrow.setAutoDraw(True)
        
        # if arrow is active this frame...
        if arrow.status == STARTED:
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
        for thisComponent in instructions_globalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_global" ---
    for thisComponent in instructions_globalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_global.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instructions_global" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions_practice" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions_practice.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_Instructions_TextPractice
    # Set the text for the first set of instructions
    Instructions_TextPractice.setText(instructions['Text_practice'])
    StartPractice.keys = []
    StartPractice.rt = []
    _StartPractice_allKeys = []
    # Run 'Begin Routine' code from code_nametask_2
    nametask_2.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions_practiceComponents = [Instructions_TextPractice, StartPractice, nametask_2]
    for thisComponent in instructions_practiceComponents:
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
    
    # --- Run Routine "instructions_practice" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *Instructions_TextPractice* updates
        
        # if Instructions_TextPractice is starting this frame...
        if Instructions_TextPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            Instructions_TextPractice.frameNStart = frameN  # exact frame index
            Instructions_TextPractice.tStart = t  # local t and not account for scr refresh
            Instructions_TextPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(Instructions_TextPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'Instructions_TextPractice.started')
            # update status
            Instructions_TextPractice.status = STARTED
            Instructions_TextPractice.setAutoDraw(True)
        
        # if Instructions_TextPractice is active this frame...
        if Instructions_TextPractice.status == STARTED:
            # update params
            pass
        
        # *StartPractice* updates
        waitOnFlip = False
        
        # if StartPractice is starting this frame...
        if StartPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StartPractice.frameNStart = frameN  # exact frame index
            StartPractice.tStart = t  # local t and not account for scr refresh
            StartPractice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StartPractice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StartPractice.started')
            # update status
            StartPractice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(StartPractice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(StartPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if StartPractice.status == STARTED and not waitOnFlip:
            theseKeys = StartPractice.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _StartPractice_allKeys.extend(theseKeys)
            if len(_StartPractice_allKeys):
                StartPractice.keys = _StartPractice_allKeys[-1].name  # just the last key pressed
                StartPractice.rt = _StartPractice_allKeys[-1].rt
                StartPractice.duration = _StartPractice_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
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
        for thisComponent in instructions_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions_practice" ---
    for thisComponent in instructions_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions_practice.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_start_practice
    send_marker('practice')
    thisExp.nextEntry()
    # the Routine "instructions_practice" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('scenario_TowerOfHanoi.csv', selection='0'),
        seed=None, name='practice')
    thisExp.addLoop(practice)  # add the loop to the experiment
    thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            globals()[paramName] = thisPractice[paramName]
    
    for thisPractice in practice:
        currentLoop = practice
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
        if thisPractice != None:
            for paramName in thisPractice:
                globals()[paramName] = thisPractice[paramName]
        
        # --- Prepare to start Routine "towertask" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('towertask.started', globalClock.getTime(format='float'))
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_movingdisks
        # Initialize move counter
        move_counter = 0
        move_counter_text.setText("Number of moves: " + str(move_counter))
        
        # Recuperate initial disk positions
        disk_positions = {
            'disk1': disk1_init,
            'disk2': disk2_init,
            'disk3': disk3_init,
            'disk4': disk4_init
        }
        
        # Update tower stacks based on initial positions
        tower_stacks = {'J': [], 'K': [], 'L': []}
        for disk, pos_label in disk_positions.items():
            pos = tower_positions[pos_label]
            if pos[0] == -0.5:
                tower_stacks['J'].append(disk)
            elif pos[0] == 0:
                tower_stacks['K'].append(disk)
            elif pos[0] == 0.5:
                tower_stacks['L'].append(disk)
        
        # Ensure the disks are ordered correctly in the stacks
        for key in tower_stacks:
            tower_stacks[key] = sorted(tower_stacks[key], key=lambda d: tower_positions[disk_positions[d]][1])
        
        # Set disk positions
        disk1.setPos(tower_positions[disk_positions['disk1']])
        disk2.setPos(tower_positions[disk_positions['disk2']])
        disk3.setPos(tower_positions[disk_positions['disk3']])
        disk4.setPos(tower_positions[disk_positions['disk4']])
        # Run 'Begin Routine' code from code_targetdisks
        # Recuperate initial disk positions
        disk_target_positions = {
            'disk1': disk1_target,
            'disk2': disk2_target,
            'disk3': disk3_target,
            'disk4': disk4_target
        }
        
        # Update tower stacks based on initial positions
        tower_target_stacks = {'J': [], 'K': [], 'L': []}
        for disk, pos_label in disk_target_positions.items():
            pos = tower_target_positions[pos_label]
            if pos[0] == -0.25:
                tower_target_stacks['J'].append(disk)
            elif pos[0] == 0:
                tower_target_stacks['K'].append(disk)
            elif pos[0] == 0.25:
                tower_target_stacks['L'].append(disk)
        
        
        # Set disk positions
        disk1target.setPos(tower_target_positions[disk_target_positions['disk1']])
        disk2target.setPos(tower_target_positions[disk_target_positions['disk2']])
        disk3target.setPos(tower_target_positions[disk_target_positions['disk3']])
        disk4target.setPos(tower_target_positions[disk_target_positions['disk4']])
        
        
        # Run 'Begin Routine' code from code_text_min_moves
        text_min_moves.setText((instructions['Text_MinMoves']) + str(n_moves))
        
        # Run 'Begin Routine' code from code_text_timer
        # Initialize the timer
        routine_timer = core.Clock()
        routine_timer.reset()
        
        # Run 'Begin Routine' code from LSL_start_trial
        send_marker('start_trial_' + str(trial))
        # keep track of which components have finished
        towertaskComponents = [mouse, towers, disk1, disk2, disk3, disk4, towers_target, disk1target, disk2target, disk3target, disk4target, square_target, text_min_moves, text_timer, move_counter_text]
        for thisComponent in towertaskComponents:
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
        
        # --- Run Routine "towertask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            
            # *towers* updates
            
            # if towers is starting this frame...
            if towers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                towers.frameNStart = frameN  # exact frame index
                towers.tStart = t  # local t and not account for scr refresh
                towers.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(towers, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'towers.started')
                # update status
                towers.status = STARTED
                towers.setAutoDraw(True)
            
            # if towers is active this frame...
            if towers.status == STARTED:
                # update params
                pass
            
            # *disk1* updates
            
            # if disk1 is starting this frame...
            if disk1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk1.frameNStart = frameN  # exact frame index
                disk1.tStart = t  # local t and not account for scr refresh
                disk1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk1.started')
                # update status
                disk1.status = STARTED
                disk1.setAutoDraw(True)
            
            # if disk1 is active this frame...
            if disk1.status == STARTED:
                # update params
                pass
            
            # *disk2* updates
            
            # if disk2 is starting this frame...
            if disk2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk2.frameNStart = frameN  # exact frame index
                disk2.tStart = t  # local t and not account for scr refresh
                disk2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk2.started')
                # update status
                disk2.status = STARTED
                disk2.setAutoDraw(True)
            
            # if disk2 is active this frame...
            if disk2.status == STARTED:
                # update params
                pass
            
            # *disk3* updates
            
            # if disk3 is starting this frame...
            if disk3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk3.frameNStart = frameN  # exact frame index
                disk3.tStart = t  # local t and not account for scr refresh
                disk3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk3.started')
                # update status
                disk3.status = STARTED
                disk3.setAutoDraw(True)
            
            # if disk3 is active this frame...
            if disk3.status == STARTED:
                # update params
                pass
            
            # *disk4* updates
            
            # if disk4 is starting this frame...
            if disk4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk4.frameNStart = frameN  # exact frame index
                disk4.tStart = t  # local t and not account for scr refresh
                disk4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk4.started')
                # update status
                disk4.status = STARTED
                disk4.setAutoDraw(True)
            
            # if disk4 is active this frame...
            if disk4.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_movingdisks
            # Check for mouse interaction
            mouse = event.Mouse(visible=True)
            current_pos = mouse.getPos()
            
            # Determine which disk is being selected
            for tower, disks in tower_stacks.items():
                for disk_name in disks:
                    disk = eval(disk_name)
                    if mouse.isPressedIn(disk) and selected_disk is None:
                        # Select the top disk only
                        if disk_name == disks[-1]:
                            selected_disk = disk
                            original_tower = tower
            
            if selected_disk:
                # Move the selected disk with the mouse
                selected_disk.setPos(current_pos)
                
                if not mouse.getPressed()[0]:
                    # Determine the nearest tower
                    nearest_tower = min(['J', 'K', 'L'], key=lambda t: (current_pos[0] - tower_positions[t+'1'][0])**2)
                    
                    # Get the current stack height of the nearest tower
                    stack_height = len(tower_stacks[nearest_tower])
                    
                    if stack_height < 4:  # Only allow stacking up to 4 disks
                        nearest_pos_key = nearest_tower + str(stack_height + 1)
                        nearest_pos = tower_positions[nearest_pos_key]
            
                        # Check if the move is valid
                        if not tower_stacks[nearest_tower] or int(selected_disk.name[-1]) > int(tower_stacks[nearest_tower][-1][-1]):
                            # Move the disk to the new tower
                            tower_stacks[original_tower].remove(selected_disk.name)
                            tower_stacks[nearest_tower].append(selected_disk.name)
                            selected_disk.setPos(nearest_pos)
                            # Update the disk_positions dictionary
                            disk_positions[selected_disk.name] = nearest_pos_key
                            # Increment the move counter and update the text component
                            move_counter += 1
                            move_counter_text.setText((instructions['Text_nMoves']) + str(move_counter))
                            # Send LSL marker
                            send_marker('move_' + str(move_counter))
                            # Save data to the PsychoPy data file
                            thisExp.addData('block', block)
                            thisExp.addData('Trial number', trial_index)
                            thisExp.addData('move_counter', move_counter)
                            thisExp.addData('disk1_position', disk_positions['disk1'])
                            thisExp.addData('disk2_position', disk_positions['disk2'])
                            thisExp.addData('disk3_position', disk_positions['disk3'])
                            thisExp.addData('disk4_position', disk_positions['disk4'])
                            thisExp.addData('timer', (timer_task-remaining_time))
                            thisExp.nextEntry()
                        else:
                            # Snap back to original position if move is invalid
                            selected_disk.setPos(tower_positions[disk_positions[selected_disk.name]])
                    else:
                        # Snap back to original position if stack is full
                        selected_disk.setPos(tower_positions[disk_positions[selected_disk.name]])
            
                    selected_disk = None
                    original_tower = None
            
            # End the routine if the solution is found
            if disk_positions == disk_target_positions:
                continueRoutine = False
            
            
            # *towers_target* updates
            
            # if towers_target is starting this frame...
            if towers_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                towers_target.frameNStart = frameN  # exact frame index
                towers_target.tStart = t  # local t and not account for scr refresh
                towers_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(towers_target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'towers_target.started')
                # update status
                towers_target.status = STARTED
                towers_target.setAutoDraw(True)
            
            # if towers_target is active this frame...
            if towers_target.status == STARTED:
                # update params
                pass
            
            # *disk1target* updates
            
            # if disk1target is starting this frame...
            if disk1target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk1target.frameNStart = frameN  # exact frame index
                disk1target.tStart = t  # local t and not account for scr refresh
                disk1target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk1target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk1target.started')
                # update status
                disk1target.status = STARTED
                disk1target.setAutoDraw(True)
            
            # if disk1target is active this frame...
            if disk1target.status == STARTED:
                # update params
                pass
            
            # *disk2target* updates
            
            # if disk2target is starting this frame...
            if disk2target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk2target.frameNStart = frameN  # exact frame index
                disk2target.tStart = t  # local t and not account for scr refresh
                disk2target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk2target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk2target.started')
                # update status
                disk2target.status = STARTED
                disk2target.setAutoDraw(True)
            
            # if disk2target is active this frame...
            if disk2target.status == STARTED:
                # update params
                pass
            
            # *disk3target* updates
            
            # if disk3target is starting this frame...
            if disk3target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk3target.frameNStart = frameN  # exact frame index
                disk3target.tStart = t  # local t and not account for scr refresh
                disk3target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk3target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk3target.started')
                # update status
                disk3target.status = STARTED
                disk3target.setAutoDraw(True)
            
            # if disk3target is active this frame...
            if disk3target.status == STARTED:
                # update params
                pass
            
            # *disk4target* updates
            
            # if disk4target is starting this frame...
            if disk4target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk4target.frameNStart = frameN  # exact frame index
                disk4target.tStart = t  # local t and not account for scr refresh
                disk4target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk4target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk4target.started')
                # update status
                disk4target.status = STARTED
                disk4target.setAutoDraw(True)
            
            # if disk4target is active this frame...
            if disk4target.status == STARTED:
                # update params
                pass
            
            # *square_target* updates
            
            # if square_target is starting this frame...
            if square_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_target.frameNStart = frameN  # exact frame index
                square_target.tStart = t  # local t and not account for scr refresh
                square_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_target.started')
                # update status
                square_target.status = STARTED
                square_target.setAutoDraw(True)
            
            # if square_target is active this frame...
            if square_target.status == STARTED:
                # update params
                pass
            
            # *text_min_moves* updates
            
            # if text_min_moves is starting this frame...
            if text_min_moves.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_min_moves.frameNStart = frameN  # exact frame index
                text_min_moves.tStart = t  # local t and not account for scr refresh
                text_min_moves.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_min_moves, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_min_moves.started')
                # update status
                text_min_moves.status = STARTED
                text_min_moves.setAutoDraw(True)
            
            # if text_min_moves is active this frame...
            if text_min_moves.status == STARTED:
                # update params
                pass
            
            # *text_timer* updates
            
            # if text_timer is starting this frame...
            if text_timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_timer.frameNStart = frameN  # exact frame index
                text_timer.tStart = t  # local t and not account for scr refresh
                text_timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_timer.started')
                # update status
                text_timer.status = STARTED
                text_timer.setAutoDraw(True)
            
            # if text_timer is active this frame...
            if text_timer.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_text_timer
            # Calculate remaining time
            remaining_time = timer_task - routine_timer.getTime()
            
            # Show the timer only if there are 10 seconds or less remaining
            if remaining_time <= 15:
                # Update the timer text
                text_timer.setText(f'{remaining_time:.0f}')
                text_timer.setAutoDraw(True)  # Make sure the timer text is drawn
            else:
                text_timer.setAutoDraw(False)  # Hide the timer text
            
            # End the routine if time is up
            if remaining_time <= 0:
                continueRoutine = False
            
            
            # *move_counter_text* updates
            
            # if move_counter_text is starting this frame...
            if move_counter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                move_counter_text.frameNStart = frameN  # exact frame index
                move_counter_text.tStart = t  # local t and not account for scr refresh
                move_counter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(move_counter_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'move_counter_text.started')
                # update status
                move_counter_text.status = STARTED
                move_counter_text.setAutoDraw(True)
            
            # if move_counter_text is active this frame...
            if move_counter_text.status == STARTED:
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
            for thisComponent in towertaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "towertask" ---
        for thisComponent in towertaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('towertask.stopped', globalClock.getTime(format='float'))
        # store data for practice (TrialHandler)
        # Run 'End Routine' code from LSL_start_trial
        send_marker('end_trial_' + str(trial))
        # the Routine "towertask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'practice'
    
    
    # --- Prepare to start Routine "startTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('startTask.started', globalClock.getTime(format='float'))
    InstructionsText2.setText('')
    # Run 'Begin Routine' code from code_InstructionsText2
    # Set the text for the second set of instructions
    InstructionsText2.setText(instructions['Text_start_task'])
    StartTest.keys = []
    StartTest.rt = []
    _StartTest_allKeys = []
    # keep track of which components have finished
    startTaskComponents = [InstructionsText2, StartTest]
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
        
        # *StartTest* updates
        waitOnFlip = False
        
        # if StartTest is starting this frame...
        if StartTest.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            StartTest.frameNStart = frameN  # exact frame index
            StartTest.tStart = t  # local t and not account for scr refresh
            StartTest.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(StartTest, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'StartTest.started')
            # update status
            StartTest.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(StartTest.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(StartTest.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if StartTest.status == STARTED and not waitOnFlip:
            theseKeys = StartTest.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _StartTest_allKeys.extend(theseKeys)
            if len(_StartTest_allKeys):
                StartTest.keys = _StartTest_allKeys[-1].name  # just the last key pressed
                StartTest.rt = _StartTest_allKeys[-1].rt
                StartTest.duration = _StartTest_allKeys[-1].duration
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
    # Run 'End Routine' code from LSL_start_test
    send_marker("start_test")
    thisExp.nextEntry()
    # the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    test = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('scenario_TowerOfHanoi.csv', selection='1:23'),
        seed=None, name='test')
    thisExp.addLoop(test)  # add the loop to the experiment
    thisTest = test.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
    if thisTest != None:
        for paramName in thisTest:
            globals()[paramName] = thisTest[paramName]
    
    for thisTest in test:
        currentLoop = test
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisTest.rgb)
        if thisTest != None:
            for paramName in thisTest:
                globals()[paramName] = thisTest[paramName]
        
        # --- Prepare to start Routine "Npuzzle" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Npuzzle.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_Puzzle
        # Set the text for the first set of instructions
        TextPuzzle.setText(instructions['Text_puzzle'] + str(trial) + "/22")
        # keep track of which components have finished
        NpuzzleComponents = [TextPuzzle]
        for thisComponent in NpuzzleComponents:
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
        
        # --- Run Routine "Npuzzle" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *TextPuzzle* updates
            
            # if TextPuzzle is starting this frame...
            if TextPuzzle.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TextPuzzle.frameNStart = frameN  # exact frame index
                TextPuzzle.tStart = t  # local t and not account for scr refresh
                TextPuzzle.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TextPuzzle, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TextPuzzle.started')
                # update status
                TextPuzzle.status = STARTED
                TextPuzzle.setAutoDraw(True)
            
            # if TextPuzzle is active this frame...
            if TextPuzzle.status == STARTED:
                # update params
                pass
            
            # if TextPuzzle is stopping this frame...
            if TextPuzzle.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > TextPuzzle.tStartRefresh + 1.0-frameTolerance:
                    # keep track of stop time/frame for later
                    TextPuzzle.tStop = t  # not accounting for scr refresh
                    TextPuzzle.tStopRefresh = tThisFlipGlobal  # on global time
                    TextPuzzle.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'TextPuzzle.stopped')
                    # update status
                    TextPuzzle.status = FINISHED
                    TextPuzzle.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in NpuzzleComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "Npuzzle" ---
        for thisComponent in NpuzzleComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('Npuzzle.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.000000)
        
        # --- Prepare to start Routine "towertask" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('towertask.started', globalClock.getTime(format='float'))
        # setup some python lists for storing info about the mouse
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_movingdisks
        # Initialize move counter
        move_counter = 0
        move_counter_text.setText("Number of moves: " + str(move_counter))
        
        # Recuperate initial disk positions
        disk_positions = {
            'disk1': disk1_init,
            'disk2': disk2_init,
            'disk3': disk3_init,
            'disk4': disk4_init
        }
        
        # Update tower stacks based on initial positions
        tower_stacks = {'J': [], 'K': [], 'L': []}
        for disk, pos_label in disk_positions.items():
            pos = tower_positions[pos_label]
            if pos[0] == -0.5:
                tower_stacks['J'].append(disk)
            elif pos[0] == 0:
                tower_stacks['K'].append(disk)
            elif pos[0] == 0.5:
                tower_stacks['L'].append(disk)
        
        # Ensure the disks are ordered correctly in the stacks
        for key in tower_stacks:
            tower_stacks[key] = sorted(tower_stacks[key], key=lambda d: tower_positions[disk_positions[d]][1])
        
        # Set disk positions
        disk1.setPos(tower_positions[disk_positions['disk1']])
        disk2.setPos(tower_positions[disk_positions['disk2']])
        disk3.setPos(tower_positions[disk_positions['disk3']])
        disk4.setPos(tower_positions[disk_positions['disk4']])
        # Run 'Begin Routine' code from code_targetdisks
        # Recuperate initial disk positions
        disk_target_positions = {
            'disk1': disk1_target,
            'disk2': disk2_target,
            'disk3': disk3_target,
            'disk4': disk4_target
        }
        
        # Update tower stacks based on initial positions
        tower_target_stacks = {'J': [], 'K': [], 'L': []}
        for disk, pos_label in disk_target_positions.items():
            pos = tower_target_positions[pos_label]
            if pos[0] == -0.25:
                tower_target_stacks['J'].append(disk)
            elif pos[0] == 0:
                tower_target_stacks['K'].append(disk)
            elif pos[0] == 0.25:
                tower_target_stacks['L'].append(disk)
        
        
        # Set disk positions
        disk1target.setPos(tower_target_positions[disk_target_positions['disk1']])
        disk2target.setPos(tower_target_positions[disk_target_positions['disk2']])
        disk3target.setPos(tower_target_positions[disk_target_positions['disk3']])
        disk4target.setPos(tower_target_positions[disk_target_positions['disk4']])
        
        
        # Run 'Begin Routine' code from code_text_min_moves
        text_min_moves.setText((instructions['Text_MinMoves']) + str(n_moves))
        
        # Run 'Begin Routine' code from code_text_timer
        # Initialize the timer
        routine_timer = core.Clock()
        routine_timer.reset()
        
        # Run 'Begin Routine' code from LSL_start_trial
        send_marker('start_trial_' + str(trial))
        # keep track of which components have finished
        towertaskComponents = [mouse, towers, disk1, disk2, disk3, disk4, towers_target, disk1target, disk2target, disk3target, disk4target, square_target, text_min_moves, text_timer, move_counter_text]
        for thisComponent in towertaskComponents:
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
        
        # --- Run Routine "towertask" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # *mouse* updates
            
            # if mouse is starting this frame...
            if mouse.status == NOT_STARTED and t >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                mouse.frameNStart = frameN  # exact frame index
                mouse.tStart = t  # local t and not account for scr refresh
                mouse.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(mouse, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.addData('mouse.started', t)
                # update status
                mouse.status = STARTED
                mouse.mouseClock.reset()
                prevButtonState = mouse.getPressed()  # if button is down already this ISN'T a new click
            
            # *towers* updates
            
            # if towers is starting this frame...
            if towers.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                towers.frameNStart = frameN  # exact frame index
                towers.tStart = t  # local t and not account for scr refresh
                towers.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(towers, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'towers.started')
                # update status
                towers.status = STARTED
                towers.setAutoDraw(True)
            
            # if towers is active this frame...
            if towers.status == STARTED:
                # update params
                pass
            
            # *disk1* updates
            
            # if disk1 is starting this frame...
            if disk1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk1.frameNStart = frameN  # exact frame index
                disk1.tStart = t  # local t and not account for scr refresh
                disk1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk1.started')
                # update status
                disk1.status = STARTED
                disk1.setAutoDraw(True)
            
            # if disk1 is active this frame...
            if disk1.status == STARTED:
                # update params
                pass
            
            # *disk2* updates
            
            # if disk2 is starting this frame...
            if disk2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk2.frameNStart = frameN  # exact frame index
                disk2.tStart = t  # local t and not account for scr refresh
                disk2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk2.started')
                # update status
                disk2.status = STARTED
                disk2.setAutoDraw(True)
            
            # if disk2 is active this frame...
            if disk2.status == STARTED:
                # update params
                pass
            
            # *disk3* updates
            
            # if disk3 is starting this frame...
            if disk3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk3.frameNStart = frameN  # exact frame index
                disk3.tStart = t  # local t and not account for scr refresh
                disk3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk3.started')
                # update status
                disk3.status = STARTED
                disk3.setAutoDraw(True)
            
            # if disk3 is active this frame...
            if disk3.status == STARTED:
                # update params
                pass
            
            # *disk4* updates
            
            # if disk4 is starting this frame...
            if disk4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk4.frameNStart = frameN  # exact frame index
                disk4.tStart = t  # local t and not account for scr refresh
                disk4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk4.started')
                # update status
                disk4.status = STARTED
                disk4.setAutoDraw(True)
            
            # if disk4 is active this frame...
            if disk4.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_movingdisks
            # Check for mouse interaction
            mouse = event.Mouse(visible=True)
            current_pos = mouse.getPos()
            
            # Determine which disk is being selected
            for tower, disks in tower_stacks.items():
                for disk_name in disks:
                    disk = eval(disk_name)
                    if mouse.isPressedIn(disk) and selected_disk is None:
                        # Select the top disk only
                        if disk_name == disks[-1]:
                            selected_disk = disk
                            original_tower = tower
            
            if selected_disk:
                # Move the selected disk with the mouse
                selected_disk.setPos(current_pos)
                
                if not mouse.getPressed()[0]:
                    # Determine the nearest tower
                    nearest_tower = min(['J', 'K', 'L'], key=lambda t: (current_pos[0] - tower_positions[t+'1'][0])**2)
                    
                    # Get the current stack height of the nearest tower
                    stack_height = len(tower_stacks[nearest_tower])
                    
                    if stack_height < 4:  # Only allow stacking up to 4 disks
                        nearest_pos_key = nearest_tower + str(stack_height + 1)
                        nearest_pos = tower_positions[nearest_pos_key]
            
                        # Check if the move is valid
                        if not tower_stacks[nearest_tower] or int(selected_disk.name[-1]) > int(tower_stacks[nearest_tower][-1][-1]):
                            # Move the disk to the new tower
                            tower_stacks[original_tower].remove(selected_disk.name)
                            tower_stacks[nearest_tower].append(selected_disk.name)
                            selected_disk.setPos(nearest_pos)
                            # Update the disk_positions dictionary
                            disk_positions[selected_disk.name] = nearest_pos_key
                            # Increment the move counter and update the text component
                            move_counter += 1
                            move_counter_text.setText((instructions['Text_nMoves']) + str(move_counter))
                            # Send LSL marker
                            send_marker('move_' + str(move_counter))
                            # Save data to the PsychoPy data file
                            thisExp.addData('block', block)
                            thisExp.addData('Trial number', trial_index)
                            thisExp.addData('move_counter', move_counter)
                            thisExp.addData('disk1_position', disk_positions['disk1'])
                            thisExp.addData('disk2_position', disk_positions['disk2'])
                            thisExp.addData('disk3_position', disk_positions['disk3'])
                            thisExp.addData('disk4_position', disk_positions['disk4'])
                            thisExp.addData('timer', (timer_task-remaining_time))
                            thisExp.nextEntry()
                        else:
                            # Snap back to original position if move is invalid
                            selected_disk.setPos(tower_positions[disk_positions[selected_disk.name]])
                    else:
                        # Snap back to original position if stack is full
                        selected_disk.setPos(tower_positions[disk_positions[selected_disk.name]])
            
                    selected_disk = None
                    original_tower = None
            
            # End the routine if the solution is found
            if disk_positions == disk_target_positions:
                continueRoutine = False
            
            
            # *towers_target* updates
            
            # if towers_target is starting this frame...
            if towers_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                towers_target.frameNStart = frameN  # exact frame index
                towers_target.tStart = t  # local t and not account for scr refresh
                towers_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(towers_target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'towers_target.started')
                # update status
                towers_target.status = STARTED
                towers_target.setAutoDraw(True)
            
            # if towers_target is active this frame...
            if towers_target.status == STARTED:
                # update params
                pass
            
            # *disk1target* updates
            
            # if disk1target is starting this frame...
            if disk1target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk1target.frameNStart = frameN  # exact frame index
                disk1target.tStart = t  # local t and not account for scr refresh
                disk1target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk1target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk1target.started')
                # update status
                disk1target.status = STARTED
                disk1target.setAutoDraw(True)
            
            # if disk1target is active this frame...
            if disk1target.status == STARTED:
                # update params
                pass
            
            # *disk2target* updates
            
            # if disk2target is starting this frame...
            if disk2target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk2target.frameNStart = frameN  # exact frame index
                disk2target.tStart = t  # local t and not account for scr refresh
                disk2target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk2target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk2target.started')
                # update status
                disk2target.status = STARTED
                disk2target.setAutoDraw(True)
            
            # if disk2target is active this frame...
            if disk2target.status == STARTED:
                # update params
                pass
            
            # *disk3target* updates
            
            # if disk3target is starting this frame...
            if disk3target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk3target.frameNStart = frameN  # exact frame index
                disk3target.tStart = t  # local t and not account for scr refresh
                disk3target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk3target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk3target.started')
                # update status
                disk3target.status = STARTED
                disk3target.setAutoDraw(True)
            
            # if disk3target is active this frame...
            if disk3target.status == STARTED:
                # update params
                pass
            
            # *disk4target* updates
            
            # if disk4target is starting this frame...
            if disk4target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                disk4target.frameNStart = frameN  # exact frame index
                disk4target.tStart = t  # local t and not account for scr refresh
                disk4target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(disk4target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'disk4target.started')
                # update status
                disk4target.status = STARTED
                disk4target.setAutoDraw(True)
            
            # if disk4target is active this frame...
            if disk4target.status == STARTED:
                # update params
                pass
            
            # *square_target* updates
            
            # if square_target is starting this frame...
            if square_target.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                square_target.frameNStart = frameN  # exact frame index
                square_target.tStart = t  # local t and not account for scr refresh
                square_target.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(square_target, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'square_target.started')
                # update status
                square_target.status = STARTED
                square_target.setAutoDraw(True)
            
            # if square_target is active this frame...
            if square_target.status == STARTED:
                # update params
                pass
            
            # *text_min_moves* updates
            
            # if text_min_moves is starting this frame...
            if text_min_moves.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_min_moves.frameNStart = frameN  # exact frame index
                text_min_moves.tStart = t  # local t and not account for scr refresh
                text_min_moves.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_min_moves, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_min_moves.started')
                # update status
                text_min_moves.status = STARTED
                text_min_moves.setAutoDraw(True)
            
            # if text_min_moves is active this frame...
            if text_min_moves.status == STARTED:
                # update params
                pass
            
            # *text_timer* updates
            
            # if text_timer is starting this frame...
            if text_timer.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_timer.frameNStart = frameN  # exact frame index
                text_timer.tStart = t  # local t and not account for scr refresh
                text_timer.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_timer, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_timer.started')
                # update status
                text_timer.status = STARTED
                text_timer.setAutoDraw(True)
            
            # if text_timer is active this frame...
            if text_timer.status == STARTED:
                # update params
                pass
            # Run 'Each Frame' code from code_text_timer
            # Calculate remaining time
            remaining_time = timer_task - routine_timer.getTime()
            
            # Show the timer only if there are 10 seconds or less remaining
            if remaining_time <= 15:
                # Update the timer text
                text_timer.setText(f'{remaining_time:.0f}')
                text_timer.setAutoDraw(True)  # Make sure the timer text is drawn
            else:
                text_timer.setAutoDraw(False)  # Hide the timer text
            
            # End the routine if time is up
            if remaining_time <= 0:
                continueRoutine = False
            
            
            # *move_counter_text* updates
            
            # if move_counter_text is starting this frame...
            if move_counter_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                move_counter_text.frameNStart = frameN  # exact frame index
                move_counter_text.tStart = t  # local t and not account for scr refresh
                move_counter_text.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(move_counter_text, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'move_counter_text.started')
                # update status
                move_counter_text.status = STARTED
                move_counter_text.setAutoDraw(True)
            
            # if move_counter_text is active this frame...
            if move_counter_text.status == STARTED:
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
            for thisComponent in towertaskComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "towertask" ---
        for thisComponent in towertaskComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('towertask.stopped', globalClock.getTime(format='float'))
        # store data for test (TrialHandler)
        # Run 'End Routine' code from LSL_start_trial
        send_marker('end_trial_' + str(trial))
        # the Routine "towertask" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'test'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from LSL_TOH_end
    send_marker('TOH_end')
    # Run 'Begin Routine' code from code_InstructionsText4
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['Text_end_task'])
    
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
            theseKeys = end_task.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _end_task_allKeys.extend(theseKeys)
            if len(_end_task_allKeys):
                end_task.keys = _end_task_allKeys[-1].name  # just the last key pressed
                end_task.rt = _end_task_allKeys[-1].rt
                end_task.duration = _end_task_allKeys[-1].duration
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
