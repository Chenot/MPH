#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on novembre 27, 2024, at 17:06
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

# --- Setup global variables (available in all functions) ---
# create a device manager to handle hardware (keyboards, mice, mirophones, speakers, etc.)
deviceManager = hardware.DeviceManager()
# ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
# store info about the experiment session
psychopyVersion = '2024.1.4'
expName = 'Vocabulary'  # from the Builder filename that created this script
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
        originPath='D:\\Google Drive\\Professionnel\\3_Post-doc_ISAE-MPH\\Experience_MPH\\project\\code\\PsychopyTasks\\Verbal_Vocabulary\\vocabulary_lastrun.py',
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
            winType='pyglet', allowStencil=True,
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
    if deviceManager.getDevice('go') is None:
        # initialise go
        go = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='go',
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
            'name_task' : 'VOCABULARY',
            'Text_instructions': (
                "Welcome to the Vocabulary Task.\n\n"
                "In this task, you will see a word on the screen.\n "
                "Your objective is to provide a SYNONYM or a DEFINITION of this word as accurately as possible. "
                "If you are unsure, provide your best guess. "
                "You will have 30 to 60 seconds to answer, depending on the word.\n\n"
                "For example: 'COLOSSAL'\n\n"
                "A synonym might be: 'gigantic'. A definition could be 'Having considerable dimensions, possessing enormous proportions.'\n\n"
                "Whenever you're ready, press the spacebar to start."
            ),
            'Text_trial': "Word ",
            'Text_end_task': (
                "This task is now over.\n\nThank you!\n\nPress the space bar to continue"
            ),
            'Placeholder1': "Type your synonym/definition here..."
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task' : 'VOCABULAIRE',
            'Text_instructions': (
                "Bienvenue dans la tâche de Vocabulaire.\n\n"
                "Dans cette tâche, vous verrez un mot à l'écran.\n"
                "Votre objectif est de fournir un SYNONYME ou une DÉFINITION de ce mot aussi précise que possible. "
                "Si vous n'êtes pas sûr, donnez votre meilleure supposition. "
                "Vous aurez entre 30 et 60 secondes pour répondre, en fonction du mot.\n\n"
                "Par exemple : 'COLOSSAL'\n\n"
                "Un synonyme pourrait être : 'gigantesque'. Une définition pourrait être 'qui a des dimensions considérables, qui a des proportions énormes.'\n\n"
                "Lorsque vous êtes prêt, appuyez sur la barre d'espace pour commencer."
            ),
            'Text_trial': "Mot ",
            'Text_end_task': (
                "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer"
            ),
            'Placeholder1': "Tapez votre synonyme/définition ici..."
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
    
    
    # --- Initialize components for Routine "Instruction1" ---
    TextInstructions = visual.TextStim(win=win, name='TextInstructions',
        text=None,
        font='Arial',
        pos=[0, 0], height=0.04, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    go = keyboard.Keyboard(deviceName='go')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "Trial" ---
    stimulus = visual.TextStim(win=win, name='stimulus',
        text=None,
        font='Arial',
        pos=[0, 0.1], height=0.1, wrapWidth=None, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    textbox_1 = visual.TextBox2(
         win, text=None, placeholder=None, font='Arial',
         pos=(0, -0.2),     letterHeight=0.05,
         size=(1, 0.30), borderWidth=2.0,
         color='black', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='top-left',
         anchor='center', overflow='visible',
         fillColor='white', borderColor='black',
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=True,
         name='textbox_1',
         depth=-2, autoLog=True,
    )
    button_next = visual.ButtonStim(win, 
        text='>', font='Arial',
        pos=(0.75, -0.4),
        letterHeight=0.05,
        size=(0.2, 0.1), borderWidth=0.0,
        fillColor='darkgrey', borderColor=None,
        color='white', colorSpace='rgb',
        opacity=None,
        bold=True, italic=False,
        padding=None,
        anchor='center',
        name='button_next',
        depth=-3
    )
    button_next.buttonClock = core.Clock()
    TextTrial = visual.TextStim(win=win, name='TextTrial',
        text=None,
        font='Arial',
        pos=(0, 0.4), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    # Run 'Begin Experiment' code from code_text_timer
    # Initialize the timer (in seconds)
    timer_task = 60
    text_timer = visual.TextStim(win=win, name='text_timer',
        text=None,
        font='Arial',
        pos=(0, -0.45), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-7.0);
    
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
        # Activate mouse
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
    
    # --- Prepare to start Routine "Instruction1" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('Instruction1.started', globalClock.getTime(format='float'))
    go.keys = []
    go.rt = []
    _go_allKeys = []
    # Run 'Begin Routine' code from code_instructions
    TextInstructions.setText(instructions['Text_instructions'])
    
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    Instruction1Components = [TextInstructions, go, nametask]
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
        
        # *TextInstructions* updates
        
        # if TextInstructions is starting this frame...
        if TextInstructions.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            TextInstructions.frameNStart = frameN  # exact frame index
            TextInstructions.tStart = t  # local t and not account for scr refresh
            TextInstructions.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(TextInstructions, 'tStartRefresh')  # time at next scr refresh
            # update status
            TextInstructions.status = STARTED
            TextInstructions.setAutoDraw(True)
        
        # if TextInstructions is active this frame...
        if TextInstructions.status == STARTED:
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
    # Run 'End Routine' code from LSL_start_test
    send_marker("Vocabulary_start")
    thisExp.nextEntry()
    # the Routine "Instruction1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    trials = data.TrialHandler(nReps=1, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('vocabulary.csv'),
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
        
        # --- Prepare to start Routine "Trial" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('Trial.started', globalClock.getTime(format='float'))
        stimulus.setText('')
        # Run 'Begin Routine' code from code_stimulus
        # Check if expInfo exists and create the language variable
        if 'expInfo' not in globals():
            expInfo = {}
        
        # Set default values to English if it is missing from expInfo keys
        if 'language' not in expInfo:
            expInfo['language'] = 'English'
        
        # Create the language variable
        language = expInfo.get('language')
        
        # Update the stimulus text based on the language
        if language == "English":
            stimulus.text = stim_eng
        elif language == "French":
            stimulus.text = stim_fr
        textbox_1.reset()
        textbox_1.setText('')
        textbox_1.setPlaceholder('')
        # reset button_next to account for continued clicks & clear times on/off
        button_next.reset()
        # Run 'Begin Routine' code from code_TextTrial
        # Set the text for the first set of instructions
        TextTrial.setText(instructions['Text_trial'] + str(trial) + "/24")
        
        # Set the placeholder text for the textboxes based on the selected language
        textbox_1.setText('')
        textbox_1.setPlaceholder(instructions['Placeholder1'])
        # Run 'Begin Routine' code from code_text_timer
        # Initialize the timer
        timer_task = time
        routine_timer = core.Clock()
        routine_timer.reset()
        
        # Run 'Begin Routine' code from LSL_start_trial
        marker = f"stimulus_{trial}"
        send_marker(marker)  # Function to send the LSL marker
        # keep track of which components have finished
        TrialComponents = [stimulus, textbox_1, button_next, TextTrial, text_timer]
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
            
            # *stimulus* updates
            
            # if stimulus is starting this frame...
            if stimulus.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                stimulus.frameNStart = frameN  # exact frame index
                stimulus.tStart = t  # local t and not account for scr refresh
                stimulus.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(stimulus, 'tStartRefresh')  # time at next scr refresh
                # update status
                stimulus.status = STARTED
                stimulus.setAutoDraw(True)
            
            # if stimulus is active this frame...
            if stimulus.status == STARTED:
                # update params
                pass
            
            # *textbox_1* updates
            
            # if textbox_1 is starting this frame...
            if textbox_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox_1.frameNStart = frameN  # exact frame index
                textbox_1.tStart = t  # local t and not account for scr refresh
                textbox_1.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox_1, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox_1.started')
                # update status
                textbox_1.status = STARTED
                textbox_1.setAutoDraw(True)
            
            # if textbox_1 is active this frame...
            if textbox_1.status == STARTED:
                # update params
                pass
            # *button_next* updates
            
            # if button_next is starting this frame...
            if button_next.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
                # keep track of start time/frame for later
                button_next.frameNStart = frameN  # exact frame index
                button_next.tStart = t  # local t and not account for scr refresh
                button_next.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(button_next, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'button_next.started')
                # update status
                button_next.status = STARTED
                button_next.setAutoDraw(True)
            
            # if button_next is active this frame...
            if button_next.status == STARTED:
                # update params
                pass
                # check whether button_next has been pressed
                if button_next.isClicked:
                    if not button_next.wasClicked:
                        # if this is a new click, store time of first click and clicked until
                        button_next.timesOn.append(button_next.buttonClock.getTime())
                        button_next.timesOff.append(button_next.buttonClock.getTime())
                    elif len(button_next.timesOff):
                        # if click is continuing from last frame, update time of clicked until
                        button_next.timesOff[-1] = button_next.buttonClock.getTime()
                    if not button_next.wasClicked:
                        # end routine when button_next is clicked
                        continueRoutine = False
                    if not button_next.wasClicked:
                        # run callback code when button_next is clicked
                        pass
            # take note of whether button_next was clicked, so that next frame we know if clicks are new
            button_next.wasClicked = button_next.isClicked and button_next.status == STARTED
            
            # *TextTrial* updates
            
            # if TextTrial is starting this frame...
            if TextTrial.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                TextTrial.frameNStart = frameN  # exact frame index
                TextTrial.tStart = t  # local t and not account for scr refresh
                TextTrial.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(TextTrial, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'TextTrial.started')
                # update status
                TextTrial.status = STARTED
                TextTrial.setAutoDraw(True)
            
            # if TextTrial is active this frame...
            if TextTrial.status == STARTED:
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
        trials.addData('textbox_1.text',textbox_1.text)
        trials.addData('button_next.numClicks', button_next.numClicks)
        if button_next.numClicks:
           trials.addData('button_next.timesOn', button_next.timesOn)
           trials.addData('button_next.timesOff', button_next.timesOff)
        else:
           trials.addData('button_next.timesOn', "")
           trials.addData('button_next.timesOff', "")
        # Run 'End Routine' code from save_data
        # Save the responses from the textboxes
        response1 = textbox_1.text
        
        # Also add them to the data file directly
        thisExp.addData('response1', response1)
        
        # Ensure the data is saved immediately
        thisExp.nextEntry()
        
        # the Routine "Trial" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
    # completed 1 repeats of 'trials'
    
    
    # --- Prepare to start Routine "end" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('end.started', globalClock.getTime(format='float'))
    # Run 'Begin Routine' code from code_InstructionsText4
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['Text_end_task'])
    
    # Run 'Begin Routine' code from LSL_Vocabulary_end
    send_marker('Vocabulary_end')
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
