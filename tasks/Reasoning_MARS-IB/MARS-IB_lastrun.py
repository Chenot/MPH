#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on novembre 12, 2024, at 13:58
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
expName = 'MARS-IB'  # from the Builder filename that created this script
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
        originPath='D:\\Google Drive\\Professionnel\\3_Post-doc_ISAE-MPH\\Experience_MPH\\project\\code\\PsychopyTasks\\Reasoning_MARS-IB\\MARS-IB_lastrun.py',
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
            monitor='testMonitor', color=[1,1,1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [1,1,1]
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
    if deviceManager.getDevice('instr_resp') is None:
        # initialise instr_resp
        instr_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_resp',
        )
    if deviceManager.getDevice('instr_resp_2') is None:
        # initialise instr_resp_2
        instr_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='instr_resp_2',
        )
    if deviceManager.getDevice('go') is None:
        # initialise go
        go = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go',
        )
    if deviceManager.getDevice('key_resp_2') is None:
        # initialise key_resp_2
        key_resp_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp_2',
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
            'name_task' : 'MATRIX REASONING',
            'Instructions1': (
                "Welcome to the Matrix Reasoning Task.\n\n"
                "In this task, you will be shown a 3x3 grid of patterns. The last one, "
                "in the bottom right-hand corner, will be missing.\n"
                "You need to select which of the four possible patterns along the bottom fits into the gap."
            ),
            'Instructions2': (
                "Try to be as fast and as accurate as you can be.\n\n"
                "If you cannot solve the puzzle, then you should guess - you will not be penalized for an incorrect answer.\n"
                "The task contains a mix of easy, medium, and hard puzzles.\n"
                "You will have 30 seconds to complete each puzzle.\n\n"
                "Press the space bar to begin the practice."
            ),
            'Text_start_task': (
                "The practice is over. Now we shall begin the real task.\n\n"
                "Ready?\n\n"
                "Press the space bar to begin."
            ),
            'Text_pause_between_blocks': "Pause\n\nPress the space bar when you are ready to continue.",
            'Text_end_task': (
                "This task is now over.\n\nThank you!\n\nPress the space bar to continue."
            )
        }
    else:
        instructions = {
            'name_task' : 'RAISONNEMENT MATRICIEL',
            'Instructions1': (
                "Bienvenue dans la tâche de raisonnement matriciel.\n\n"
                "Dans cette tâche, un tableau de motifs 3x3 vous sera présenté. Le dernier, "
                "dans le coin inférieur droit, sera manquant.\n"
                "Vous devez sélectionner lequel des quatre motifs possibles en bas correspond à l'emplacement vide."
            ),
            'Instructions2': (
                "Essayez d'être aussi rapide et précis que possible.\n\n"
                "Si vous ne pouvez pas résoudre le puzzle, vous devez deviner - vous ne serez pas pénalisé pour une réponse incorrecte.\n"
                "La tâche contient un mélange de puzzles faciles, moyens et difficiles.\n"
                "Vous aurez 30 secondes pour compléter chaque puzzle.\n\n"
                "Appuyez sur la barre d'espace pour commencer l'entraînement."
            ),
            'Text_start_task': (
                "L'entraînement est terminée. Nous allons maintenant commencer la vraie tâche.\n\n"
                "Prêt ?\n\n"
                "Appuyez sur la barre d'espace pour commencer."
            ),
            'Text_pause_between_blocks': "Pause\n\nAppuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer.",
            'Text_end_task': (
                "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer."
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
    
    # Run 'Begin Experiment' code from define_block
    import pandas as pd
    import psychopy.logging as logging
    
    # Set logging level to WARNING to suppress INFO and DEBUG messages
    logging.console.setLevel(logging.WARNING)
    
    # Load the scenario CSV file
    scenario_df = pd.read_csv('MARS-IB_scenario.csv')
    
    # Filter the practice trials
    practice_indices = scenario_df.index[scenario_df['block'] == 'practice'].tolist()
    # Convert indices to PsychoPy's format (string of ranges)
    selected_rows_practice = f"{practice_indices[0]}:{practice_indices[-1]+1}" if practice_indices else ""
    
    
    # --- Initialize components for Routine "instr1" ---
    instr_text = visual.TextStim(win=win, name='instr_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_resp = keyboard.Keyboard(deviceName='instr_resp')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "instr2" ---
    instr_text_2 = visual.TextStim(win=win, name='instr_text_2',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    instr_resp_2 = keyboard.Keyboard(deviceName='instr_resp_2')
    nametask_2 = visual.TextStim(win=win, name='nametask_2',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    
    # --- Initialize components for Routine "fixation_cross" ---
    blank = visual.TextStim(win=win, name='blank',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    image_main = visual.ImageStim(
        win=win,
        name='image_main', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.5,0.5),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=0.0)
    opt1 = visual.ImageStim(
        win=win,
        name='opt1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    opt2 = visual.ImageStim(
        win=win,
        name='opt2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.15, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    opt3 = visual.ImageStim(
        win=win,
        name='opt3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.15, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    opt4 = visual.ImageStim(
        win=win,
        name='opt4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    text_timer = visual.TextStim(win=win, name='text_timer',
        text=None,
        font='Arial',
        pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    # Run 'Begin Experiment' code from code_text_timer
    # Initialize the timer (in seconds)
    timer_task = 30
    
    # --- Initialize components for Routine "startTask" ---
    InstructionsText2 = visual.TextStim(win=win, name='InstructionsText2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go = keyboard.Keyboard(deviceName='go')
    # Run 'Begin Experiment' code from define_block_rows
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_test = True
    
    # --- Initialize components for Routine "block_counter" ---
    # Run 'Begin Experiment' code from LSL_start_testblock
    send_marker("start_block")
    
    # --- Initialize components for Routine "fixation_cross" ---
    blank = visual.TextStim(win=win, name='blank',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    cross = visual.TextStim(win=win, name='cross',
        text='+',
        font='Arial',
        pos=(0, 0.2), height=0.1, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "trial" ---
    image_main = visual.ImageStim(
        win=win,
        name='image_main', 
        image='default.png', mask=None, anchor='center',
        ori=0, pos=(0, 0.2), size=(0.5,0.5),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=512, interpolate=True, depth=0.0)
    opt1 = visual.ImageStim(
        win=win,
        name='opt1', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.5, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-1.0)
    opt2 = visual.ImageStim(
        win=win,
        name='opt2', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(-0.15, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-2.0)
    opt3 = visual.ImageStim(
        win=win,
        name='opt3', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.15, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    opt4 = visual.ImageStim(
        win=win,
        name='opt4', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0.5, -0.3), size=(0.2, 0.2),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-4.0)
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    text_timer = visual.TextStim(win=win, name='text_timer',
        text=None,
        font='Arial',
        pos=(0, -0.1), height=0.04, wrapWidth=None, ori=0.0, 
        color='black', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-8.0);
    # Run 'Begin Experiment' code from code_text_timer
    # Initialize the timer (in seconds)
    timer_task = 30
    
    # --- Initialize components for Routine "done" ---
    end_text = visual.TextStim(win=win, name='end_text',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='black', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    key_resp_2 = keyboard.Keyboard(deviceName='key_resp_2')
    
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
    
    # --- Prepare to start Routine "instr1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr1.started', globalClock.getTime(format='float'))
    instr_resp.keys = []
    instr_resp.rt = []
    _instr_resp_allKeys = []
    # Run 'Begin Routine' code from code_instr_text
    # Set the text for the first set of instructions
    instr_text.setText(instructions['Instructions1'])
    
    # Run 'Begin Routine' code from LSL_MARS_start
    send_marker('MARS_start')
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instr1Components = [instr_text, instr_resp, nametask]
    for thisComponent in instr1Components:
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
    
    # --- Run Routine "instr1" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text* updates
        
        # if instr_text is starting this frame...
        if instr_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text.frameNStart = frameN  # exact frame index
            instr_text.tStart = t  # local t and not account for scr refresh
            instr_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_text.status = STARTED
            instr_text.setAutoDraw(True)
        
        # if instr_text is active this frame...
        if instr_text.status == STARTED:
            # update params
            pass
        
        # *instr_resp* updates
        waitOnFlip = False
        
        # if instr_resp is starting this frame...
        if instr_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp.frameNStart = frameN  # exact frame index
            instr_resp.tStart = t  # local t and not account for scr refresh
            instr_resp.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_resp.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _instr_resp_allKeys.extend(theseKeys)
            if len(_instr_resp_allKeys):
                instr_resp.keys = _instr_resp_allKeys[-1].name  # just the last key pressed
                instr_resp.rt = _instr_resp_allKeys[-1].rt
                instr_resp.duration = _instr_resp_allKeys[-1].duration
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
        for thisComponent in instr1Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr1" ---
    for thisComponent in instr1Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr1.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instr1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instr2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instr2.started', globalClock.getTime(format='float'))
    instr_resp_2.keys = []
    instr_resp_2.rt = []
    _instr_resp_2_allKeys = []
    # Run 'Begin Routine' code from code_instr_text_2
    # Set the text for the first set of instructions
    instr_text_2.setText(instructions['Instructions2'])
    
    # Run 'Begin Routine' code from code_nametask_2
    nametask_2.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instr2Components = [instr_text_2, instr_resp_2, nametask_2]
    for thisComponent in instr2Components:
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
    
    # --- Run Routine "instr2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instr_text_2* updates
        
        # if instr_text_2 is starting this frame...
        if instr_text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_text_2.frameNStart = frameN  # exact frame index
            instr_text_2.tStart = t  # local t and not account for scr refresh
            instr_text_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_text_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_text_2.status = STARTED
            instr_text_2.setAutoDraw(True)
        
        # if instr_text_2 is active this frame...
        if instr_text_2.status == STARTED:
            # update params
            pass
        
        # *instr_resp_2* updates
        waitOnFlip = False
        
        # if instr_resp_2 is starting this frame...
        if instr_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instr_resp_2.frameNStart = frameN  # exact frame index
            instr_resp_2.tStart = t  # local t and not account for scr refresh
            instr_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instr_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            instr_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(instr_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(instr_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if instr_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = instr_resp_2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _instr_resp_2_allKeys.extend(theseKeys)
            if len(_instr_resp_2_allKeys):
                instr_resp_2.keys = _instr_resp_2_allKeys[-1].name  # just the last key pressed
                instr_resp_2.rt = _instr_resp_2_allKeys[-1].rt
                instr_resp_2.duration = _instr_resp_2_allKeys[-1].duration
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
        for thisComponent in instr2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instr2" ---
    for thisComponent in instr2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instr2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instr2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practice = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('MARS-IB_scenario.csv', selection=selected_rows_practice),
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
        
        # --- Prepare to start Routine "fixation_cross" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('fixation_cross.started', globalClock.getTime(format='float'))
        # keep track of which components have finished
        fixation_crossComponents = [blank, cross]
        for thisComponent in fixation_crossComponents:
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
        
        # --- Run Routine "fixation_cross" ---
        routineForceEnded = not continueRoutine
        while continueRoutine and routineTimer.getTime() < 1.7:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *blank* updates
            
            # if blank is starting this frame...
            if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                blank.frameNStart = frameN  # exact frame index
                blank.tStart = t  # local t and not account for scr refresh
                blank.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'blank.started')
                # update status
                blank.status = STARTED
                blank.setAutoDraw(True)
            
            # if blank is active this frame...
            if blank.status == STARTED:
                # update params
                pass
            
            # if blank is stopping this frame...
            if blank.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > blank.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    blank.tStop = t  # not accounting for scr refresh
                    blank.tStopRefresh = tThisFlipGlobal  # on global time
                    blank.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank.stopped')
                    # update status
                    blank.status = FINISHED
                    blank.setAutoDraw(False)
            
            # *cross* updates
            
            # if cross is starting this frame...
            if cross.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
            
            # if cross is stopping this frame...
            if cross.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > cross.tStartRefresh + 1.2-frameTolerance:
                    # keep track of stop time/frame for later
                    cross.tStop = t  # not accounting for scr refresh
                    cross.tStopRefresh = tThisFlipGlobal  # on global time
                    cross.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'cross.stopped')
                    # update status
                    cross.status = FINISHED
                    cross.setAutoDraw(False)
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in fixation_crossComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "fixation_cross" ---
        for thisComponent in fixation_crossComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('fixation_cross.stopped', globalClock.getTime(format='float'))
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-1.700000)
        
        # --- Prepare to start Routine "trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('trial.started', globalClock.getTime(format='float'))
        image_main.setImage(image_file_main)
        opt1.setImage(image_file_opt1)
        opt2.setImage(image_file_opt2)
        opt3.setImage(image_file_opt3)
        opt4.setImage(image_file_opt4)
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        mouse.corr = []
        mouse.clicked_name = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from code_mouse
        # Initialize choice as None
        choice = None
        
        marker = f"stimulus_{image_file_main}"
        send_marker(marker)
        # Run 'Begin Routine' code from code_correct_resp
        # Determine which opt is the correct one based on the correct_resp from the CSV
        if correct_resp == image_file_opt1:
            correct_image = opt1
        elif correct_resp == image_file_opt2:
            correct_image = opt2
        elif correct_resp == image_file_opt3:
            correct_image = opt3
        elif correct_resp == image_file_opt4:
            correct_image = opt4
        # Run 'Begin Routine' code from code_text_timer
        # Initialize the timer
        routine_timer = core.Clock()
        routine_timer.reset()
        # Run 'Begin Routine' code from code_LSL_trial
        marker = f"stimulus_{image_file_main}"
        send_marker(marker)
        # keep track of which components have finished
        trialComponents = [image_main, opt1, opt2, opt3, opt4, mouse, text_timer]
        for thisComponent in trialComponents:
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
        
        # --- Run Routine "trial" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *image_main* updates
            
            # if image_main is starting this frame...
            if image_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                image_main.frameNStart = frameN  # exact frame index
                image_main.tStart = t  # local t and not account for scr refresh
                image_main.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(image_main, 'tStartRefresh')  # time at next scr refresh
                # update status
                image_main.status = STARTED
                image_main.setAutoDraw(True)
            
            # if image_main is active this frame...
            if image_main.status == STARTED:
                # update params
                pass
            
            # *opt1* updates
            
            # if opt1 is starting this frame...
            if opt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt1.frameNStart = frameN  # exact frame index
                opt1.tStart = t  # local t and not account for scr refresh
                opt1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt1.started')
                # update status
                opt1.status = STARTED
                opt1.setAutoDraw(True)
            
            # if opt1 is active this frame...
            if opt1.status == STARTED:
                # update params
                pass
            
            # *opt2* updates
            
            # if opt2 is starting this frame...
            if opt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt2.frameNStart = frameN  # exact frame index
                opt2.tStart = t  # local t and not account for scr refresh
                opt2.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt2, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt2.started')
                # update status
                opt2.status = STARTED
                opt2.setAutoDraw(True)
            
            # if opt2 is active this frame...
            if opt2.status == STARTED:
                # update params
                pass
            
            # *opt3* updates
            
            # if opt3 is starting this frame...
            if opt3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt3.frameNStart = frameN  # exact frame index
                opt3.tStart = t  # local t and not account for scr refresh
                opt3.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt3, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt3.started')
                # update status
                opt3.status = STARTED
                opt3.setAutoDraw(True)
            
            # if opt3 is active this frame...
            if opt3.status == STARTED:
                # update params
                pass
            
            # *opt4* updates
            
            # if opt4 is starting this frame...
            if opt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                opt4.frameNStart = frameN  # exact frame index
                opt4.tStart = t  # local t and not account for scr refresh
                opt4.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(opt4, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'opt4.started')
                # update status
                opt4.status = STARTED
                opt4.setAutoDraw(True)
            
            # if opt4 is active this frame...
            if opt4.status == STARTED:
                # update params
                pass
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
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        # check if the mouse was inside our 'clickable' objects
                        gotValidClick = False
                        clickableList = environmenttools.getFromNames([opt1,opt2,opt3,opt4], namespace=locals())
                        for obj in clickableList:
                            # is this object clicked on?
                            if obj.contains(mouse):
                                gotValidClick = True
                                mouse.clicked_name.append(obj.name)
                        # check whether click was in correct object
                        if gotValidClick:
                            _corr = 0
                            _corrAns = environmenttools.getFromNames(correct_image, namespace=locals())
                            for obj in _corrAns:
                                # is this object clicked on?
                                if obj.contains(mouse):
                                    _corr = 1
                            mouse.corr.append(_corr)
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
                        if gotValidClick:
                            continueRoutine = False  # end routine on response
            
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
            
            # Show the timer only if there are 5 seconds or less remaining
            if remaining_time <= 5:
                # Update the timer text
                text_timer.setText(f'{remaining_time:.0f}')
                text_timer.setAutoDraw(True)  # Make sure the timer text is drawn
            else:
                text_timer.setAutoDraw(False)  # Hide the timer text
            
            # End the routine if time is up
            if remaining_time <= 0:
                continueRoutine = False
            
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "trial" ---
        for thisComponent in trialComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
        # store data for practice (TrialHandler)
        practice.addData('mouse.x', mouse.x)
        practice.addData('mouse.y', mouse.y)
        practice.addData('mouse.leftButton', mouse.leftButton)
        practice.addData('mouse.midButton', mouse.midButton)
        practice.addData('mouse.rightButton', mouse.rightButton)
        practice.addData('mouse.time', mouse.time)
        practice.addData('mouse.corr', mouse.corr)
        practice.addData('mouse.clicked_name', mouse.clicked_name)
        # Run 'End Routine' code from code_mouse
        # Check which option was clicked and store the choice
        if mouse.isPressedIn(opt1):
            choice = 'opt1'
        elif mouse.isPressedIn(opt2):
            choice = 'opt2'
        elif mouse.isPressedIn(opt3):
            choice = 'opt3'
        elif mouse.isPressedIn(opt4):
            choice = 'opt4'
        
        # If a choice was made, send the corresponding LSL marker and store the response
        if choice:
            send_marker(choice)  # Function to send the LSL marker
            thisExp.addData('resp_mouse', choice)  # Add the choice to the data file
        else:
            thisExp.addData('resp_mouse', 'no_response')  # Handle case where no choice was made
        
        # Run 'End Routine' code from code_LSL_trial
        answer_corr = f"response_{mouse.corr}"
        send_marker(answer_corr)  # Function to send the LSL marker
        
        
        # the Routine "trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
    # completed 1.0 repeats of 'practice'
    
    # get names of stimulus parameters
    if practice.trialList in ([], [None], None):
        params = []
    else:
        params = practice.trialList[0].keys()
    # save data for this loop
    practice.saveAsExcel(filename + '.xlsx', sheetName='practice',
        stimOut=params,
        dataOut=['n','all_mean','all_std', 'all_raw'])
    
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
        trialList=data.importConditions('MARS-IB_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        
        # set up handler to look after randomisation of conditions etc
        trials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('MARS-IB_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
            seed=None, name='trials')
        thisExp.addLoop(trials)  # add the loop to the experiment
        thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
        # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
        if thisTrial != None:
            for paramName in thisTrial:
                globals()[paramName] = thisTrial[paramName]
        
        for thisTrial in trials:
            currentLoop = trials
            thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
            # pause experiment here if requested
            if thisExp.status == PAUSED:
                pauseExperiment(
                    thisExp=thisExp, 
                    win=win, 
                    timers=[routineTimer], 
                    playbackComponents=[]
            )
            # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
            if thisTrial != None:
                for paramName in thisTrial:
                    globals()[paramName] = thisTrial[paramName]
            
            # --- Prepare to start Routine "fixation_cross" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('fixation_cross.started', globalClock.getTime(format='float'))
            # keep track of which components have finished
            fixation_crossComponents = [blank, cross]
            for thisComponent in fixation_crossComponents:
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
            
            # --- Run Routine "fixation_cross" ---
            routineForceEnded = not continueRoutine
            while continueRoutine and routineTimer.getTime() < 1.7:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *blank* updates
                
                # if blank is starting this frame...
                if blank.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    blank.frameNStart = frameN  # exact frame index
                    blank.tStart = t  # local t and not account for scr refresh
                    blank.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(blank, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'blank.started')
                    # update status
                    blank.status = STARTED
                    blank.setAutoDraw(True)
                
                # if blank is active this frame...
                if blank.status == STARTED:
                    # update params
                    pass
                
                # if blank is stopping this frame...
                if blank.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > blank.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        blank.tStop = t  # not accounting for scr refresh
                        blank.tStopRefresh = tThisFlipGlobal  # on global time
                        blank.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'blank.stopped')
                        # update status
                        blank.status = FINISHED
                        blank.setAutoDraw(False)
                
                # *cross* updates
                
                # if cross is starting this frame...
                if cross.status == NOT_STARTED and tThisFlip >= 0.5-frameTolerance:
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
                
                # if cross is stopping this frame...
                if cross.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > cross.tStartRefresh + 1.2-frameTolerance:
                        # keep track of stop time/frame for later
                        cross.tStop = t  # not accounting for scr refresh
                        cross.tStopRefresh = tThisFlipGlobal  # on global time
                        cross.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'cross.stopped')
                        # update status
                        cross.status = FINISHED
                        cross.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in fixation_crossComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "fixation_cross" ---
            for thisComponent in fixation_crossComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('fixation_cross.stopped', globalClock.getTime(format='float'))
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-1.700000)
            
            # --- Prepare to start Routine "trial" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial.started', globalClock.getTime(format='float'))
            image_main.setImage(image_file_main)
            opt1.setImage(image_file_opt1)
            opt2.setImage(image_file_opt2)
            opt3.setImage(image_file_opt3)
            opt4.setImage(image_file_opt4)
            # setup some python lists for storing info about the mouse
            mouse.x = []
            mouse.y = []
            mouse.leftButton = []
            mouse.midButton = []
            mouse.rightButton = []
            mouse.time = []
            mouse.corr = []
            mouse.clicked_name = []
            gotValidClick = False  # until a click is received
            # Run 'Begin Routine' code from code_mouse
            # Initialize choice as None
            choice = None
            
            marker = f"stimulus_{image_file_main}"
            send_marker(marker)
            # Run 'Begin Routine' code from code_correct_resp
            # Determine which opt is the correct one based on the correct_resp from the CSV
            if correct_resp == image_file_opt1:
                correct_image = opt1
            elif correct_resp == image_file_opt2:
                correct_image = opt2
            elif correct_resp == image_file_opt3:
                correct_image = opt3
            elif correct_resp == image_file_opt4:
                correct_image = opt4
            # Run 'Begin Routine' code from code_text_timer
            # Initialize the timer
            routine_timer = core.Clock()
            routine_timer.reset()
            # Run 'Begin Routine' code from code_LSL_trial
            marker = f"stimulus_{image_file_main}"
            send_marker(marker)
            # keep track of which components have finished
            trialComponents = [image_main, opt1, opt2, opt3, opt4, mouse, text_timer]
            for thisComponent in trialComponents:
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
            
            # --- Run Routine "trial" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *image_main* updates
                
                # if image_main is starting this frame...
                if image_main.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    image_main.frameNStart = frameN  # exact frame index
                    image_main.tStart = t  # local t and not account for scr refresh
                    image_main.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(image_main, 'tStartRefresh')  # time at next scr refresh
                    # update status
                    image_main.status = STARTED
                    image_main.setAutoDraw(True)
                
                # if image_main is active this frame...
                if image_main.status == STARTED:
                    # update params
                    pass
                
                # *opt1* updates
                
                # if opt1 is starting this frame...
                if opt1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt1.frameNStart = frameN  # exact frame index
                    opt1.tStart = t  # local t and not account for scr refresh
                    opt1.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt1, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt1.started')
                    # update status
                    opt1.status = STARTED
                    opt1.setAutoDraw(True)
                
                # if opt1 is active this frame...
                if opt1.status == STARTED:
                    # update params
                    pass
                
                # *opt2* updates
                
                # if opt2 is starting this frame...
                if opt2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt2.frameNStart = frameN  # exact frame index
                    opt2.tStart = t  # local t and not account for scr refresh
                    opt2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt2.started')
                    # update status
                    opt2.status = STARTED
                    opt2.setAutoDraw(True)
                
                # if opt2 is active this frame...
                if opt2.status == STARTED:
                    # update params
                    pass
                
                # *opt3* updates
                
                # if opt3 is starting this frame...
                if opt3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt3.frameNStart = frameN  # exact frame index
                    opt3.tStart = t  # local t and not account for scr refresh
                    opt3.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt3, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt3.started')
                    # update status
                    opt3.status = STARTED
                    opt3.setAutoDraw(True)
                
                # if opt3 is active this frame...
                if opt3.status == STARTED:
                    # update params
                    pass
                
                # *opt4* updates
                
                # if opt4 is starting this frame...
                if opt4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    opt4.frameNStart = frameN  # exact frame index
                    opt4.tStart = t  # local t and not account for scr refresh
                    opt4.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(opt4, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'opt4.started')
                    # update status
                    opt4.status = STARTED
                    opt4.setAutoDraw(True)
                
                # if opt4 is active this frame...
                if opt4.status == STARTED:
                    # update params
                    pass
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
                if mouse.status == STARTED:  # only update if started and not finished!
                    buttons = mouse.getPressed()
                    if buttons != prevButtonState:  # button state changed?
                        prevButtonState = buttons
                        if sum(buttons) > 0:  # state changed to a new click
                            # check if the mouse was inside our 'clickable' objects
                            gotValidClick = False
                            clickableList = environmenttools.getFromNames([opt1,opt2,opt3,opt4], namespace=locals())
                            for obj in clickableList:
                                # is this object clicked on?
                                if obj.contains(mouse):
                                    gotValidClick = True
                                    mouse.clicked_name.append(obj.name)
                            # check whether click was in correct object
                            if gotValidClick:
                                _corr = 0
                                _corrAns = environmenttools.getFromNames(correct_image, namespace=locals())
                                for obj in _corrAns:
                                    # is this object clicked on?
                                    if obj.contains(mouse):
                                        _corr = 1
                                mouse.corr.append(_corr)
                            x, y = mouse.getPos()
                            mouse.x.append(x)
                            mouse.y.append(y)
                            buttons = mouse.getPressed()
                            mouse.leftButton.append(buttons[0])
                            mouse.midButton.append(buttons[1])
                            mouse.rightButton.append(buttons[2])
                            mouse.time.append(mouse.mouseClock.getTime())
                            if gotValidClick:
                                continueRoutine = False  # end routine on response
                
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
                
                # Show the timer only if there are 5 seconds or less remaining
                if remaining_time <= 5:
                    # Update the timer text
                    text_timer.setText(f'{remaining_time:.0f}')
                    text_timer.setAutoDraw(True)  # Make sure the timer text is drawn
                else:
                    text_timer.setAutoDraw(False)  # Hide the timer text
                
                # End the routine if time is up
                if remaining_time <= 0:
                    continueRoutine = False
                
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trialComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial" ---
            for thisComponent in trialComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial.stopped', globalClock.getTime(format='float'))
            # store data for trials (TrialHandler)
            trials.addData('mouse.x', mouse.x)
            trials.addData('mouse.y', mouse.y)
            trials.addData('mouse.leftButton', mouse.leftButton)
            trials.addData('mouse.midButton', mouse.midButton)
            trials.addData('mouse.rightButton', mouse.rightButton)
            trials.addData('mouse.time', mouse.time)
            trials.addData('mouse.corr', mouse.corr)
            trials.addData('mouse.clicked_name', mouse.clicked_name)
            # Run 'End Routine' code from code_mouse
            # Check which option was clicked and store the choice
            if mouse.isPressedIn(opt1):
                choice = 'opt1'
            elif mouse.isPressedIn(opt2):
                choice = 'opt2'
            elif mouse.isPressedIn(opt3):
                choice = 'opt3'
            elif mouse.isPressedIn(opt4):
                choice = 'opt4'
            
            # If a choice was made, send the corresponding LSL marker and store the response
            if choice:
                send_marker(choice)  # Function to send the LSL marker
                thisExp.addData('resp_mouse', choice)  # Add the choice to the data file
            else:
                thisExp.addData('resp_mouse', 'no_response')  # Handle case where no choice was made
            
            # Run 'End Routine' code from code_LSL_trial
            answer_corr = f"response_{mouse.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # the Routine "trial" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'trials'
        
        # get names of stimulus parameters
        if trials.trialList in ([], [None], None):
            params = []
        else:
            params = trials.trialList[0].keys()
        # save data for this loop
        trials.saveAsExcel(filename + '.xlsx', sheetName='trials',
            stimOut=params,
            dataOut=['n','all_mean','all_std', 'all_raw'])
    # completed 1.0 repeats of 'testblocks'
    
    
    # --- Prepare to start Routine "done" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('done.started', globalClock.getTime(format='float'))
    key_resp_2.keys = []
    key_resp_2.rt = []
    _key_resp_2_allKeys = []
    # Run 'Begin Routine' code from code_end_text
    # Set the text for the third set of instructions
    end_text.setText(instructions['Text_end_task'])
    
    # keep track of which components have finished
    doneComponents = [end_text, key_resp_2]
    for thisComponent in doneComponents:
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
    
    # --- Run Routine "done" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *end_text* updates
        
        # if end_text is starting this frame...
        if end_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_text.frameNStart = frameN  # exact frame index
            end_text.tStart = t  # local t and not account for scr refresh
            end_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_text, 'tStartRefresh')  # time at next scr refresh
            # update status
            end_text.status = STARTED
            end_text.setAutoDraw(True)
        
        # if end_text is active this frame...
        if end_text.status == STARTED:
            # update params
            pass
        
        # *key_resp_2* updates
        waitOnFlip = False
        
        # if key_resp_2 is starting this frame...
        if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_2.frameNStart = frameN  # exact frame index
            key_resp_2.tStart = t  # local t and not account for scr refresh
            key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
            # update status
            key_resp_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_2.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _key_resp_2_allKeys.extend(theseKeys)
            if len(_key_resp_2_allKeys):
                key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
                key_resp_2.rt = _key_resp_2_allKeys[-1].rt
                key_resp_2.duration = _key_resp_2_allKeys[-1].duration
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
        for thisComponent in doneComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "done" ---
    for thisComponent in doneComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('done.stopped', globalClock.getTime(format='float'))
    # Run 'End Routine' code from LSL_MARS_end
    send_marker('MARS_end')
    thisExp.nextEntry()
    # the Routine "done" was not non-slip safe, so reset the non-slip timer
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
