#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on janvier 29, 2025, at 18:03
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
expName = 'DualNback'  # from the Builder filename that created this script
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
        originPath='E:\\OneDrive - ISAE-SUPAERO\\MPH\\tasks\\Updating_DualNback\\DualNback_lastrun.py',
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
    if deviceManager.getDevice('startInst_practice') is None:
        # initialise startInst_practice
        startInst_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startInst_practice',
        )
    if deviceManager.getDevice('startInst') is None:
        # initialise startInst
        startInst = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='startInst',
        )
    # create speaker 'stimulus_auditory_practice'
    deviceManager.addDevice(
        deviceName='stimulus_auditory_practice',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('response_visual_practice') is None:
        # initialise response_visual_practice
        response_visual_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_visual_practice',
        )
    if deviceManager.getDevice('response_auditory_practice') is None:
        # initialise response_auditory_practice
        response_auditory_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_auditory_practice',
        )
    if deviceManager.getDevice('go2_practice') is None:
        # initialise go2_practice
        go2_practice = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go2_practice',
        )
    if deviceManager.getDevice('go') is None:
        # initialise go
        go = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go',
        )
    # create speaker 'stimulus_auditory'
    deviceManager.addDevice(
        deviceName='stimulus_auditory',
        deviceClass='psychopy.hardware.speaker.SpeakerDevice',
        index=-1
    )
    if deviceManager.getDevice('response_visual') is None:
        # initialise response_visual
        response_visual = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_visual',
        )
    if deviceManager.getDevice('response_auditory') is None:
        # initialise response_auditory
        response_auditory = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='response_auditory',
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
    import pandas as pd
    import psychopy.logging as logging
    
    # Set logging level to WARNING to suppress INFO and DEBUG messages
    logging.console.setLevel(logging.WARNING)
    
    # Load the scenario CSV file
    scenario_df = pd.read_csv('DualNback_scenario.csv')
    
    # Filter the practice trials
    practice_indices = scenario_df.index[scenario_df['block'] == 'practice'].tolist()
    # Convert indices to PsychoPy's format (string of ranges)
    selected_rows_practice = f"{practice_indices[0]}:{practice_indices[-1]+1}" if practice_indices else ""
    
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
            'name_task' : 'DUAL N-BACK',
            'Text_instructions': ("Welcome to the dual n-back task.\n\n"
                                  "In this task, you will be required to perform both two tasks simultaneously.\n"
                                  "In a visual task, you will see squares appearing in different positions on the screen.\n"
                                  "in a auditory task, you will hear a sequence of letters.\n"
                                  "Your goal is to identify when the current visual or auditory stimulus matches one from a specified number of trials ago (n-back).\n\n"
                                  "We will start with some practice sessions to help you get familiar with the task.\n\n"
                                  "Press the space bar to continue."),
            
            'Practice_Visual': ("Let's begin with the visual part of the task (sequence of squares).\n\n"
                                "In this part, you will see a sequence of squares appearing in different positions on the screen.\n\n"
                                "Your goal is to press the 'k' key if the current square position matches the position from n trials ago (visual task).\n"
                                "In this first practice, we will focus on a 1-back condition, so press 'k' when the square is in the same position as in the previous trial.\n\n"
                                "Press the space bar to begin the practice session."),
    
            'Practice_Auditory': ("Now, let's focus on the auditory part of the task (sequence of letters).\n\n"
                                  "In this part, you will hear a sequence of letters.\n\n"
                                  "Your goal is to press the 'd' key if the current letter matches the letter from n trials ago (auditory task).\n"
                                  "In this practice, we will focus on a 1-back condition, so press 'd' when the letter is the same as in the previous trial.\n\n"
                                  "Press the space bar to begin the practice session."),
    
            'Practice_Both_1back': ("Now, let's combine both tasks (1-back).\n\n"
                                    "In this practice session, you will perform both the visual and auditory tasks simultaneously.\n\n"
                                    "Remember to press 'd' when the letter is the same as in the previous trial, and press 'k' when the square is in the same position as in the previous trial.\n\n"
                                    "Press the space bar to begin the practice session."),
    
            'Practice_Both_2back': ("Finally, let's combine both tasks in a 2-back condition.\n\n"
                                    "In this last practice session, you will perform both the visual and auditory tasks simultaneously, but in a 2-back condition.\n\n"
                                    "Remember to press 'd' when the letter matches the letter from 2 trials ago, and press 'k' when the square is in the same position as 2 trials ago.\n\n"
                                    "Press the space bar to begin the practice session."),
    
            'Text_start_task': ("The practice is over. Now we shall begin the real task.\nThis will consist of 6 blocks of either 1-back, 2-back or 3-back.\n"
                                "Ready?\n\n"
                                "Press the space bar to begin."),
            'Text_block' : "type : ",
            'Text_pause_between_blocks': ("Pause\n\n"
                                          "Press the space bar when you are ready to continue."),
            'Text_end_task': ("This task is now over.\n\nThank you!\n\nPress the space bar to continue")
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task' : 'DUAL N-BACK',
            'Text_instructions': ("Bienvenue dans la tâche de double n-back.\n\n"
                                  "Dans cette tâche, vous devrez effectuer simultanément des tâches visuelles et auditives. "
                                  "Dans la tâche visuelle, vous verrez des carrés apparaissant à différentes positions sur l'écran.\n"
                                  "Dans la tâche auditive, vous entendrez une séquence de lettres.\n"
                                  "Votre objectif est d'identifier si chaque stimulus actuel correspond à celui d'il y a un certain nombre d'essais (n-back).\n\n"
                                  "Commençons par quelques sessions d'entraînement pour vous familiariser avec la tâche.\n\n"
                                  "Appuyez sur la barre d'espace pour continuer."),
            
            'Practice_Visual': ("Commençons par la partie visuelle de la tâche (séquence de carrés).\n\n"
                                "Dans cette partie, vous verrez une séquence de carrés apparaissant à différentes positions sur l'écran.\n\n"
                                "Votre objectif est d'appuyer sur la touche 'k' si la position actuelle du carré correspond à la position d'il y a n essais (tâche visuelle).\n"
                                "Dans cette première pratique, nous nous concentrerons sur une condition 1-back, donc appuyez sur 'k' lorsque le carré est à la même position que lors de l'essai précédent.\n\n"
                                "Appuyez sur la barre d'espace pour commencer la session d'entraînement."),
    
            'Practice_Auditory': ("Passons maintenant à la partie auditive de la tâche (séquence de lettres).\n\n"
                                  "Dans cette partie, vous entendrez une séquence de lettres.\n\n"
                                  "Votre objectif est d'appuyer sur la touche 'd' si la lettre actuelle correspond à la lettre d'il y a n essais (tâche auditive).\n"
                                  "Dans cette pratique, nous nous concentrerons sur une condition 1-back, donc appuyez sur 'd' lorsque la lettre est la même que lors de l'essai précédent.\n\n"
                                  "Appuyez sur la barre d'espace pour commencer la session d'entraînement."),
    
            'Practice_Both_1back': ("Passons maintenant à la combinaison des deux tâches (1-back).\n\n"
                                    "Dans cette session d'entraînement, vous effectuerez simultanément les tâches visuelle et auditive.\n\n"
                                    "N'oubliez pas d'appuyer sur 'd' lorsque la lettre est la même que lors de l'essai précédent, et appuyez sur 'k' lorsque le carré est à la même position que lors de l'essai précédent.\n\n"
                                    "Appuyez sur la barre d'espace pour commencer la session d'entraînement."),
    
            'Practice_Both_2back': ("Enfin, combinons les deux tâches en condition 2-back.\n\n"
                                    "Dans cette dernière session d'entraînement, vous effectuerez simultanément les tâches visuelle et auditive, mais en condition 2-back.\n\n"
                                    "N'oubliez pas d'appuyer sur 'd' lorsque la lettre correspond à la lettre d'il y a 2 essais, et appuyez sur 'k' lorsque le carré est à la même position qu'il y a 2 essais.\n\n"
                                    "Appuyez sur la barre d'espace pour commencer la session d'entraînement."),
    
            'Text_start_task': ("L'entraînement est terminé. Nous allons maintenant commencer la vraie tâche.\nCette dernière sera constituée de 6 blocs de 1-back, 2-back ou 3-back"
                                "Prêt·e ?\n\n"
                                "Appuyez sur la barre d'espace pour commencer."),
            'Text_block' : "type : ",
            'Text_pause_between_blocks': ("Pause\n\n"
                                          "Appuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer."),
            'Text_end_task': ("Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer")
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
    startInst_practice = keyboard.Keyboard(deviceName='startInst_practice')
    text_instructions = visual.TextStim(win=win, name='text_instructions',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.6, ori=0, 
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
    
    # --- Initialize components for Routine "block_counter_practice" ---
    # Run 'Begin Experiment' code from LSL_start_practiceblock
    send_marker("start_practice_block")
    
    # --- Initialize components for Routine "instructions_practice" ---
    text_practice = visual.TextStim(win=win, name='text_practice',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.6, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    startInst = keyboard.Keyboard(deviceName='startInst')
    # Run 'Begin Experiment' code from define_block_rows_practice
    # Initialize block variables
    block_index = 0  # Start with the first block for test
    is_practice = True
    
    # --- Initialize components for Routine "main_practice" ---
    grid_practice = visual.ImageStim(
        win=win,
        name='grid_practice', units='height', 
        image='ressources/grid.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.6, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    stimulus_visual_practice = visual.Rect(
        win=win, name='stimulus_visual_practice',
        width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    stimulus_auditory_practice = sound.Sound(
        'A', 
        secs=1.5, 
        stereo=True, 
        hamming=True, 
        speaker='stimulus_auditory_practice',    name='stimulus_auditory_practice'
    )
    stimulus_auditory_practice.setVolume(1.0)
    response_visual_practice = keyboard.Keyboard(deviceName='response_visual_practice')
    response_auditory_practice = keyboard.Keyboard(deviceName='response_auditory_practice')
    feedback_auditory = visual.ImageStim(
        win=win,
        name='feedback_auditory', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(-0.5, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-8.0)
    feedback_visual = visual.ImageStim(
        win=win,
        name='feedback_visual', 
        image=None, mask=None, anchor='center',
        ori=0.0, pos=(0.5, 0), size=(0.3, 0.3),
        color=[1,1,1], colorSpace='rgb', opacity=None,
        flipHoriz=False, flipVert=False,
        texRes=128.0, interpolate=True, depth=-9.0)
    # Run 'Begin Experiment' code from code_feedback
    feedback_duration = 0.5  # duration of feedback display
    show_feedback = False  # initialize feedback visibility
    
    
    # --- Initialize components for Routine "pause_practice" ---
    InstructionsText3_practice = visual.TextStim(win=win, name='InstructionsText3_practice',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    go2_practice = keyboard.Keyboard(deviceName='go2_practice')
    # Run 'Begin Experiment' code from check_block_counter_practice
    # Check if the block is test and block_n is to skip the loop
    if is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
        practiceblocks.finished = True  # Skip the loop
    
    # --- Initialize components for Routine "startTask" ---
    InstructionsText2 = visual.TextStim(win=win, name='InstructionsText2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go = keyboard.Keyboard(deviceName='go')
    # Run 'Begin Experiment' code from define_block_rows
    is_test = True
    
    # --- Initialize components for Routine "block_counter" ---
    # Run 'Begin Experiment' code from LSL_start_testblock
    send_marker("start_block")
    textblock = visual.TextStim(win=win, name='textblock',
        text='',
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    wait = visual.TextStim(win=win, name='wait',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "main" ---
    grid = visual.ImageStim(
        win=win,
        name='grid', units='height', 
        image='ressources/grid.png', mask=None, anchor='center',
        ori=0, pos=(0, 0), size=(0.6, 0.6),
        color=[1,1,1], colorSpace='rgb', opacity=1,
        flipHoriz=False, flipVert=False,
        texRes=128, interpolate=True, depth=0.0)
    stimulus_visual = visual.Rect(
        win=win, name='stimulus_visual',
        width=(0.2, 0.2)[0], height=(0.2, 0.2)[1],
        ori=0.0, pos=(0, 0), anchor='center',
        lineWidth=1.0,     colorSpace='rgb',  lineColor='white', fillColor='white',
        opacity=None, depth=-1.0, interpolate=True)
    stimulus_auditory = sound.Sound(
        'A', 
        secs=1.5, 
        stereo=True, 
        hamming=True, 
        speaker='stimulus_auditory',    name='stimulus_auditory'
    )
    stimulus_auditory.setVolume(1.0)
    response_visual = keyboard.Keyboard(deviceName='response_visual')
    response_auditory = keyboard.Keyboard(deviceName='response_auditory')
    
    # --- Initialize components for Routine "pause" ---
    InstructionsText3 = visual.TextStim(win=win, name='InstructionsText3',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    go2 = keyboard.Keyboard(deviceName='go2')
    # Run 'Begin Experiment' code from check_block_counter
    # Check if the block is test and block_n is to skip the loop
    if is_test and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique()):
        testblocks.finished = True  # Skip the loop
    
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
    startInst_practice.keys = []
    startInst_practice.rt = []
    _startInst_practice_allKeys = []
    text_instructions.setText('')
    # Run 'Begin Routine' code from code_text_instructions
    text_instructions.text = instructions['Text_instructions']
    
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions1Components = [startInst_practice, text_instructions, nametask]
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
        
        # *startInst_practice* updates
        waitOnFlip = False
        
        # if startInst_practice is starting this frame...
        if startInst_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            startInst_practice.frameNStart = frameN  # exact frame index
            startInst_practice.tStart = t  # local t and not account for scr refresh
            startInst_practice.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(startInst_practice, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'startInst_practice.started')
            # update status
            startInst_practice.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(startInst_practice.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(startInst_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if startInst_practice.status == STARTED and not waitOnFlip:
            theseKeys = startInst_practice.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _startInst_practice_allKeys.extend(theseKeys)
            if len(_startInst_practice_allKeys):
                startInst_practice.keys = _startInst_practice_allKeys[-1].name  # just the last key pressed
                startInst_practice.rt = _startInst_practice_allKeys[-1].rt
                startInst_practice.duration = _startInst_practice_allKeys[-1].duration
                # a response ends the routine
                continueRoutine = False
        
        # *text_instructions* updates
        
        # if text_instructions is starting this frame...
        if text_instructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_instructions.frameNStart = frameN  # exact frame index
            text_instructions.tStart = t  # local t and not account for scr refresh
            text_instructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_instructions, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'text_instructions.started')
            # update status
            text_instructions.status = STARTED
            text_instructions.setAutoDraw(True)
        
        # if text_instructions is active this frame...
        if text_instructions.status == STARTED:
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
    thisExp.nextEntry()
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('DualNback_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        # the Routine "block_counter_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "instructions_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructions_practice.started', globalClock.getTime(format='float'))
        text_practice.setText('')
        startInst.keys = []
        startInst.rt = []
        _startInst_allKeys = []
        # Run 'Begin Routine' code from code_InstructionsText1
        # Extract block_type for the current block
        current_practice_block = scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)]['block_n'].values[0]
        
        # Set the instruction text based on the block type
        if current_practice_block == 1:
            text_practice.text = instructions['Practice_Visual']
        elif current_practice_block == 2:
            text_practice.text = instructions['Practice_Auditory']
        elif current_practice_block == 3:
            text_practice.text = instructions['Practice_Both_1back']
        elif current_practice_block == 4:
            text_practice.text = instructions['Practice_Both_2back']
        # Run 'Begin Routine' code from LSL_DualNback_start
        send_marker('DualNback_start')
        # Run 'Begin Routine' code from define_block_rows_practice
        # Set the stimuli based on the block type
        if current_practice_block == 1: #Practice_Visual
            play_auditory = False
            play_visual = True
        elif current_practice_block == 2: # Practice_Auditory
            play_auditory = True
            play_visual = False
        elif current_practice_block == 3: # Practice_Both_1back
            play_auditory = True
            play_visual = True
        elif current_practice_block == 4: # Practice_Both_2back
            play_auditory = True
            play_visual = True
        
        # keep track of which components have finished
        instructions_practiceComponents = [text_practice, startInst]
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
        # the Routine "instructions_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practiceTrials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('DualNback_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "main_practice" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('main_practice.started', globalClock.getTime(format='float'))
            stimulus_auditory_practice.setSound(auditory_path, secs=1.5, hamming=True)
            stimulus_auditory_practice.setVolume(1.0, log=False)
            stimulus_auditory_practice.seek(0)
            response_visual_practice.keys = []
            response_visual_practice.rt = []
            _response_visual_practice_allKeys = []
            response_auditory_practice.keys = []
            response_auditory_practice.rt = []
            _response_auditory_practice_allKeys = []
            # Run 'Begin Routine' code from code_stimulus_visual_practice
            # Dictionary mapping square_position to coordinates
            position_dict = {
                'pos_1': (-0.2, 0.2),
                'pos_2': (0, 0.2),
                'pos_3': (0.2, 0.2),
                'pos_4': (-0.2, 0),
                'pos_5': (0, 0),
                'pos_6': (0.2, 0),
                'pos_7': (-0.2, -0.2),
                'pos_8': (0, -0.2),
                'pos_9': (0.2, -0.2)
            }
            
            # Get the current position from the trial handler
            current_position = square_position
            
            # Set the position of the stimulus_visual polygon
            stimulus_visual_practice.pos = position_dict[current_position]
            
            # Run 'Begin Routine' code from LSL_stimulus_practice
            send_marker("practice_stimulus_" + auditory_path + "_" + square_position)
            # Run 'Begin Routine' code from code_feedback
            show_feedback = False  # Reset feedback visibility at the start of each trial
            
            # keep track of which components have finished
            main_practiceComponents = [grid_practice, stimulus_visual_practice, stimulus_auditory_practice, response_visual_practice, response_auditory_practice, feedback_auditory, feedback_visual]
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
                # is it time to end the Routine? (based on local clock)
                if tThisFlip > 3-frameTolerance:
                    continueRoutine = False
                
                # *grid_practice* updates
                
                # if grid_practice is starting this frame...
                if grid_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    grid_practice.frameNStart = frameN  # exact frame index
                    grid_practice.tStart = t  # local t and not account for scr refresh
                    grid_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(grid_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grid_practice.started')
                    # update status
                    grid_practice.status = STARTED
                    grid_practice.setAutoDraw(True)
                
                # if grid_practice is active this frame...
                if grid_practice.status == STARTED:
                    # update params
                    pass
                
                # if grid_practice is stopping this frame...
                if grid_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > grid_practice.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        grid_practice.tStop = t  # not accounting for scr refresh
                        grid_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        grid_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'grid_practice.stopped')
                        # update status
                        grid_practice.status = FINISHED
                        grid_practice.setAutoDraw(False)
                
                # *stimulus_visual_practice* updates
                
                # if stimulus_visual_practice is starting this frame...
                if stimulus_visual_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus_visual_practice.frameNStart = frameN  # exact frame index
                    stimulus_visual_practice.tStart = t  # local t and not account for scr refresh
                    stimulus_visual_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus_visual_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus_visual_practice.started')
                    # update status
                    stimulus_visual_practice.status = STARTED
                    stimulus_visual_practice.setAutoDraw(True)
                
                # if stimulus_visual_practice is active this frame...
                if stimulus_visual_practice.status == STARTED:
                    # update params
                    pass
                
                # if stimulus_visual_practice is stopping this frame...
                if stimulus_visual_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimulus_visual_practice.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimulus_visual_practice.tStop = t  # not accounting for scr refresh
                        stimulus_visual_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        stimulus_visual_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulus_visual_practice.stopped')
                        # update status
                        stimulus_visual_practice.status = FINISHED
                        stimulus_visual_practice.setAutoDraw(False)
                
                # if stimulus_auditory_practice is starting this frame...
                if stimulus_auditory_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus_auditory_practice.frameNStart = frameN  # exact frame index
                    stimulus_auditory_practice.tStart = t  # local t and not account for scr refresh
                    stimulus_auditory_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('stimulus_auditory_practice.started', tThisFlipGlobal)
                    # update status
                    stimulus_auditory_practice.status = STARTED
                    stimulus_auditory_practice.play(when=win)  # sync with win flip
                
                # if stimulus_auditory_practice is stopping this frame...
                if stimulus_auditory_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimulus_auditory_practice.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimulus_auditory_practice.tStop = t  # not accounting for scr refresh
                        stimulus_auditory_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        stimulus_auditory_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulus_auditory_practice.stopped')
                        # update status
                        stimulus_auditory_practice.status = FINISHED
                        stimulus_auditory_practice.stop()
                # update stimulus_auditory_practice status according to whether it's playing
                if stimulus_auditory_practice.isPlaying:
                    stimulus_auditory_practice.status = STARTED
                elif stimulus_auditory_practice.isFinished:
                    stimulus_auditory_practice.status = FINISHED
                
                # *response_visual_practice* updates
                waitOnFlip = False
                
                # if response_visual_practice is starting this frame...
                if response_visual_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    response_visual_practice.frameNStart = frameN  # exact frame index
                    response_visual_practice.tStart = t  # local t and not account for scr refresh
                    response_visual_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_visual_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_visual_practice.started')
                    # update status
                    response_visual_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_visual_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_visual_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response_visual_practice is stopping this frame...
                if response_visual_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_visual_practice.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        response_visual_practice.tStop = t  # not accounting for scr refresh
                        response_visual_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        response_visual_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_visual_practice.stopped')
                        # update status
                        response_visual_practice.status = FINISHED
                        response_visual_practice.status = FINISHED
                if response_visual_practice.status == STARTED and not waitOnFlip:
                    theseKeys = response_visual_practice.getKeys(keyList=['k'], ignoreKeys=None, waitRelease=False)
                    _response_visual_practice_allKeys.extend(theseKeys)
                    if len(_response_visual_practice_allKeys):
                        response_visual_practice.keys = _response_visual_practice_allKeys[0].name  # just the first key pressed
                        response_visual_practice.rt = _response_visual_practice_allKeys[0].rt
                        response_visual_practice.duration = _response_visual_practice_allKeys[0].duration
                        # was this correct?
                        if (response_visual_practice.keys == str(visual_correct)) or (response_visual_practice.keys == visual_correct):
                            response_visual_practice.corr = 1
                        else:
                            response_visual_practice.corr = 0
                
                # *response_auditory_practice* updates
                waitOnFlip = False
                
                # if response_auditory_practice is starting this frame...
                if response_auditory_practice.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    response_auditory_practice.frameNStart = frameN  # exact frame index
                    response_auditory_practice.tStart = t  # local t and not account for scr refresh
                    response_auditory_practice.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_auditory_practice, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_auditory_practice.started')
                    # update status
                    response_auditory_practice.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_auditory_practice.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_auditory_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response_auditory_practice is stopping this frame...
                if response_auditory_practice.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_auditory_practice.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        response_auditory_practice.tStop = t  # not accounting for scr refresh
                        response_auditory_practice.tStopRefresh = tThisFlipGlobal  # on global time
                        response_auditory_practice.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_auditory_practice.stopped')
                        # update status
                        response_auditory_practice.status = FINISHED
                        response_auditory_practice.status = FINISHED
                if response_auditory_practice.status == STARTED and not waitOnFlip:
                    theseKeys = response_auditory_practice.getKeys(keyList=['d'], ignoreKeys=None, waitRelease=False)
                    _response_auditory_practice_allKeys.extend(theseKeys)
                    if len(_response_auditory_practice_allKeys):
                        response_auditory_practice.keys = _response_auditory_practice_allKeys[0].name  # just the first key pressed
                        response_auditory_practice.rt = _response_auditory_practice_allKeys[0].rt
                        response_auditory_practice.duration = _response_auditory_practice_allKeys[0].duration
                        # was this correct?
                        if (response_auditory_practice.keys == str(auditory_correct)) or (response_auditory_practice.keys == auditory_correct):
                            response_auditory_practice.corr = 1
                        else:
                            response_auditory_practice.corr = 0
                # Run 'Each Frame' code from code_stimulus
                if play_visual == False:
                    stimulus_visual_practice.setAutoDraw(False)  # Disable the visual stimulus
                if play_auditory == False:
                    stimulus_auditory_practice.stop()  # Stop the auditory stimulus
                
                
                
                # *feedback_auditory* updates
                
                # if feedback_auditory is starting this frame...
                if feedback_auditory.status == NOT_STARTED and False:
                    # keep track of start time/frame for later
                    feedback_auditory.frameNStart = frameN  # exact frame index
                    feedback_auditory.tStart = t  # local t and not account for scr refresh
                    feedback_auditory.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_auditory, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_auditory.started')
                    # update status
                    feedback_auditory.status = STARTED
                    feedback_auditory.setAutoDraw(True)
                
                # if feedback_auditory is active this frame...
                if feedback_auditory.status == STARTED:
                    # update params
                    pass
                
                # *feedback_visual* updates
                
                # if feedback_visual is starting this frame...
                if feedback_visual.status == NOT_STARTED and False:
                    # keep track of start time/frame for later
                    feedback_visual.frameNStart = frameN  # exact frame index
                    feedback_visual.tStart = t  # local t and not account for scr refresh
                    feedback_visual.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(feedback_visual, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'feedback_visual.started')
                    # update status
                    feedback_visual.status = STARTED
                    feedback_visual.setAutoDraw(True)
                
                # if feedback_visual is active this frame...
                if feedback_visual.status == STARTED:
                    # update params
                    pass
                # Run 'Each Frame' code from code_feedback
                if response_visual_practice.keys:  # Check if a key was pressed for visual response
                    if play_visual:  # Only proceed if visual feedback is needed
                        if response_visual_practice.corr:  # If correct response
                            feedback_visual.setImage('ressources/correct.png')
                        else:  # If incorrect response
                            feedback_visual.setImage('ressources/incorrect.png')
                        show_feedback = True  # Set flag to show visual feedback
                        feedback_start_time = t  # Record the time when feedback starts
                        feedback_visual.setAutoDraw(True)  # Start drawing visual feedback
                
                if response_auditory_practice.keys:  # Check if a key was pressed for auditory response
                    if play_auditory:  # Only proceed if auditory feedback is needed
                        if response_auditory_practice.corr:  # If correct response
                            feedback_auditory.setImage('ressources/correct.png')
                        else:  # If incorrect response
                            feedback_auditory.setImage('ressources/incorrect.png')
                        show_feedback = True  # Set flag to show auditory feedback
                        feedback_start_time = t  # Record the time when feedback starts
                        feedback_auditory.setAutoDraw(True)  # Start drawing auditory feedback
                
                if show_feedback:  # If feedback is shown, control timing
                    if t >= feedback_start_time + feedback_duration:  # Stop showing feedback after 0.5 seconds
                        feedback_visual.setAutoDraw(False)
                        feedback_auditory.setAutoDraw(False)
                        show_feedback = False  # Reset feedback flag
                        continueRoutine = False  # End the routine once feedback is displayed
                
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
            stimulus_auditory_practice.pause()  # ensure sound has stopped at end of Routine
            # check responses
            if response_visual_practice.keys in ['', [], None]:  # No response was made
                response_visual_practice.keys = None
                # was no response the correct answer?!
                if str(visual_correct).lower() == 'none':
                   response_visual_practice.corr = 1;  # correct non-response
                else:
                   response_visual_practice.corr = 0;  # failed to respond (incorrectly)
            # store data for practiceTrials (TrialHandler)
            practiceTrials.addData('response_visual_practice.keys',response_visual_practice.keys)
            practiceTrials.addData('response_visual_practice.corr', response_visual_practice.corr)
            if response_visual_practice.keys != None:  # we had a response
                practiceTrials.addData('response_visual_practice.rt', response_visual_practice.rt)
                practiceTrials.addData('response_visual_practice.duration', response_visual_practice.duration)
            # check responses
            if response_auditory_practice.keys in ['', [], None]:  # No response was made
                response_auditory_practice.keys = None
                # was no response the correct answer?!
                if str(auditory_correct).lower() == 'none':
                   response_auditory_practice.corr = 1;  # correct non-response
                else:
                   response_auditory_practice.corr = 0;  # failed to respond (incorrectly)
            # store data for practiceTrials (TrialHandler)
            practiceTrials.addData('response_auditory_practice.keys',response_auditory_practice.keys)
            practiceTrials.addData('response_auditory_practice.corr', response_auditory_practice.corr)
            if response_auditory_practice.keys != None:  # we had a response
                practiceTrials.addData('response_auditory_practice.rt', response_auditory_practice.rt)
                practiceTrials.addData('response_auditory_practice.duration', response_auditory_practice.duration)
            # Run 'End Routine' code from LSL_stimulus_practice
            answer_corr_auditory = f"response_auditory_{response_auditory.corr}"
            answer_corr_visual = f"response_visual_{response_visual.corr}"
            send_marker(answer_corr_auditory)  # Function to send the LSL marker
            send_marker(answer_corr_visual)  # Function to send the LSL marker
            
            
            # Run 'End Routine' code from code_feedback
            # Clear feedback visuals
            feedback_visual.setAutoDraw(False)
            feedback_auditory.setAutoDraw(False)
            
            # the Routine "main_practice" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'practiceTrials'
        
        
        # --- Prepare to start Routine "pause_practice" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('pause_practice.started', globalClock.getTime(format='float'))
        InstructionsText3_practice.setText('')
        go2_practice.keys = []
        go2_practice.rt = []
        _go2_practice_allKeys = []
        # Run 'Begin Routine' code from code_InstructionsText3_practice
        # Set the text for the third set of instructions
        InstructionsText3_practice.setText(instructions['Text_pause_between_blocks'])
        
        # keep track of which components have finished
        pause_practiceComponents = [InstructionsText3_practice, go2_practice]
        for thisComponent in pause_practiceComponents:
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
        
        # --- Run Routine "pause_practice" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *InstructionsText3_practice* updates
            
            # if InstructionsText3_practice is starting this frame...
            if InstructionsText3_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                InstructionsText3_practice.frameNStart = frameN  # exact frame index
                InstructionsText3_practice.tStart = t  # local t and not account for scr refresh
                InstructionsText3_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(InstructionsText3_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'InstructionsText3_practice.started')
                # update status
                InstructionsText3_practice.status = STARTED
                InstructionsText3_practice.setAutoDraw(True)
            
            # if InstructionsText3_practice is active this frame...
            if InstructionsText3_practice.status == STARTED:
                # update params
                pass
            
            # *go2_practice* updates
            waitOnFlip = False
            
            # if go2_practice is starting this frame...
            if go2_practice.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                go2_practice.frameNStart = frameN  # exact frame index
                go2_practice.tStart = t  # local t and not account for scr refresh
                go2_practice.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(go2_practice, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'go2_practice.started')
                # update status
                go2_practice.status = STARTED
                # keyboard checking is just starting
                waitOnFlip = True
                win.callOnFlip(go2_practice.clock.reset)  # t=0 on next screen flip
                win.callOnFlip(go2_practice.clearEvents, eventType='keyboard')  # clear events on next screen flip
            if go2_practice.status == STARTED and not waitOnFlip:
                theseKeys = go2_practice.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _go2_practice_allKeys.extend(theseKeys)
                if len(_go2_practice_allKeys):
                    go2_practice.keys = _go2_practice_allKeys[-1].name  # just the last key pressed
                    go2_practice.rt = _go2_practice_allKeys[-1].rt
                    go2_practice.duration = _go2_practice_allKeys[-1].duration
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
            for thisComponent in pause_practiceComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "pause_practice" ---
        for thisComponent in pause_practiceComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('pause_practice.stopped', globalClock.getTime(format='float'))
        # check responses
        if go2_practice.keys in ['', [], None]:  # No response was made
            go2_practice.keys = None
        practiceblocks.addData('go2_practice.keys',go2_practice.keys)
        if go2_practice.keys != None:  # we had a response
            practiceblocks.addData('go2_practice.rt', go2_practice.rt)
            practiceblocks.addData('go2_practice.duration', go2_practice.duration)
        # the Routine "pause_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1.0 repeats of 'practiceblocks'
    
    
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
        trialList=data.importConditions('DualNback_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            block_type = scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_n)]['block_type'].iloc[0]
        
        
        textblock.setText(block_type)
        # keep track of which components have finished
        block_counterComponents = [textblock, wait]
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
        while continueRoutine and routineTimer.getTime() < 2.0:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            
            # *textblock* updates
            
            # if textblock is starting this frame...
            if textblock.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textblock.frameNStart = frameN  # exact frame index
                textblock.tStart = t  # local t and not account for scr refresh
                textblock.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textblock, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textblock.started')
                # update status
                textblock.status = STARTED
                textblock.setAutoDraw(True)
            
            # if textblock is active this frame...
            if textblock.status == STARTED:
                # update params
                pass
            
            # if textblock is stopping this frame...
            if textblock.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > textblock.tStartRefresh + 1.5-frameTolerance:
                    # keep track of stop time/frame for later
                    textblock.tStop = t  # not accounting for scr refresh
                    textblock.tStopRefresh = tThisFlipGlobal  # on global time
                    textblock.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'textblock.stopped')
                    # update status
                    textblock.status = FINISHED
                    textblock.setAutoDraw(False)
            
            # *wait* updates
            
            # if wait is starting this frame...
            if wait.status == NOT_STARTED and tThisFlip >= 1.5-frameTolerance:
                # keep track of start time/frame for later
                wait.frameNStart = frameN  # exact frame index
                wait.tStart = t  # local t and not account for scr refresh
                wait.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(wait, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'wait.started')
                # update status
                wait.status = STARTED
                wait.setAutoDraw(True)
            
            # if wait is active this frame...
            if wait.status == STARTED:
                # update params
                pass
            
            # if wait is stopping this frame...
            if wait.status == STARTED:
                # is it time to stop? (based on global clock, using actual start)
                if tThisFlipGlobal > wait.tStartRefresh + 0.5-frameTolerance:
                    # keep track of stop time/frame for later
                    wait.tStop = t  # not accounting for scr refresh
                    wait.tStopRefresh = tThisFlipGlobal  # on global time
                    wait.frameNStop = frameN  # exact frame index
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'wait.stopped')
                    # update status
                    wait.status = FINISHED
                    wait.setAutoDraw(False)
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
        # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
        if routineForceEnded:
            routineTimer.reset()
        else:
            routineTimer.addTime(-2.000000)
        
        # set up handler to look after randomisation of conditions etc
        testTrials = data.TrialHandler(nReps=1, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('DualNback_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "main" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('main.started', globalClock.getTime(format='float'))
            stimulus_auditory.setSound(auditory_path, secs=1.5, hamming=True)
            stimulus_auditory.setVolume(1.0, log=False)
            stimulus_auditory.seek(0)
            response_visual.keys = []
            response_visual.rt = []
            _response_visual_allKeys = []
            response_auditory.keys = []
            response_auditory.rt = []
            _response_auditory_allKeys = []
            # Run 'Begin Routine' code from code_stimulus_visual
            # Dictionary mapping square_position to coordinates
            position_dict = {
                'pos_1': (-0.2, 0.2),
                'pos_2': (0, 0.2),
                'pos_3': (0.2, 0.2),
                'pos_4': (-0.2, 0),
                'pos_5': (0, 0),
                'pos_6': (0.2, 0),
                'pos_7': (-0.2, -0.2),
                'pos_8': (0, -0.2),
                'pos_9': (0.2, -0.2)
            }
            
            # Get the current position from the trial handler
            current_position = square_position
            
            # Set the position of the stimulus_visual polygon
            stimulus_visual.pos = position_dict[current_position]
            
            # Run 'Begin Routine' code from LSL_stimulus
            send_marker("stimulus_" + auditory_path + "_" + square_position)
            marker_sent_visual = False
            marker_sent_auditory = False
            # Run 'Begin Routine' code from test
            print(block_type)
            print(block_n)
            # keep track of which components have finished
            mainComponents = [grid, stimulus_visual, stimulus_auditory, response_visual, response_auditory]
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
            while continueRoutine and routineTimer.getTime() < 3.0:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *grid* updates
                
                # if grid is starting this frame...
                if grid.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    grid.frameNStart = frameN  # exact frame index
                    grid.tStart = t  # local t and not account for scr refresh
                    grid.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(grid, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'grid.started')
                    # update status
                    grid.status = STARTED
                    grid.setAutoDraw(True)
                
                # if grid is active this frame...
                if grid.status == STARTED:
                    # update params
                    pass
                
                # if grid is stopping this frame...
                if grid.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > grid.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        grid.tStop = t  # not accounting for scr refresh
                        grid.tStopRefresh = tThisFlipGlobal  # on global time
                        grid.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'grid.stopped')
                        # update status
                        grid.status = FINISHED
                        grid.setAutoDraw(False)
                
                # *stimulus_visual* updates
                
                # if stimulus_visual is starting this frame...
                if stimulus_visual.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus_visual.frameNStart = frameN  # exact frame index
                    stimulus_visual.tStart = t  # local t and not account for scr refresh
                    stimulus_visual.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(stimulus_visual, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'stimulus_visual.started')
                    # update status
                    stimulus_visual.status = STARTED
                    stimulus_visual.setAutoDraw(True)
                
                # if stimulus_visual is active this frame...
                if stimulus_visual.status == STARTED:
                    # update params
                    pass
                
                # if stimulus_visual is stopping this frame...
                if stimulus_visual.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimulus_visual.tStartRefresh + 0.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimulus_visual.tStop = t  # not accounting for scr refresh
                        stimulus_visual.tStopRefresh = tThisFlipGlobal  # on global time
                        stimulus_visual.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulus_visual.stopped')
                        # update status
                        stimulus_visual.status = FINISHED
                        stimulus_visual.setAutoDraw(False)
                
                # if stimulus_auditory is starting this frame...
                if stimulus_auditory.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    stimulus_auditory.frameNStart = frameN  # exact frame index
                    stimulus_auditory.tStart = t  # local t and not account for scr refresh
                    stimulus_auditory.tStartRefresh = tThisFlipGlobal  # on global time
                    # add timestamp to datafile
                    thisExp.addData('stimulus_auditory.started', tThisFlipGlobal)
                    # update status
                    stimulus_auditory.status = STARTED
                    stimulus_auditory.play(when=win)  # sync with win flip
                
                # if stimulus_auditory is stopping this frame...
                if stimulus_auditory.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > stimulus_auditory.tStartRefresh + 1.5-frameTolerance:
                        # keep track of stop time/frame for later
                        stimulus_auditory.tStop = t  # not accounting for scr refresh
                        stimulus_auditory.tStopRefresh = tThisFlipGlobal  # on global time
                        stimulus_auditory.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'stimulus_auditory.stopped')
                        # update status
                        stimulus_auditory.status = FINISHED
                        stimulus_auditory.stop()
                # update stimulus_auditory status according to whether it's playing
                if stimulus_auditory.isPlaying:
                    stimulus_auditory.status = STARTED
                elif stimulus_auditory.isFinished:
                    stimulus_auditory.status = FINISHED
                
                # *response_visual* updates
                waitOnFlip = False
                
                # if response_visual is starting this frame...
                if response_visual.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    response_visual.frameNStart = frameN  # exact frame index
                    response_visual.tStart = t  # local t and not account for scr refresh
                    response_visual.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_visual, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_visual.started')
                    # update status
                    response_visual.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_visual.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_visual.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response_visual is stopping this frame...
                if response_visual.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_visual.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        response_visual.tStop = t  # not accounting for scr refresh
                        response_visual.tStopRefresh = tThisFlipGlobal  # on global time
                        response_visual.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_visual.stopped')
                        # update status
                        response_visual.status = FINISHED
                        response_visual.status = FINISHED
                if response_visual.status == STARTED and not waitOnFlip:
                    theseKeys = response_visual.getKeys(keyList=['k'], ignoreKeys=None, waitRelease=False)
                    _response_visual_allKeys.extend(theseKeys)
                    if len(_response_visual_allKeys):
                        response_visual.keys = _response_visual_allKeys[0].name  # just the first key pressed
                        response_visual.rt = _response_visual_allKeys[0].rt
                        response_visual.duration = _response_visual_allKeys[0].duration
                        # was this correct?
                        if (response_visual.keys == str(visual_correct)) or (response_visual.keys == visual_correct):
                            response_visual.corr = 1
                        else:
                            response_visual.corr = 0
                
                # *response_auditory* updates
                waitOnFlip = False
                
                # if response_auditory is starting this frame...
                if response_auditory.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                    # keep track of start time/frame for later
                    response_auditory.frameNStart = frameN  # exact frame index
                    response_auditory.tStart = t  # local t and not account for scr refresh
                    response_auditory.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(response_auditory, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'response_auditory.started')
                    # update status
                    response_auditory.status = STARTED
                    # keyboard checking is just starting
                    waitOnFlip = True
                    win.callOnFlip(response_auditory.clock.reset)  # t=0 on next screen flip
                    win.callOnFlip(response_auditory.clearEvents, eventType='keyboard')  # clear events on next screen flip
                
                # if response_auditory is stopping this frame...
                if response_auditory.status == STARTED:
                    # is it time to stop? (based on global clock, using actual start)
                    if tThisFlipGlobal > response_auditory.tStartRefresh + 3-frameTolerance:
                        # keep track of stop time/frame for later
                        response_auditory.tStop = t  # not accounting for scr refresh
                        response_auditory.tStopRefresh = tThisFlipGlobal  # on global time
                        response_auditory.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'response_auditory.stopped')
                        # update status
                        response_auditory.status = FINISHED
                        response_auditory.status = FINISHED
                if response_auditory.status == STARTED and not waitOnFlip:
                    theseKeys = response_auditory.getKeys(keyList=['d'], ignoreKeys=None, waitRelease=False)
                    _response_auditory_allKeys.extend(theseKeys)
                    if len(_response_auditory_allKeys):
                        response_auditory.keys = _response_auditory_allKeys[0].name  # just the first key pressed
                        response_auditory.rt = _response_auditory_allKeys[0].rt
                        response_auditory.duration = _response_auditory_allKeys[0].duration
                        # was this correct?
                        if (response_auditory.keys == str(auditory_correct)) or (response_auditory.keys == auditory_correct):
                            response_auditory.corr = 1
                        else:
                            response_auditory.corr = 0
                # Run 'Each Frame' code from LSL_stimulus
                if response_visual.keys and not marker_sent_visual:  # Check if a key was pressed for visual response and marker hasn't been sent
                    answer_corr_visual = f"response_visual_{response_visual.corr}"
                    send_marker(answer_corr_visual)  # Function to send the LSL marker
                    marker_sent_visual = True  # Set the flag to indicate that the marker has been sent
                
                if response_auditory.keys and not marker_sent_auditory:  # Check if a key was pressed for auditory response and marker hasn't been sent
                    answer_corr_auditory = f"response_auditory_{response_auditory.corr}"
                    send_marker(answer_corr_auditory)  # Function to send the LSL marker
                    marker_sent_auditory = True  # Set the flag to indicate that the marker has been sent
                
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
            stimulus_auditory.pause()  # ensure sound has stopped at end of Routine
            # check responses
            if response_visual.keys in ['', [], None]:  # No response was made
                response_visual.keys = None
                # was no response the correct answer?!
                if str(visual_correct).lower() == 'none':
                   response_visual.corr = 1;  # correct non-response
                else:
                   response_visual.corr = 0;  # failed to respond (incorrectly)
            # store data for testTrials (TrialHandler)
            testTrials.addData('response_visual.keys',response_visual.keys)
            testTrials.addData('response_visual.corr', response_visual.corr)
            if response_visual.keys != None:  # we had a response
                testTrials.addData('response_visual.rt', response_visual.rt)
                testTrials.addData('response_visual.duration', response_visual.duration)
            # check responses
            if response_auditory.keys in ['', [], None]:  # No response was made
                response_auditory.keys = None
                # was no response the correct answer?!
                if str(auditory_correct).lower() == 'none':
                   response_auditory.corr = 1;  # correct non-response
                else:
                   response_auditory.corr = 0;  # failed to respond (incorrectly)
            # store data for testTrials (TrialHandler)
            testTrials.addData('response_auditory.keys',response_auditory.keys)
            testTrials.addData('response_auditory.corr', response_auditory.corr)
            if response_auditory.keys != None:  # we had a response
                testTrials.addData('response_auditory.rt', response_auditory.rt)
                testTrials.addData('response_auditory.duration', response_auditory.duration)
            # Run 'End Routine' code from LSL_stimulus
            # Reset the flags after the key is released
            if not response_visual.keys:
                marker_sent_visual = False  # Reset the flag for the next key press
            
            if not response_auditory.keys:
                marker_sent_auditory = False  # Reset the flag for the next key press
            # using non-slip timing so subtract the expected duration of this Routine (unless ended on request)
            if routineForceEnded:
                routineTimer.reset()
            else:
                routineTimer.addTime(-3.000000)
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1 repeats of 'testTrials'
        
        
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
    # Run 'Begin Routine' code from LSL_DualNback_end
    send_marker('DualNback_end')
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
