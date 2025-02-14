#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 18:07
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
expName = 'ColorShape'  # from the Builder filename that created this script
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Switch_ColorShape\\ColorShape_lastrun.py',
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
            monitor='testMonitor', color=[-1,-1,-1], colorSpace='rgb',
            backgroundImage='', backgroundFit='none',
            blendMode='avg', useFBO=True,
            units='height', 
            checkTiming=False  # we're going to do this ourselves in a moment
        )
    else:
        # if we have a window, just set the attributes which are safe to set
        win.color = [-1,-1,-1]
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
    if deviceManager.getDevice('end_inst') is None:
        # initialise end_inst
        end_inst = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='end_inst',
        )
    if deviceManager.getDevice('startPractice') is None:
        # initialise startPractice
        startPractice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startPractice',
        )
    if deviceManager.getDevice('response_practice') is None:
        # initialise response_practice
        response_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_practice',
        )
    if deviceManager.getDevice('start_Task') is None:
        # initialise start_Task
        start_Task = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='start_Task',
        )
    if deviceManager.getDevice('response') is None:
        # initialise response
        response = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response',
        )
    if deviceManager.getDevice('Unpause') is None:
        # initialise Unpause
        Unpause = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='Unpause',
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
    
    # Load the scenario file
    scenario_df = pd.read_csv('color_shape_task_scenario.csv')
    
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
            'name_task' : 'COLOR-SHAPE',
            'Introduction': "Welcome to the 'COLOR-SHAPE' task.\n\nIn this task, you will see one of four stimuli (green circle, green triangle, red circle, red triangle), appearing one at a time.\n\nSometimes you will be asked to respond to the COLOR; at other times, you will be asked to respond to the SHAPE of the stimulus.",
            'Practice_Color_Only': "If you see a 'C' on the screen, you will be asked to respond to the COLOR of the stimulus that appears.\n\nIf it is GREEN, press the 'd' key.\nIf it is RED, press the 'k' key.\n\nPress the space bar to begin the practice session for color only.",
            'Practice_Shape_Only': "If you see a 'S' on the screen, you will be asked to respond to the SHAPE of the stimulus that appears.\n\nIf it is a CIRCLE, press the 'd' key.\nIf it is a TRIANGLE, press the 'k' key.\n\nPress the space bar to begin the practice session for shape only.",
            'Practice_Both': "You will now practice responding to both SHAPE and COLOR.\n\nPay attention to the cues and respond to the objects as quickly as possible without making too many errors.\n\nPress the space bar to begin the practice session.",
            'Start_Actual_Task': "The training is over. Let's start the real task.\n\nThe actual task consists of 4 rounds. Each round lasts about 2 minutes.\n\nPress the space bar to start.",
            'Pause': "Pause\n\nPress the space bar when you are ready to continue",
            'text_end_task': "This task is now over.\n\nThank you!\n\nPress the space bar to continue"
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task' : 'COLOR-SHAPE',
            'Introduction': "Bienvenue dans la tâche 'COLOR-SHAPE'.\n\nDans cette tâche, vous verrez un stimulus parmi quatre (cercle vert, triangle vert, cercle rouge, triangle rouge), apparaissant un à la fois.\n\nParfois, on vous demandera de répondre selon la COULEUR; à d'autres moments, on vous demandera de répondre selon la FORME du stimulus.",
            'Practice_Color_Only': "Si vous voyez un 'C' à l'écran, il vous sera demandé de répondre à la COULEUR du stimulus qui apparaîtra.\n\nSi l'objet est VERT, appuyez sur la touche 'd'.\nSi l'objet est ROUGE, appuyez sur la touche 'k'.\n\nAppuyez sur la barre d'espace pour commencer la session d'entraînement pour la couleur uniquement.",
            'Practice_Shape_Only': "Si vous voyez un 'F' à l'écran, il vous sera demandé de répondre à la FORME du stimulus qui apparaîtra.\n\nSi l'objet est un CERCLE, appuyez sur la touche 'd'.\nSi l'objet est un TRIANGLE, appuyez sur la touche 'k'.\n\nAppuyez sur la barre d'espace pour commencer la session d'entraînement pour la forme uniquement.",
            'Practice_Both': "Vous allez maintenant vous entraîner à répondre à la fois à la FORME et à la COULEUR.\n\nFaites attention aux indices et répondez aux stimuli aussi vite que possible sans faire trop d'erreurs.\n\nAppuyez sur la barre d'espace pour commencer la session d'entraînement.",
            'Start_Actual_Task': "L'entrainement est terminé. Passons maintenant à la vraie tâche.\n\nCette dernière se composera de 4 tours. Chaque tour durera environ 2 minutes.\n\nAppuyez sur la barre d'espace pour commencer.",
            'Pause': "Pause\n\nAppuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer",
            'text_end_task': "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer"
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
    
    
    # --- Initialize components for Routine "instruction_global" ---
    instruction_text_component_introduction = visual.TextStim(win=win, name='instruction_text_component_introduction',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    end_inst = keyboard.Keyboard(deviceName='end_inst')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "block_counter_practice" ---
    
    # --- Initialize components for Routine "instructions_practice" ---
    startPractice = keyboard.Keyboard(deviceName='startPractice')
    text_practice = visual.TextStim(win=win, name='text_practice',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "trial_practice" ---
    response_practice = keyboard.Keyboard(deviceName='response_practice')
    ITI_practice = visual.TextStim(win=win, name='ITI_practice',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instruction_text_component_practice = visual.TextStim(win=win, name='instruction_text_component_practice',
        text=None,
        font='Arial',
        pos=(0, 0.35), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stimulus_image_practice = visual.ImageStim(
        win=win,
        name='stimulus_image_practice', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    instruction_d = visual.TextStim(win=win, name='instruction_d',
        text=None,
        font='Arial',
        pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    instruction_k = visual.TextStim(win=win, name='instruction_k',
        text=None,
        font='Arial',
        pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-6.0);
    
    # --- Initialize components for Routine "feedback" ---
    feedback_text = visual.TextStim(win=win, name='feedback_text',
        text='',
        font='Arial',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instruction_d_2 = visual.TextStim(win=win, name='instruction_d_2',
        text=None,
        font='Arial',
        pos=(-0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    instruction_k_2 = visual.TextStim(win=win, name='instruction_k_2',
        text=None,
        font='Arial',
        pos=(0.4, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "increment_block_practice" ---
    
    # --- Initialize components for Routine "startTask" ---
    instruction_text_component_start_task = visual.TextStim(win=win, name='instruction_text_component_start_task',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    start_Task = keyboard.Keyboard(deviceName='start_Task')
    
    # --- Initialize components for Routine "block_counter" ---
    # Run 'Begin Experiment' code from LSL_start_testblock
    send_marker("start_block")
    
    # --- Initialize components for Routine "trial_test" ---
    response = keyboard.Keyboard(deviceName='response')
    ITI = visual.TextStim(win=win, name='ITI',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    instruction_text_component = visual.TextStim(win=win, name='instruction_text_component',
        text=None,
        font='Arial',
        pos=(0, 0.35), height=0.1, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    stimulus_image = visual.ImageStim(
        win=win,
        name='stimulus_image', 
        image='default.png', mask=None, anchor='center',
        ori=0.0, pos=(0, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-3.0)
    
    # --- Initialize components for Routine "feedback_test" ---
    feedback_text_test = visual.TextStim(win=win, name='feedback_text_test',
        text='',
        font='Arial',
        pos=(0, 0), height=0.2, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "pause" ---
    instruction_text_component_pause = visual.TextStim(win=win, name='instruction_text_component_pause',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    Unpause = keyboard.Keyboard(deviceName='Unpause')
    
    # --- Initialize components for Routine "thanks" ---
    InstructionsText4 = visual.TextStim(win=win, name='InstructionsText4',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    # Run 'Begin Experiment' code from code_InstructionThanks
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['text_end_task'])
    
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
    
    # --- Prepare to start Routine "instruction_global" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instruction_global.started', globalClock.getTime(format='float'))
    instruction_text_component_introduction.setText('')
    end_inst.keys = []
    end_inst.rt = []
    _end_inst_allKeys = []
    # Run 'Begin Routine' code from code_Instructions
    instruction_text_component_introduction.text = instructions['Introduction']
    
    # Run 'Begin Routine' code from LSL_CS_start
    send_marker('ColorShape_start')
    # Run 'Begin Routine' code from code_block_variable
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_practice = True
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instruction_globalComponents = [instruction_text_component_introduction, end_inst, nametask]
    for thisComponent in instruction_globalComponents:
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
    
    # --- Run Routine "instruction_global" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_text_component_introduction* updates
        
        # if instruction_text_component_introduction is starting this frame...
        if instruction_text_component_introduction.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text_component_introduction.frameNStart = frameN  # exact frame index
            instruction_text_component_introduction.tStart = t  # local t and not account for scr refresh
            instruction_text_component_introduction.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text_component_introduction, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text_component_introduction.started')
            # update status
            instruction_text_component_introduction.status = STARTED
            instruction_text_component_introduction.setAutoDraw(True)
        
        # if instruction_text_component_introduction is active this frame...
        if instruction_text_component_introduction.status == STARTED:
            # update params
            pass
        
        # *end_inst* updates
        waitOnFlip = False
        
        # if end_inst is starting this frame...
        if end_inst.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_inst.frameNStart = frameN  # exact frame index
            end_inst.tStart = t  # local t and not account for scr refresh
            end_inst.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_inst, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_inst.started')
            # update status
            end_inst.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_inst.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_inst.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_inst.status == STARTED and not waitOnFlip:
            theseKeys = end_inst.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _end_inst_allKeys.extend(theseKeys)
            if len(_end_inst_allKeys):
                end_inst.keys = _end_inst_allKeys[-1].name  # just the last key pressed
                end_inst.rt = _end_inst_allKeys[-1].rt
                end_inst.duration = _end_inst_allKeys[-1].duration
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
        for thisComponent in instruction_globalComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instruction_global" ---
    for thisComponent in instruction_globalComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instruction_global.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instruction_global" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('color_shape_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
        seed=None, name='practiceblocks')
    thisExp.addLoop(practiceblocks)  # add the loop to the experiment
    thisPracticeblock = practiceblocks.trialList[0]  # so we can initialise stimuli with some values
    # abbreviate parameter names if possible (e.g. rgb = thisPracticeblock.rgb)
    if thisPracticeblock != None:
        for paramName in thisPracticeblock:
            globals()[paramName] = thisPracticeblock[paramName]
    
    for thisPracticeblock in practiceblocks:
        currentLoop = practiceblocks
        thisExp.timestampOnFlip(win, 'thisRow.t', format=globalClock.format)
        # pause experiment here if requested
        if thisExp.status == PAUSED:
            pauseExperiment(
                thisExp=thisExp, 
                win=win, 
                timers=[routineTimer], 
                playbackComponents=[]
        )
        # abbreviate parameter names if possible (e.g. rgb = thisPracticeblock.rgb)
        if thisPracticeblock != None:
            for paramName in thisPracticeblock:
                globals()[paramName] = thisPracticeblock[paramName]
        
        # --- Prepare to start Routine "block_counter_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('block_counter_practice.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from blockSetup_practice
        # Increment block counter
        block_index += 1
        
        # Determine the current block type and number
        # block_type = 'test'
        if block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique()):
            # Skip the remaining test blocks
            practiceblocks.finished = True
            continueRoutine = False
        else:
            block_n = block_index  # block_n in CSV starts from 1
        
        
        # keep track of which components have finished
        block_counter_practiceComponents = []
        for thisComponent in block_counter_practiceComponents:
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
        
        # --- Run Routine "block_counter_practice" ---
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
            for thisComponent in block_counter_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "block_counter_practice" ---
        for thisComponent in block_counter_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('block_counter_practice.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from LSL_start_testblock_practice
        send_marker("start_block_practice")
        # the Routine "block_counter_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "instructions_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructions_practice.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_InstructionsPractice
        # Extract block_type for the current block
        current_block_type = scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)]['block_type'].values[0]
        
        # Set the instruction text based on the block type
        if current_block_type == 'color':
            text_practice.text = instructions['Practice_Color_Only']
        elif current_block_type == 'shape':
            text_practice.text = instructions['Practice_Shape_Only']
        elif current_block_type == 'both':
            text_practice.text = instructions['Practice_Both']
        
        startPractice.keys = []
        startPractice.rt = []
        _startPractice_allKeys = []
        # keep track of which components have finished
        instructions_practiceComponents = [startPractice, text_practice]
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
            
            # *startPractice* updates
            waitOnFlip = False
            
            # if startPractice is starting this frame...
            if startPractice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                startPractice.frameNStart = frameN  # exact frame index
                startPractice.tStart = t  # local t and not account for scr refresh
                startPractice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(startPractice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'startPractice.started')
                # update status
                startPractice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(startPractice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(startPractice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if startPractice.status == STARTED and not waitOnFlip:
                theseKeys = startPractice.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _startPractice_allKeys.extend(theseKeys)
                if len(_startPractice_allKeys):
                    startPractice.keys = _startPractice_allKeys[-1].name  # just the last key pressed
                    startPractice.rt = _startPractice_allKeys[-1].rt
                    startPractice.duration = _startPractice_allKeys[-1].duration
                    # a response ends the routine
                    continueRoutine = False
            
            # *text_practice* updates
            
            # if text_practice is starting this frame...
            if text_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_practice.frameNStart = frameN  # exact frame index
                text_practice.tStart = t  # local t and not account for scr refresh
                text_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_practice.started')
                # update status
                text_practice.status = STARTED
                text_practice.setAutoDraw(True)
            
            # if text_practice is active this frame...
            if text_practice.status == STARTED:
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
        send_marker('practice_block')
        # the Routine "instructions_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practiceTrials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('color_shape_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "trial_practice" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial_practice.started', globalClock.getTime(format='float'))
            response_practice.keys = []
            response_practice.rt = []
            _response_practice_allKeys = []
            ITI_practice.setText('')
            instruction_text_component_practice.setText('')
            stimulus_image_practice.setImage(stimulus)
            # Run 'Begin Routine' code from code_instruction_text
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
                if current_block_type == 'color':
                    instruction_text_component_practice.text = instruction_eng
                    instruction_d.text = 'd\ngreen'
                    instruction_k.text = 'k\nred'
                elif current_block_type == 'shape':
                    instruction_text_component_practice.text = instruction_eng
                    instruction_d.text = 'd\ncircle'
                    instruction_k.text = 'k\ntriangle'
                elif current_block_type == 'both':
                    instruction_text_component_practice.text = instruction_eng
                    instruction_d.text = 'd\ngreen\ncircle'
                    instruction_k.text = 'k\nred\ntriangle'
            else:
                if current_block_type == 'color':
                    instruction_text_component_practice.text = instruction_fr
                    instruction_d.text = 'd\nvert'
                    instruction_k.text = 'k\nrouge'
                elif current_block_type == 'shape':
                    instruction_text_component_practice.text = instruction_fr
                    instruction_d.text = 'd\ncercle'
                    instruction_k.text = 'k\ntriangle'
                elif current_block_type == 'both':
                    instruction_text_component_practice.text = instruction_fr
                    instruction_d.text = 'd\nvert\ncercle'
                    instruction_k.text = 'k\nrouge\ntriangle'
            # keep track of which components have finished
            trial_practiceComponents = [response_practice, ITI_practice, instruction_text_component_practice, stimulus_image_practice, instruction_d, instruction_k]
            for thisComponent in trial_practiceComponents:
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
            
            # --- Run Routine "trial_practice" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *response_practice* updates
                waitOnFlip = False
                
                # if response_practice is starting this frame...
                if response_practice.status == NOT_STARTED and frameN >= iti_60hz+soa_60hz:
                    # keep track of start time/frame for later
                    response_practice.frameNStart = frameN  # exact frame index
                    response_practice.tStart = t  # local t and not account for scr refresh
                    response_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_practice.started')
                    # update status
                    response_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                if response_practice.status == STARTED and not waitOnFlip:
                    theseKeys = response_practice.getKeys(keyList=['d','k'], ignoreKeys=None, waitRelease=False)
                    _response_practice_allKeys.extend(theseKeys)
                    if len(_response_practice_allKeys):
                        response_practice.keys = _response_practice_allKeys[0].name  # just the first key pressed
                        response_practice.rt = _response_practice_allKeys[0].rt
                        response_practice.duration = _response_practice_allKeys[0].duration
                        # was this correct?
                        if (response_practice.keys == str(correct_resp)) or (response_practice.keys == correct_resp):
                            response_practice.corr = 1
                        else:
                            response_practice.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *ITI_practice* updates
                
                # if ITI_practice is starting this frame...
                if ITI_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI_practice.frameNStart = frameN  # exact frame index
                    ITI_practice.tStart = t  # local t and not account for scr refresh
                    ITI_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI_practice.started')
                    # update status
                    ITI_practice.status = STARTED
                    ITI_practice.setAutoDraw(True)
                
                # if ITI_practice is active this frame...
                if ITI_practice.status == STARTED:
                    # update params
                    pass
                
                # if ITI_practice is stopping this frame...
                if ITI_practice.status == STARTED:
                    if frameN >= iti_60hz:
                        # keep track of stop time/frame for later
                        ITI_practice.tStop = t  # not accounting for scr refresh
                        ITI_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        ITI_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI_practice.stopped')
                        # update status
                        ITI_practice.status = FINISHED
                        ITI_practice.setAutoDraw(False)
                
                # *instruction_text_component_practice* updates
                
                # if instruction_text_component_practice is starting this frame...
                if instruction_text_component_practice.status == NOT_STARTED and frameN >= iti_60hz:
                    # keep track of start time/frame for later
                    instruction_text_component_practice.frameNStart = frameN  # exact frame index
                    instruction_text_component_practice.tStart = t  # local t and not account for scr refresh
                    instruction_text_component_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_text_component_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_text_component_practice.started')
                    # update status
                    instruction_text_component_practice.status = STARTED
                    instruction_text_component_practice.setAutoDraw(True)
                
                # if instruction_text_component_practice is active this frame...
                if instruction_text_component_practice.status == STARTED:
                    # update params
                    pass
                
                # *stimulus_image_practice* updates
                
                # if stimulus_image_practice is starting this frame...
                if stimulus_image_practice.status == NOT_STARTED and frameN >= iti_60hz+soa_60hz:
                    # keep track of start time/frame for later
                    stimulus_image_practice.frameNStart = frameN  # exact frame index
                    stimulus_image_practice.tStart = t  # local t and not account for scr refresh
                    stimulus_image_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus_image_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus_image_practice.started')
                    # update status
                    stimulus_image_practice.status = STARTED
                    stimulus_image_practice.setAutoDraw(True)
                
                # if stimulus_image_practice is active this frame...
                if stimulus_image_practice.status == STARTED:
                    # update params
                    pass
                
                # *instruction_d* updates
                
                # if instruction_d is starting this frame...
                if instruction_d.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_d.frameNStart = frameN  # exact frame index
                    instruction_d.tStart = t  # local t and not account for scr refresh
                    instruction_d.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_d, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_d.started')
                    # update status
                    instruction_d.status = STARTED
                    instruction_d.setAutoDraw(True)
                
                # if instruction_d is active this frame...
                if instruction_d.status == STARTED:
                    # update params
                    pass
                
                # *instruction_k* updates
                
                # if instruction_k is starting this frame...
                if instruction_k.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_k.frameNStart = frameN  # exact frame index
                    instruction_k.tStart = t  # local t and not account for scr refresh
                    instruction_k.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_k, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_k.started')
                    # update status
                    instruction_k.status = STARTED
                    instruction_k.setAutoDraw(True)
                
                # if instruction_k is active this frame...
                if instruction_k.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from LSL_stimulus_practice
                # Check if the current frame matches the isi_frame60hz value
                if frameN == iti_60hz+soa_60hz:
                    # Send the marker with the stimulus type
                    send_marker("stimulus_" + instruction + "_" + trial_type + "_" + stimulus)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_practiceComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_practice" ---
            for thisComponent in trial_practiceComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial_practice.stopped', globalClock.getTime(format='float'))
            # check responses
            if response_practice.keys in ['', [], None]:  # No response was made
                response_practice.keys = None
                # was no response the correct answer?!
                if str(correct_resp).lower() == 'none':
                   response_practice.corr = 1;  # correct non-response
                else:
                   response_practice.corr = 0;  # failed to respond (incorrectly)
            # store data for practiceTrials (TrialHandler)
            practiceTrials.addData('response_practice.keys',response_practice.keys)
            practiceTrials.addData('response_practice.corr', response_practice.corr)
            if response_practice.keys != None:  # we had a response
                practiceTrials.addData('response_practice.rt', response_practice.rt)
                practiceTrials.addData('response_practice.duration', response_practice.duration)
            # Run 'End Routine' code from LSL_stimulus_practice
            answer_corr = f"response_{response_practice.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # the Routine "trial_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('feedback.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from set_feedback
            if not response_practice.corr:  # Check if the response is incorrect
                feedback_message = 'X'  # Set the feedback message to a red cross
                feedback_text.color = 'red'  # Set the color to red
            else:
                feedback_message = ''  # No feedback if correct
            
            feedback_text.setText(feedback_message)
            # Run 'Begin Routine' code from code_instruction_text_2
            # Determine the block type for the current block
            current_block_type = scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)]['block_type'].values[0]
            
            if language == "English":
                if current_block_type == 'color':
                    instruction_d_2.text = 'd\ngreen'
                    instruction_k_2.text = 'k\nred'
                elif current_block_type == 'shape':
                    instruction_d_2.text = 'd\ncircle'
                    instruction_k_2.text = 'k\ntriangle'
                elif current_block_type == 'both':
                    instruction_d_2.text = 'd\ngreen\ncircle'
                    instruction_k_2.text = 'k\nred\ntriangle'
            else:
                if current_block_type == 'color':
                    instruction_d_2.text = 'd\nvert'
                    instruction_k_2.text = 'k\nrouge'
                elif current_block_type == 'shape':
                    instruction_d_2.text = 'd\ncercle'
                    instruction_k_2.text = 'k\ntriangle'
                elif current_block_type == 'both':
                    instruction_d_2.text = 'd\nvert\ncercle'
                    instruction_k_2.text = 'k\nrouge\ntriangle'
            # keep track of which components have finished
            feedbackComponents = [feedback_text, instruction_d_2, instruction_k_2]
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
                
                # *instruction_d_2* updates
                
                # if instruction_d_2 is starting this frame...
                if instruction_d_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_d_2.frameNStart = frameN  # exact frame index
                    instruction_d_2.tStart = t  # local t and not account for scr refresh
                    instruction_d_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_d_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_d_2.started')
                    # update status
                    instruction_d_2.status = STARTED
                    instruction_d_2.setAutoDraw(True)
                
                # if instruction_d_2 is active this frame...
                if instruction_d_2.status == STARTED:
                    # update params
                    pass
                
                # if instruction_d_2 is stopping this frame...
                if instruction_d_2.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        instruction_d_2.tStop = t  # not accounting for scr refresh
                        instruction_d_2.tStopRefresh = tThisFlipGlobal  # on global time
                        instruction_d_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instruction_d_2.stopped')
                        # update status
                        instruction_d_2.status = FINISHED
                        instruction_d_2.setAutoDraw(False)
                
                # *instruction_k_2* updates
                
                # if instruction_k_2 is starting this frame...
                if instruction_k_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    instruction_k_2.frameNStart = frameN  # exact frame index
                    instruction_k_2.tStart = t  # local t and not account for scr refresh
                    instruction_k_2.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_k_2, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_k_2.started')
                    # update status
                    instruction_k_2.status = STARTED
                    instruction_k_2.setAutoDraw(True)
                
                # if instruction_k_2 is active this frame...
                if instruction_k_2.status == STARTED:
                    # update params
                    pass
                
                # if instruction_k_2 is stopping this frame...
                if instruction_k_2.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        instruction_k_2.tStop = t  # not accounting for scr refresh
                        instruction_k_2.tStopRefresh = tThisFlipGlobal  # on global time
                        instruction_k_2.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'instruction_k_2.stopped')
                        # update status
                        instruction_k_2.status = FINISHED
                        instruction_k_2.setAutoDraw(False)
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
        # completed 1.0 repeats of 'practiceTrials'
        
        
        # --- Prepare to start Routine "increment_block_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('increment_block_practice.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from check_block_counter_2
        # Check if the block is test and block_n is to skip the loop
        if is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique()):
            practiceblocks.finished = True  # Skip the loop
        # keep track of which components have finished
        increment_block_practiceComponents = []
        for thisComponent in increment_block_practiceComponents:
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
        
        # --- Run Routine "increment_block_practice" ---
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
            for thisComponent in increment_block_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "increment_block_practice" ---
        for thisComponent in increment_block_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('increment_block_practice.stopped', globalClock.getTime(format='float'))
        # the Routine "increment_block_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'practiceblocks'
    
    
    # --- Prepare to start Routine "startTask" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('startTask.started', globalClock.getTime(format='float'))
    start_Task.keys = []
    start_Task.rt = []
    _start_Task_allKeys = []
    # Run 'Begin Routine' code from code_InstructionsStartTask
    instruction_text_component_start_task.text = instructions['Start_Actual_Task']
    
    # Run 'Begin Routine' code from define_block_rows
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_test = True
    # keep track of which components have finished
    startTaskComponents = [instruction_text_component_start_task, start_Task]
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
        
        # *instruction_text_component_start_task* updates
        
        # if instruction_text_component_start_task is starting this frame...
        if instruction_text_component_start_task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text_component_start_task.frameNStart = frameN  # exact frame index
            instruction_text_component_start_task.tStart = t  # local t and not account for scr refresh
            instruction_text_component_start_task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text_component_start_task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text_component_start_task.started')
            # update status
            instruction_text_component_start_task.status = STARTED
            instruction_text_component_start_task.setAutoDraw(True)
        
        # if instruction_text_component_start_task is active this frame...
        if instruction_text_component_start_task.status == STARTED:
            # update params
            pass
        
        # *start_Task* updates
        waitOnFlip = False
        
        # if start_Task is starting this frame...
        if start_Task.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_Task.frameNStart = frameN  # exact frame index
            start_Task.tStart = t  # local t and not account for scr refresh
            start_Task.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_Task, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'start_Task.started')
            # update status
            start_Task.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_Task.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_Task.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_Task.status == STARTED and not waitOnFlip:
            theseKeys = start_Task.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _start_Task_allKeys.extend(theseKeys)
            if len(_start_Task_allKeys):
                start_Task.keys = _start_Task_allKeys[-1].name  # just the last key pressed
                start_Task.rt = _start_Task_allKeys[-1].rt
                start_Task.duration = _start_Task_allKeys[-1].duration
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
    # Run 'End Routine' code from LSL_start_task
    send_marker("block")
    thisExp.nextEntry()
    # the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('color_shape_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        testTrials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('color_shape_task_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "trial_test" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('trial_test.started', globalClock.getTime(format='float'))
            response.keys = []
            response.rt = []
            _response_allKeys = []
            ITI.setText('')
            instruction_text_component.setText('')
            stimulus_image.setImage(stimulus)
            # Run 'Begin Routine' code from code
            # Check if expInfo exists and create the language variable
            if 'expInfo' not in globals():
                expInfo = {}
            
            # Set default values to English if it is missing from expInfo keys
            if 'language' not in expInfo:
                expInfo['language'] = 'English'
            
            # Create the language variable
            language = expInfo.get('language')
            
            # Set the instruction text based on the language
            if language == "English":
                instruction_text_component.text = instruction_eng
            else:
                instruction_text_component.text = instruction_fr
            
            # keep track of which components have finished
            trial_testComponents = [response, ITI, instruction_text_component, stimulus_image]
            for thisComponent in trial_testComponents:
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
            
            # --- Run Routine "trial_test" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *response* updates
                waitOnFlip = False
                
                # if response is starting this frame...
                if response.status == NOT_STARTED and frameN >= iti_60hz+soa_60hz:
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
                        response.keys = _response_allKeys[0].name  # just the first key pressed
                        response.rt = _response_allKeys[0].rt
                        response.duration = _response_allKeys[0].duration
                        # was this correct?
                        if (response.keys == str(correct_resp)) or (response.keys == correct_resp):
                            response.corr = 1
                        else:
                            response.corr = 0
                        # a response ends the routine
                        continueRoutine = False
                
                # *ITI* updates
                
                # if ITI is starting this frame...
                if ITI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    ITI.frameNStart = frameN  # exact frame index
                    ITI.tStart = t  # local t and not account for scr refresh
                    ITI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ITI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ITI.started')
                    # update status
                    ITI.status = STARTED
                    ITI.setAutoDraw(True)
                
                # if ITI is active this frame...
                if ITI.status == STARTED:
                    # update params
                    pass
                
                # if ITI is stopping this frame...
                if ITI.status == STARTED:
                    if frameN >= iti_60hz:
                        # keep track of stop time/frame for later
                        ITI.tStop = t  # not accounting for scr refresh
                        ITI.tStopRefresh = tThisFlipGlobal  # on global time
                        ITI.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ITI.stopped')
                        # update status
                        ITI.status = FINISHED
                        ITI.setAutoDraw(False)
                
                # *instruction_text_component* updates
                
                # if instruction_text_component is starting this frame...
                if instruction_text_component.status == NOT_STARTED and frameN >= iti_60hz:
                    # keep track of start time/frame for later
                    instruction_text_component.frameNStart = frameN  # exact frame index
                    instruction_text_component.tStart = t  # local t and not account for scr refresh
                    instruction_text_component.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(instruction_text_component, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'instruction_text_component.started')
                    # update status
                    instruction_text_component.status = STARTED
                    instruction_text_component.setAutoDraw(True)
                
                # if instruction_text_component is active this frame...
                if instruction_text_component.status == STARTED:
                    # update params
                    pass
                
                # *stimulus_image* updates
                
                # if stimulus_image is starting this frame...
                if stimulus_image.status == NOT_STARTED and frameN >= iti_60hz+soa_60hz:
                    # keep track of start time/frame for later
                    stimulus_image.frameNStart = frameN  # exact frame index
                    stimulus_image.tStart = t  # local t and not account for scr refresh
                    stimulus_image.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus_image, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus_image.started')
                    # update status
                    stimulus_image.status = STARTED
                    stimulus_image.setAutoDraw(True)
                
                # if stimulus_image is active this frame...
                if stimulus_image.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from LSL_stimulus
                # Check if the current frame matches the isi_frame60hz value
                if frameN == iti_60hz+soa_60hz:
                    # Send the marker with the stimulus type
                    send_marker("stimulus_" + instruction + "_" + trial_type + "_" + stimulus)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in trial_testComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "trial_test" ---
            for thisComponent in trial_testComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('trial_test.stopped', globalClock.getTime(format='float'))
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
            # Run 'End Routine' code from LSL_stimulus
            answer_corr = f"response_{response.corr}"
            send_marker(answer_corr)  # Function to send the LSL marker
            
            
            # the Routine "trial_test" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "feedback_test" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('feedback_test.started', globalClock.getTime(format='float'))
            # Run 'Begin Routine' code from set_feedback_test
            if not response.corr:  # Check if the response is incorrect
                feedback_message = ''  # No feedback (test trials)
            else:
                feedback_message = ''  # No feedback if correct
            
            feedback_text_test.setText(feedback_message)
            # keep track of which components have finished
            feedback_testComponents = [feedback_text_test]
            for thisComponent in feedback_testComponents:
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
            
            # --- Run Routine "feedback_test" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *feedback_text_test* updates
                
                # if feedback_text_test is starting this frame...
                if feedback_text_test.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    feedback_text_test.frameNStart = frameN  # exact frame index
                    feedback_text_test.tStart = t  # local t and not account for scr refresh
                    feedback_text_test.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_text_test, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_text_test.started')
                    # update status
                    feedback_text_test.status = STARTED
                    feedback_text_test.setAutoDraw(True)
                
                # if feedback_text_test is active this frame...
                if feedback_text_test.status == STARTED:
                    # update params
                    pass
                
                # if feedback_text_test is stopping this frame...
                if feedback_text_test.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        feedback_text_test.tStop = t  # not accounting for scr refresh
                        feedback_text_test.tStopRefresh = tThisFlipGlobal  # on global time
                        feedback_text_test.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'feedback_text_test.stopped')
                        # update status
                        feedback_text_test.status = FINISHED
                        feedback_text_test.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in feedback_testComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "feedback_test" ---
            for thisComponent in feedback_testComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('feedback_test.stopped', globalClock.getTime(format='float'))
            # the Routine "feedback_test" was not non-slip safe, so reset the non-slip timer
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
        instruction_text_component_pause.setText('')
        Unpause.keys = []
        Unpause.rt = []
        _Unpause_allKeys = []
        # Run 'Begin Routine' code from code_InstructionsPause
        instruction_text_component_pause.text = instructions['Pause']
        
        
        # Run 'Begin Routine' code from check_block_counter
        # Check if the block is test and block_n is to skip the loop
        if is_test and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
            testblocks.finished = True  # Skip the loop
        # keep track of which components have finished
        pauseComponents = [instruction_text_component_pause, Unpause]
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
            
            # *instruction_text_component_pause* updates
            
            # if instruction_text_component_pause is starting this frame...
            if instruction_text_component_pause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                instruction_text_component_pause.frameNStart = frameN  # exact frame index
                instruction_text_component_pause.tStart = t  # local t and not account for scr refresh
                instruction_text_component_pause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(instruction_text_component_pause, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'instruction_text_component_pause.started')
                # update status
                instruction_text_component_pause.status = STARTED
                instruction_text_component_pause.setAutoDraw(True)
            
            # if instruction_text_component_pause is active this frame...
            if instruction_text_component_pause.status == STARTED:
                # update params
                pass
            
            # *Unpause* updates
            waitOnFlip = False
            
            # if Unpause is starting this frame...
            if Unpause.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                Unpause.frameNStart = frameN  # exact frame index
                Unpause.tStart = t  # local t and not account for scr refresh
                Unpause.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(Unpause, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'Unpause.started')
                # update status
                Unpause.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(Unpause.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(Unpause.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if Unpause.status == STARTED and not waitOnFlip:
                theseKeys = Unpause.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _Unpause_allKeys.extend(theseKeys)
                if len(_Unpause_allKeys):
                    Unpause.keys = _Unpause_allKeys[-1].name  # just the last key pressed
                    Unpause.rt = _Unpause_allKeys[-1].rt
                    Unpause.duration = _Unpause_allKeys[-1].duration
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
        if Unpause.keys in ['', [], None]:  # No response was made
            Unpause.keys = None
        testblocks.addData('Unpause.keys',Unpause.keys)
        if Unpause.keys != None:  # we had a response
            testblocks.addData('Unpause.rt', Unpause.rt)
            testblocks.addData('Unpause.duration', Unpause.duration)
        # the Routine "pause" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'testblocks'
    
    
    # --- Prepare to start Routine "thanks" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('thanks.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from LSL_ColorShape_end
    send_marker('ColorShape_end')
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
