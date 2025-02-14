#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2024.1.4),
    on novembre 27, 2024, at 17:03
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
expName = 'KeepTrack'  # from the Builder filename that created this script
# information about this experiment
expInfo = {
    'participant': f"{randint(0, 999999):06.0f}",
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
_loggingLevel = logging.getLevel('warning')
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
        originPath='D:\\Google Drive\\Professionnel\\3_Post-doc_ISAE-MPH\\Experience_MPH\\project\\code\\PsychopyTasks\\Updating_KeepTrack\\KeepTrack_lastrun.py',
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
    if deviceManager.getDevice('end_inst_1') is None:
        # initialise end_inst_1
        end_inst_1 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='end_inst_1',
        )
    if deviceManager.getDevice('end_inst_2') is None:
        # initialise end_inst_2
        end_inst_2 = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='end_inst_2',
        )
    if deviceManager.getDevice('key_resp') is None:
        # initialise key_resp
        key_resp = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='key_resp',
        )
    if deviceManager.getDevice('start_Task') is None:
        # initialise start_Task
        start_Task = deviceManager.addDevice(
            deviceClass='keyboard',
            deviceName='start_Task',
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
    
    # Load the CSV file
    scenario_df = pd.read_csv('keep_track_scenario.csv')
    
    # Select practice and test blocks
    practice_blocks = scenario_df[scenario_df['block'] == 'practice']['block_n'].unique().tolist()
    test_blocks = scenario_df[scenario_df['block'] == 'test']['block_n'].unique().tolist()
    # Run 'Begin Experiment' code from language
    # Check if expInfo exists and create the language variable
    if 'expInfo' not in globals():
        expInfo = {}
    
    # Set default values to English if it is missing from expInfo keys
    if 'language' not in expInfo:
        expInfo['language'] = 'French'
    
    # Create the language variable
    language = expInfo.get('language')
    
    # Define instructions based on the selected language
    if language == "English":
        instructions = {
            'name_task': 'KEEP-TRACK',
            'Introduction1': "Welcome to the Keep-Track task.\nIn this task, you will be presented with a sequence of 15 words, one at a time in the center of the screen.\n\nThe words will be selected from the following 6 categories:\n\n- Animals: bear, dog, horse, lion, rabbit, wolf\n- Colors: blue, green, white, purple, red, yellow\n- Countries: Australia, Brazil, China, Italy, India, Japan\n- Fruits: banana, strawberry, melon, pear, apple, apricot\n- Body: mouth, arm, elbow, foot, leg, hand\n- Family: mother, father, brother, sister, aunt, uncle\n\nTake a moment to familiarize yourself with the words.",
            'Introduction2': "Once the 15 words have been presented, you will be asked to recall the last word presented for the selected categories.\nYou will always be informed of the categories to pay attention to before each new round begins.\n\nExample: The categories to keep track of are 'Animals' and 'Family'.\n\nThe 15 words are presented one by one in the center of the screen. The last item presented for the 'Animals' category is 'bear'. Type 'bear' for 'Animals' when you are asked to enter your responses in the text boxes. Make sure the spelling of the word you enter is correct.\n\n!Important!\nIt is important that you memorize the words.\nDo not write down the words.\n\nYou can start the practice when you are ready.",
            'Start_Actual_Task': "Start of the Test\n\nThe training is over and the test is about to begin. There will be 12 rounds in total and the maximum number of categories to track will be 5.\n\nHere is a reminder of all the possible words:\n\n- Animals: bear, dog, horse, lion, rabbit, wolf\n- Colors: blue, green, white, purple, red, yellow\n- Countries: Australia, Brazil, China, Italy, India, Japan\n- Fruits: banana, strawberry, melon, pear, apple, apricot\n- Body: mouth, arm, elbow, foot, leg, hand\n- Family: mother, father, brother, sister, aunt, uncle\n\n!Important!\nIt is important that you memorize the words.\nDo not write down the words.\n\nYou can start the test when you are ready.",
            'Pause': "Pause\n\nPress the space bar when you are ready to continue",
            'text_end_task': "This task is now over.\n\nThank you!\n\nPress the space bar to continue",
            'MemorizeCategories': "Memorize the words from the following categories:\n\n\n\nPress spacebar when ready"
        }
    else:  # Default to French if any issues
        instructions = {
            'name_task': 'KEEP-TRACK',
            'Introduction1': "Bienvenue dans la tâche de 'Keep-Track'.\nDans cette tâche, une séquence de 15 mots vous sera présentée, un par un au milieu de l'écran.\n\nLes mots seront sélectionnés parmi les 6 catégories suivantes :\n\n- Animaux: ours, chien, cheval, lion, lapin, loup\n- Couleurs: bleu, vert, blanc, violet, rouge, jaune\n- Pays: Australie, Brésil, Chine, Italie, Inde, Japon\n- Fruits: banane, fraise, melon, poire, pomme, abricot\n- Corps: bouche, bras, coude, pied, jambe, main\n- Famille: mère, père, frère, soeur, tante, oncle\n\nPrenez un moment pour vous familiariser avec les mots.",
            'Introduction2': "Une fois que les 15 mots auront défilés, il vous sera demandé de rappeler le dernier mot présenté pour les catégories sélectionnées.\nIl vous sera toujours indiqué les catégories auxquelles il faudra prêter attention avant le début de chaque nouvelle manche.\n\nExemple: Les catégories à suivre sont : 'Animaux' et 'Famille'.\n\nLes 15 mots défilent un par un au milieu de l'écran. Le dernier élément présenté pour la catégorie 'Animaux' est 'ours'. Tapez 'ours' pour 'Animaux' lorsqu'on vous demandera d'entrer vos réponses dans les zones de texte. Vérifiez bien que l'orthographe du mot que vous entrez est correcte.\n\n!Important!\nIl est important que vous mémorisiez les mots.\nN'écrivez pas les mots.\n\nVous pouvez commencer l'entraînement quand vous êtes prêt.",
            'Start_Actual_Task': "Début du test\n\nL'entraînement est terminé et le test est sur le point de commencer. Il y aura 12 manches au total et le nombre maximum de catégories à suivre sera de 5.\n\nVoici un rappel de tous les mots possibles:\n\n- Animaux: ours, chien, cheval, lion, lapin, loup\n- Couleurs: bleu, vert, blanc, violet, rouge, jaune\n- Pays: Australie, Brésil, Chine, Italie, Inde, Japon\n- Fruits: banane, fraise, melon, poire, pomme, abricot\n- Corps: bouche, bras, coude, pied, jambe, main\n- Famille: mère, père, frère, soeur, tante, oncle\n\n!Important!\nIl est important que vous mémorisiez les mots.\nN'écrivez pas les mots.\n\nVous pouvez commencer le test quand vous êtes prêt.",
            'Pause': "Pause\n\nAppuyez sur la barre d'espace lorsque vous êtes prêt·e à continuer",
            'text_end_task': "Cette tâche est maintenant terminée.\n\nMerci !\n\nAppuyez sur la barre d'espace pour continuer",
            'MemorizeCategories': "Mémorisez les mots des catégories suivantes :\n\n\n\nAppuyez sur la barre d'espace pour continuer"
        }
    
    # Category translation dictionary with lowercase keys
    category_translations = {
        'animal': 'animal',
        'color': 'couleur',
        'country': 'pays',
        'fruit': 'fruit',
        'body': 'corps',
        'family': 'famille'
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
    instruction_text_component_introduction_1 = visual.TextStim(win=win, name='instruction_text_component_introduction_1',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.6, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    end_inst_1 = keyboard.Keyboard(deviceName='end_inst_1')
    nametask = visual.TextStim(win=win, name='nametask',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "instructions2" ---
    instruction_text_component_introduction_2 = visual.TextStim(win=win, name='instruction_text_component_introduction_2',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.04, wrapWidth=1.6, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    end_inst_2 = keyboard.Keyboard(deviceName='end_inst_2')
    # Run 'Begin Experiment' code from code_initialize_block_index
    # Initialize block variables
    block_index = 0  # Start with the first block for practice
    is_practice = True
    is_test = False
    nametask_2 = visual.TextStim(win=win, name='nametask_2',
        text=None,
        font='Arial',
        pos=(0, 0.45), height=0.06, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-5.0);
    
    # --- Initialize components for Routine "block_counter_practice" ---
    
    # --- Initialize components for Routine "instructions_test" ---
    text_instructions = visual.TextStim(win=win, name='text_instructions',
        text='',
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_categories = visual.TextStim(win=win, name='text_categories',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "ISI" ---
    ISI_wait = visual.TextStim(win=win, name='ISI_wait',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_categories_ISI = visual.TextStim(win=win, name='text_categories_ISI',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "stimulus" ---
    word = visual.TextStim(win=win, name='word',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_categories_stim = visual.TextStim(win=win, name='text_categories_stim',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "response" ---
    textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0, 0),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-1, autoLog=True,
    )
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
    # --- Initialize components for Routine "startTask" ---
    instruction_text_component_start_task = visual.TextStim(win=win, name='instruction_text_component_start_task',
        text=None,
        font='Arial',
        units='height', pos=(0, 0), height=0.05, wrapWidth=1.5, ori=0, 
        color='white', colorSpace='rgb', opacity=1, 
        languageStyle='LTR',
        depth=0.0);
    start_Task = keyboard.Keyboard(deviceName='start_Task')
    
    # --- Initialize components for Routine "block_counter" ---
    # Run 'Begin Experiment' code from LSL_start_testblock
    send_marker("start_block")
    
    # --- Initialize components for Routine "instructions_test" ---
    text_instructions = visual.TextStim(win=win, name='text_instructions',
        text='',
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=1.5, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-2.0);
    text_categories = visual.TextStim(win=win, name='text_categories',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-4.0);
    key_resp = keyboard.Keyboard(deviceName='key_resp')
    
    # --- Initialize components for Routine "ISI" ---
    ISI_wait = visual.TextStim(win=win, name='ISI_wait',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_categories_ISI = visual.TextStim(win=win, name='text_categories_ISI',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-1.0);
    
    # --- Initialize components for Routine "stimulus" ---
    word = visual.TextStim(win=win, name='word',
        text=None,
        font='Arial',
        pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=0.0);
    text_categories_stim = visual.TextStim(win=win, name='text_categories_stim',
        text=None,
        font='Arial',
        pos=(0, -0.15), height=0.04, wrapWidth=None, ori=0.0, 
        color='white', colorSpace='rgb', opacity=None, 
        languageStyle='LTR',
        depth=-3.0);
    
    # --- Initialize components for Routine "response" ---
    textbox = visual.TextBox2(
         win, text=None, placeholder='Type here...', font='Arial',
         pos=(0, 0),     letterHeight=0.05,
         size=(0.5, 0.5), borderWidth=2.0,
         color='white', colorSpace='rgb',
         opacity=None,
         bold=False, italic=False,
         lineSpacing=1.0, speechPoint=None,
         padding=0.0, alignment='center',
         anchor='center', overflow='visible',
         fillColor=None, borderColor=None,
         flipHoriz=False, flipVert=False, languageStyle='LTR',
         editable=False,
         name='textbox',
         depth=-1, autoLog=True,
    )
    mouse = event.Mouse(win=win)
    x, y = [None, None]
    mouse.mouseClock = core.Clock()
    
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
    instruction_text_component_introduction_1.setText('')
    end_inst_1.keys = []
    end_inst_1.rt = []
    _end_inst_1_allKeys = []
    # Run 'Begin Routine' code from code_Instructions_1
    instruction_text_component_introduction_1.text = instructions['Introduction1']
    
    # Run 'Begin Routine' code from LSL_KT_start
    send_marker('KeepTrack_start')
    # Run 'Begin Routine' code from code_nametask
    nametask.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions1Components = [instruction_text_component_introduction_1, end_inst_1, nametask]
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
        
        # *instruction_text_component_introduction_1* updates
        
        # if instruction_text_component_introduction_1 is starting this frame...
        if instruction_text_component_introduction_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text_component_introduction_1.frameNStart = frameN  # exact frame index
            instruction_text_component_introduction_1.tStart = t  # local t and not account for scr refresh
            instruction_text_component_introduction_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text_component_introduction_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text_component_introduction_1.started')
            # update status
            instruction_text_component_introduction_1.status = STARTED
            instruction_text_component_introduction_1.setAutoDraw(True)
        
        # if instruction_text_component_introduction_1 is active this frame...
        if instruction_text_component_introduction_1.status == STARTED:
            # update params
            pass
        
        # *end_inst_1* updates
        waitOnFlip = False
        
        # if end_inst_1 is starting this frame...
        if end_inst_1.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_inst_1.frameNStart = frameN  # exact frame index
            end_inst_1.tStart = t  # local t and not account for scr refresh
            end_inst_1.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_inst_1, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_inst_1.started')
            # update status
            end_inst_1.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_inst_1.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_inst_1.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_inst_1.status == STARTED and not waitOnFlip:
            theseKeys = end_inst_1.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _end_inst_1_allKeys.extend(theseKeys)
            if len(_end_inst_1_allKeys):
                end_inst_1.keys = _end_inst_1_allKeys[-1].name  # just the last key pressed
                end_inst_1.rt = _end_inst_1_allKeys[-1].rt
                end_inst_1.duration = _end_inst_1_allKeys[-1].duration
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
    thisExp.nextEntry()
    # the Routine "instructions1" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # --- Prepare to start Routine "instructions2" ---
    continueRoutine = True
    # update component parameters for each repeat
    thisExp.addData('instructions2.started', globalClock.getTime(format='float'))
    instruction_text_component_introduction_2.setText('')
    end_inst_2.keys = []
    end_inst_2.rt = []
    _end_inst_2_allKeys = []
    # Run 'Begin Routine' code from code_Instructions_2
    instruction_text_component_introduction_2.text = instructions['Introduction2']
    
    # Run 'Begin Routine' code from code_nametask_2
    nametask_2.setText(instructions['name_task'])
    
    # keep track of which components have finished
    instructions2Components = [instruction_text_component_introduction_2, end_inst_2, nametask_2]
    for thisComponent in instructions2Components:
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
    
    # --- Run Routine "instructions2" ---
    routineForceEnded = not continueRoutine
    while continueRoutine:
        # get current time
        t = routineTimer.getTime()
        tThisFlip = win.getFutureFlipTime(clock=routineTimer)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *instruction_text_component_introduction_2* updates
        
        # if instruction_text_component_introduction_2 is starting this frame...
        if instruction_text_component_introduction_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            instruction_text_component_introduction_2.frameNStart = frameN  # exact frame index
            instruction_text_component_introduction_2.tStart = t  # local t and not account for scr refresh
            instruction_text_component_introduction_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(instruction_text_component_introduction_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'instruction_text_component_introduction_2.started')
            # update status
            instruction_text_component_introduction_2.status = STARTED
            instruction_text_component_introduction_2.setAutoDraw(True)
        
        # if instruction_text_component_introduction_2 is active this frame...
        if instruction_text_component_introduction_2.status == STARTED:
            # update params
            pass
        
        # *end_inst_2* updates
        waitOnFlip = False
        
        # if end_inst_2 is starting this frame...
        if end_inst_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            end_inst_2.frameNStart = frameN  # exact frame index
            end_inst_2.tStart = t  # local t and not account for scr refresh
            end_inst_2.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_inst_2, 'tStartRefresh')  # time at next scr refresh
            # add timestamp to datafile
            thisExp.timestampOnFlip(win, 'end_inst_2.started')
            # update status
            end_inst_2.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(end_inst_2.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(end_inst_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if end_inst_2.status == STARTED and not waitOnFlip:
            theseKeys = end_inst_2.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
            _end_inst_2_allKeys.extend(theseKeys)
            if len(_end_inst_2_allKeys):
                end_inst_2.keys = _end_inst_2_allKeys[-1].name  # just the last key pressed
                end_inst_2.rt = _end_inst_2_allKeys[-1].rt
                end_inst_2.duration = _end_inst_2_allKeys[-1].duration
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
        for thisComponent in instructions2Components:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # --- Ending Routine "instructions2" ---
    for thisComponent in instructions2Components:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    thisExp.addData('instructions2.stopped', globalClock.getTime(format='float'))
    thisExp.nextEntry()
    # the Routine "instructions2" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    practiceblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('keep_track_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        send_marker("start_practice")
        # Run 'End Routine' code from code_2
        print("block_n = " + str(block_n))
        # the Routine "block_counter_practice" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # --- Prepare to start Routine "instructions_test" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('instructions_test.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from code_IdentifyCategories
        # Determine the current block type and number
        if is_practice:
            block_type = 'practice'
        else:
            block_type = 'test'
        
        # Initialize categories_to_memorize as an empty list
        categories_to_memorize = []
        
        # Get the number of words to memorize from the current block
        num_categories = int(scenario_df[(scenario_df['block'] == block_type) & (scenario_df['block_n'] == block_index)].iloc[0]['word_n'])
        
        # Dynamically add categories based on the CSV columns
        for i in range(1, num_categories + 1):
            category = scenario_df[(scenario_df['block'] == block_type) & (scenario_df['block_n'] == block_index)].iloc[0][f'cat_to_memorize{i}']
            if category != 'NA':
                # Translate the category if language is French
                if language == "French" and category in category_translations:
                    category = category_translations[category]
                categories_to_memorize.append(category)
        
        # Save the categories to memorize in the experiment data
        thisExp.addData('categories_to_memorize', categories_to_memorize)
        
        text_instructions.setText('\n')
        # Run 'Begin Routine' code from code_text_instructions
        text_instructions.setText(instructions['MemorizeCategories'])
        # Run 'Begin Routine' code from code_text_categories
        # Translate categories if language is French
        if language == "French":
            categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
        
        text_categories.setText("   ".join(categories_to_memorize))
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        instructions_testComponents = [text_instructions, text_categories, key_resp]
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
            # Run 'Each Frame' code from code_mouse
            event.Mouse(visible=False)
            
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
            
            # *text_categories* updates
            
            # if text_categories is starting this frame...
            if text_categories.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_categories.frameNStart = frameN  # exact frame index
                text_categories.tStart = t  # local t and not account for scr refresh
                text_categories.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_categories, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_categories.started')
                # update status
                text_categories.status = STARTED
                text_categories.setAutoDraw(True)
            
            # if text_categories is active this frame...
            if text_categories.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
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
        # Run 'End Routine' code from LSL_start_practice
        send_marker('practice_block')
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        practiceblocks.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            practiceblocks.addData('key_resp.rt', key_resp.rt)
            practiceblocks.addData('key_resp.duration', key_resp.duration)
        # the Routine "instructions_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        practiceTrials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('keep_track_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'practice') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            ISI_wait.setText('')
            # Run 'Begin Routine' code from code_text_categories_ISI
            # Translate categories if language is French
            if language == "French":
                categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
            
            text_categories_ISI.setText("   ".join(categories_to_memorize))
            # keep track of which components have finished
            ISIComponents = [ISI_wait, text_categories_ISI]
            for thisComponent in ISIComponents:
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
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI_wait* updates
                
                # if ISI_wait is starting this frame...
                if ISI_wait.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    ISI_wait.frameNStart = frameN  # exact frame index
                    ISI_wait.tStart = t  # local t and not account for scr refresh
                    ISI_wait.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_wait, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_wait.started')
                    # update status
                    ISI_wait.status = STARTED
                    ISI_wait.setAutoDraw(True)
                
                # if ISI_wait is active this frame...
                if ISI_wait.status == STARTED:
                    # update params
                    pass
                
                # if ISI_wait is stopping this frame...
                if ISI_wait.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        ISI_wait.tStop = t  # not accounting for scr refresh
                        ISI_wait.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI_wait.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_wait.stopped')
                        # update status
                        ISI_wait.status = FINISHED
                        ISI_wait.setAutoDraw(False)
                
                # *text_categories_ISI* updates
                
                # if text_categories_ISI is starting this frame...
                if text_categories_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_categories_ISI.frameNStart = frameN  # exact frame index
                    text_categories_ISI.tStart = t  # local t and not account for scr refresh
                    text_categories_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_categories_ISI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_categories_ISI.started')
                    # update status
                    text_categories_ISI.status = STARTED
                    text_categories_ISI.setAutoDraw(True)
                
                # if text_categories_ISI is active this frame...
                if text_categories_ISI.status == STARTED:
                    # update params
                    pass
                
                # if text_categories_ISI is stopping this frame...
                if text_categories_ISI.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        text_categories_ISI.tStop = t  # not accounting for scr refresh
                        text_categories_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                        text_categories_ISI.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_categories_ISI.stopped')
                        # update status
                        text_categories_ISI.status = FINISHED
                        text_categories_ISI.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stimulus" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stimulus.started', globalClock.getTime(format='float'))
            word.setText('')
            # Run 'Begin Routine' code from code_word
            # Check if expInfo exists and create the language variable
            if 'expInfo' not in globals():
                expInfo = {}
            
            # Set default values to English if it is missing from expInfo keys
            if 'language' not in expInfo:
                expInfo['language'] = 'English'
            
            # Create the language variable
            language = expInfo.get('language')
            
            if language == "English":
                word.text = stim_eng
            else:
                word.text = stim_fr
            
            
            # Run 'Begin Routine' code from LSL_word
            if language == "English":
                send_marker(stim_eng)
            else:
                send_marker(stim_fr)
            # Run 'Begin Routine' code from code_text_categories_stim
            # Translate categories if language is French
            if language == "French":
                categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
            
            text_categories_stim.setText("   ".join(categories_to_memorize))
            # keep track of which components have finished
            stimulusComponents = [word, text_categories_stim]
            for thisComponent in stimulusComponents:
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
            
            # --- Run Routine "stimulus" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *word* updates
                
                # if word is starting this frame...
                if word.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    word.frameNStart = frameN  # exact frame index
                    word.tStart = t  # local t and not account for scr refresh
                    word.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'word.started')
                    # update status
                    word.status = STARTED
                    word.setAutoDraw(True)
                
                # if word is active this frame...
                if word.status == STARTED:
                    # update params
                    pass
                
                # if word is stopping this frame...
                if word.status == STARTED:
                    if frameN >= 90:
                        # keep track of stop time/frame for later
                        word.tStop = t  # not accounting for scr refresh
                        word.tStopRefresh = tThisFlipGlobal  # on global time
                        word.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'word.stopped')
                        # update status
                        word.status = FINISHED
                        word.setAutoDraw(False)
                
                # *text_categories_stim* updates
                
                # if text_categories_stim is starting this frame...
                if text_categories_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_categories_stim.frameNStart = frameN  # exact frame index
                    text_categories_stim.tStart = t  # local t and not account for scr refresh
                    text_categories_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_categories_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_categories_stim.started')
                    # update status
                    text_categories_stim.status = STARTED
                    text_categories_stim.setAutoDraw(True)
                
                # if text_categories_stim is active this frame...
                if text_categories_stim.status == STARTED:
                    # update params
                    pass
                
                # if text_categories_stim is stopping this frame...
                if text_categories_stim.status == STARTED:
                    if frameN >= 90:
                        # keep track of stop time/frame for later
                        text_categories_stim.tStop = t  # not accounting for scr refresh
                        text_categories_stim.tStopRefresh = tThisFlipGlobal  # on global time
                        text_categories_stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_categories_stim.stopped')
                        # update status
                        text_categories_stim.status = FINISHED
                        text_categories_stim.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimulusComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stimulus" ---
            for thisComponent in stimulusComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stimulus.stopped', globalClock.getTime(format='float'))
            # the Routine "stimulus" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            thisExp.nextEntry()
            
            if thisSession is not None:
                # if running in a Session with a Liaison client, send data up to now
                thisSession.sendExperimentData()
        # completed 1.0 repeats of 'practiceTrials'
        
        
        # --- Prepare to start Routine "response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from DynamicTextBoxes
        # Create a list to hold the text boxes
        text_boxes = []
        
        # Create the text boxes dynamically based on categories_to_memorize
        for i, category in enumerate(categories_to_memorize):
            # Create a new text box with the category name
            text_box = visual.TextBox2(
                win=win, 
                text=f"{category}: ",  # Include category name
                font='Arial',
                pos=(0, 0.2 - i*0.1),  # Adjust the position as needed
                letterHeight=0.05,
                size=(1.0, 0.1),
                borderWidth=2.0,
                color='black',
                colorSpace='rgb',
                opacity=None,
                bold=False,
                italic=False,
                lineSpacing=1.0,
                padding=None,
                alignment='center',
                anchor='center',
                fillColor='white',
                borderColor='black',
                flipHoriz=False,
                flipVert=False,
                editable=True,
                name=f'text_box_{i}',
                autoLog=True,
            )
            # Add the text box to the list
            text_boxes.append(text_box)
        
        # Create a "Validate" button
        validate_button = visual.ButtonStim(
            win,
            text='Validate',
            font='Arial',
            pos=(0, -0.4),  # Position it below the text boxes
            letterHeight=0.05,
            size=(0.3, 0.1),
            borderWidth=2.0,
            fillColor='lightgrey',
            borderColor='black',
            color='black',
            colorSpace='rgb',
            opacity=1,
            bold=True,
            italic=False,
            padding=None,
            anchor='center',
            name='validate_button'
        )
        
        textbox.reset()
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from LSL_recall
        send_marker('recall')
        # keep track of which components have finished
        responseComponents = [textbox, mouse]
        for thisComponent in responseComponents:
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
        
        # --- Run Routine "response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from DynamicTextBoxes
            # Activate Mouse
            event.Mouse(visible=True)
            
            # Draw the text boxes
            for text_box in text_boxes:
                text_box.draw()
            
            # Draw the validate button
            validate_button.draw()
            
            # Check for mouse clicks on the validate button
            if mouse.isPressedIn(validate_button):
                continueRoutine = False  # End the routine when the button is clicked
            
            
            # *textbox* updates
            
            # if textbox is starting this frame...
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                # update status
                textbox.status = STARTED
                textbox.setAutoDraw(True)
            
            # if textbox is active this frame...
            if textbox.status == STARTED:
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
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response" ---
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from DynamicTextBoxes
        # Clear the text boxes
        for text_box in text_boxes:
            text_box.setAutoDraw(False)
        
        # Save the responses
        responses = {}
        for i, text_box in enumerate(text_boxes):
            responses[f'category_{i}'] = text_box.text
        
        # Save the responses in the experiment data
        thisExp.addData('responses', responses)
        
        # Run 'End Routine' code from check_block_counter_practice
        # Check if the block is test and block_n is to skip the loop
        #if is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique()):
        #    practiceblocks.finished = True  # Skip the loop
        
        # Check if the block is practice or test and if block_index exceeds the number of available blocks to skip the loop
        if (is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique())) or (is_test and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique())):
            if is_practice:
                print("All practice blocks completed.")
                practiceblocks.finished = True  # Skip the practice loop
            elif is_test:
                print("All test blocks completed.")
                testblocks.finished = True  # Skip the test loop
        # store data for practiceblocks (TrialHandler)
        practiceblocks.addData('mouse.x', mouse.x)
        practiceblocks.addData('mouse.y', mouse.y)
        practiceblocks.addData('mouse.leftButton', mouse.leftButton)
        practiceblocks.addData('mouse.midButton', mouse.midButton)
        practiceblocks.addData('mouse.rightButton', mouse.rightButton)
        practiceblocks.addData('mouse.time', mouse.time)
        # Run 'End Routine' code from LSL_recall
        send_marker('end_recall')
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        thisExp.nextEntry()
        
        if thisSession is not None:
            # if running in a Session with a Liaison client, send data up to now
            thisSession.sendExperimentData()
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
    is_practice = False
    # Run 'Begin Routine' code from test_script
    # Debugging print statements
    print("START TASK")
    print("START TASK")
    print("START TASK")
    print("START TASK")
    print("START TASK")
    print("START TASK")
    print("START TASK")
    
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
    send_marker("start_test_blocks")
    thisExp.nextEntry()
    # the Routine "startTask" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # set up handler to look after randomisation of conditions etc
    testblocks = data.TrialHandler(nReps=1.0, method='sequential', 
        extraInfo=expInfo, originPath=-1,
        trialList=data.importConditions('keep_track_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
        # Run 'Begin Routine' code from code_IdentifyCategories
        # Determine the current block type and number
        if is_practice:
            block_type = 'practice'
        else:
            block_type = 'test'
        
        # Initialize categories_to_memorize as an empty list
        categories_to_memorize = []
        
        # Get the number of words to memorize from the current block
        num_categories = int(scenario_df[(scenario_df['block'] == block_type) & (scenario_df['block_n'] == block_index)].iloc[0]['word_n'])
        
        # Dynamically add categories based on the CSV columns
        for i in range(1, num_categories + 1):
            category = scenario_df[(scenario_df['block'] == block_type) & (scenario_df['block_n'] == block_index)].iloc[0][f'cat_to_memorize{i}']
            if category != 'NA':
                # Translate the category if language is French
                if language == "French" and category in category_translations:
                    category = category_translations[category]
                categories_to_memorize.append(category)
        
        # Save the categories to memorize in the experiment data
        thisExp.addData('categories_to_memorize', categories_to_memorize)
        
        text_instructions.setText('\n')
        # Run 'Begin Routine' code from code_text_instructions
        text_instructions.setText(instructions['MemorizeCategories'])
        # Run 'Begin Routine' code from code_text_categories
        # Translate categories if language is French
        if language == "French":
            categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
        
        text_categories.setText("   ".join(categories_to_memorize))
        key_resp.keys = []
        key_resp.rt = []
        _key_resp_allKeys = []
        # keep track of which components have finished
        instructions_testComponents = [text_instructions, text_categories, key_resp]
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
            # Run 'Each Frame' code from code_mouse
            event.Mouse(visible=False)
            
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
            
            # *text_categories* updates
            
            # if text_categories is starting this frame...
            if text_categories.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                text_categories.frameNStart = frameN  # exact frame index
                text_categories.tStart = t  # local t and not account for scr refresh
                text_categories.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(text_categories, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'text_categories.started')
                # update status
                text_categories.status = STARTED
                text_categories.setAutoDraw(True)
            
            # if text_categories is active this frame...
            if text_categories.status == STARTED:
                # update params
                pass
            
            # *key_resp* updates
            waitOnFlip = False
            
            # if key_resp is starting this frame...
            if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
                theseKeys = key_resp.getKeys(keyList=['space'], ignoreKeys=None, waitRelease=False)
                _key_resp_allKeys.extend(theseKeys)
                if len(_key_resp_allKeys):
                    key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
                    key_resp.rt = _key_resp_allKeys[-1].rt
                    key_resp.duration = _key_resp_allKeys[-1].duration
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
        # Run 'End Routine' code from LSL_start_practice
        send_marker('practice_block')
        # check responses
        if key_resp.keys in ['', [], None]:  # No response was made
            key_resp.keys = None
        testblocks.addData('key_resp.keys',key_resp.keys)
        if key_resp.keys != None:  # we had a response
            testblocks.addData('key_resp.rt', key_resp.rt)
            testblocks.addData('key_resp.duration', key_resp.duration)
        # the Routine "instructions_test" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
        # set up handler to look after randomisation of conditions etc
        testTrials = data.TrialHandler(nReps=1.0, method='sequential', 
            extraInfo=expInfo, originPath=-1,
            trialList=data.importConditions('keep_track_scenario.csv', selection=scenario_df[(scenario_df['block'] == 'test') & (scenario_df['block_n'] == block_index)].index.tolist()),
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
            
            # --- Prepare to start Routine "ISI" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('ISI.started', globalClock.getTime(format='float'))
            ISI_wait.setText('')
            # Run 'Begin Routine' code from code_text_categories_ISI
            # Translate categories if language is French
            if language == "French":
                categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
            
            text_categories_ISI.setText("   ".join(categories_to_memorize))
            # keep track of which components have finished
            ISIComponents = [ISI_wait, text_categories_ISI]
            for thisComponent in ISIComponents:
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
            
            # --- Run Routine "ISI" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *ISI_wait* updates
                
                # if ISI_wait is starting this frame...
                if ISI_wait.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    ISI_wait.frameNStart = frameN  # exact frame index
                    ISI_wait.tStart = t  # local t and not account for scr refresh
                    ISI_wait.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(ISI_wait, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'ISI_wait.started')
                    # update status
                    ISI_wait.status = STARTED
                    ISI_wait.setAutoDraw(True)
                
                # if ISI_wait is active this frame...
                if ISI_wait.status == STARTED:
                    # update params
                    pass
                
                # if ISI_wait is stopping this frame...
                if ISI_wait.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        ISI_wait.tStop = t  # not accounting for scr refresh
                        ISI_wait.tStopRefresh = tThisFlipGlobal  # on global time
                        ISI_wait.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'ISI_wait.stopped')
                        # update status
                        ISI_wait.status = FINISHED
                        ISI_wait.setAutoDraw(False)
                
                # *text_categories_ISI* updates
                
                # if text_categories_ISI is starting this frame...
                if text_categories_ISI.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_categories_ISI.frameNStart = frameN  # exact frame index
                    text_categories_ISI.tStart = t  # local t and not account for scr refresh
                    text_categories_ISI.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_categories_ISI, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_categories_ISI.started')
                    # update status
                    text_categories_ISI.status = STARTED
                    text_categories_ISI.setAutoDraw(True)
                
                # if text_categories_ISI is active this frame...
                if text_categories_ISI.status == STARTED:
                    # update params
                    pass
                
                # if text_categories_ISI is stopping this frame...
                if text_categories_ISI.status == STARTED:
                    if frameN >= 30:
                        # keep track of stop time/frame for later
                        text_categories_ISI.tStop = t  # not accounting for scr refresh
                        text_categories_ISI.tStopRefresh = tThisFlipGlobal  # on global time
                        text_categories_ISI.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_categories_ISI.stopped')
                        # update status
                        text_categories_ISI.status = FINISHED
                        text_categories_ISI.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in ISIComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "ISI" ---
            for thisComponent in ISIComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('ISI.stopped', globalClock.getTime(format='float'))
            # the Routine "ISI" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
            
            # --- Prepare to start Routine "stimulus" ---
            continueRoutine = True
            # update component parameters for each repeat
            thisExp.addData('stimulus.started', globalClock.getTime(format='float'))
            word.setText('')
            # Run 'Begin Routine' code from code_word
            # Check if expInfo exists and create the language variable
            if 'expInfo' not in globals():
                expInfo = {}
            
            # Set default values to English if it is missing from expInfo keys
            if 'language' not in expInfo:
                expInfo['language'] = 'English'
            
            # Create the language variable
            language = expInfo.get('language')
            
            if language == "English":
                word.text = stim_eng
            else:
                word.text = stim_fr
            
            
            # Run 'Begin Routine' code from LSL_word
            if language == "English":
                send_marker(stim_eng)
            else:
                send_marker(stim_fr)
            # Run 'Begin Routine' code from code_text_categories_stim
            # Translate categories if language is French
            if language == "French":
                categories_to_memorize = [category_translations.get(cat, cat) for cat in categories_to_memorize]
            
            text_categories_stim.setText("   ".join(categories_to_memorize))
            # keep track of which components have finished
            stimulusComponents = [word, text_categories_stim]
            for thisComponent in stimulusComponents:
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
            
            # --- Run Routine "stimulus" ---
            routineForceEnded = not continueRoutine
            while continueRoutine:
                # get current time
                t = routineTimer.getTime()
                tThisFlip = win.getFutureFlipTime(clock=routineTimer)
                tThisFlipGlobal = win.getFutureFlipTime(clock=None)
                frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
                # update/draw components on each frame
                
                # *word* updates
                
                # if word is starting this frame...
                if word.status == NOT_STARTED and frameN >= 0:
                    # keep track of start time/frame for later
                    word.frameNStart = frameN  # exact frame index
                    word.tStart = t  # local t and not account for scr refresh
                    word.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(word, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'word.started')
                    # update status
                    word.status = STARTED
                    word.setAutoDraw(True)
                
                # if word is active this frame...
                if word.status == STARTED:
                    # update params
                    pass
                
                # if word is stopping this frame...
                if word.status == STARTED:
                    if frameN >= 90:
                        # keep track of stop time/frame for later
                        word.tStop = t  # not accounting for scr refresh
                        word.tStopRefresh = tThisFlipGlobal  # on global time
                        word.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'word.stopped')
                        # update status
                        word.status = FINISHED
                        word.setAutoDraw(False)
                
                # *text_categories_stim* updates
                
                # if text_categories_stim is starting this frame...
                if text_categories_stim.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                    # keep track of start time/frame for later
                    text_categories_stim.frameNStart = frameN  # exact frame index
                    text_categories_stim.tStart = t  # local t and not account for scr refresh
                    text_categories_stim.tStartRefresh = tThisFlipGlobal  # on global time
                    win.timeOnFlip(text_categories_stim, 'tStartRefresh')  # time at next scr refresh
                    # add timestamp to datafile
                    thisExp.timestampOnFlip(win, 'text_categories_stim.started')
                    # update status
                    text_categories_stim.status = STARTED
                    text_categories_stim.setAutoDraw(True)
                
                # if text_categories_stim is active this frame...
                if text_categories_stim.status == STARTED:
                    # update params
                    pass
                
                # if text_categories_stim is stopping this frame...
                if text_categories_stim.status == STARTED:
                    if frameN >= 90:
                        # keep track of stop time/frame for later
                        text_categories_stim.tStop = t  # not accounting for scr refresh
                        text_categories_stim.tStopRefresh = tThisFlipGlobal  # on global time
                        text_categories_stim.frameNStop = frameN  # exact frame index
                        # add timestamp to datafile
                        thisExp.timestampOnFlip(win, 'text_categories_stim.stopped')
                        # update status
                        text_categories_stim.status = FINISHED
                        text_categories_stim.setAutoDraw(False)
                if thisExp.status == FINISHED or endExpNow:
                    endExperiment(thisExp, win=win)
                    return
                
                # check if all components have finished
                if not continueRoutine:  # a component has requested a forced-end of Routine
                    routineForceEnded = True
                    break
                continueRoutine = False  # will revert to True if at least one component still running
                for thisComponent in stimulusComponents:
                    if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                        continueRoutine = True
                        break  # at least one component has not yet finished
                
                # refresh the screen
                if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                    win.flip()
            
            # --- Ending Routine "stimulus" ---
            for thisComponent in stimulusComponents:
                if hasattr(thisComponent, "setAutoDraw"):
                    thisComponent.setAutoDraw(False)
            thisExp.addData('stimulus.stopped', globalClock.getTime(format='float'))
            # the Routine "stimulus" was not non-slip safe, so reset the non-slip timer
            routineTimer.reset()
        # completed 1.0 repeats of 'testTrials'
        
        
        # --- Prepare to start Routine "response" ---
        continueRoutine = True
        # update component parameters for each repeat
        thisExp.addData('response.started', globalClock.getTime(format='float'))
        # Run 'Begin Routine' code from DynamicTextBoxes
        # Create a list to hold the text boxes
        text_boxes = []
        
        # Create the text boxes dynamically based on categories_to_memorize
        for i, category in enumerate(categories_to_memorize):
            # Create a new text box with the category name
            text_box = visual.TextBox2(
                win=win, 
                text=f"{category}: ",  # Include category name
                font='Arial',
                pos=(0, 0.2 - i*0.1),  # Adjust the position as needed
                letterHeight=0.05,
                size=(1.0, 0.1),
                borderWidth=2.0,
                color='black',
                colorSpace='rgb',
                opacity=None,
                bold=False,
                italic=False,
                lineSpacing=1.0,
                padding=None,
                alignment='center',
                anchor='center',
                fillColor='white',
                borderColor='black',
                flipHoriz=False,
                flipVert=False,
                editable=True,
                name=f'text_box_{i}',
                autoLog=True,
            )
            # Add the text box to the list
            text_boxes.append(text_box)
        
        # Create a "Validate" button
        validate_button = visual.ButtonStim(
            win,
            text='Validate',
            font='Arial',
            pos=(0, -0.4),  # Position it below the text boxes
            letterHeight=0.05,
            size=(0.3, 0.1),
            borderWidth=2.0,
            fillColor='lightgrey',
            borderColor='black',
            color='black',
            colorSpace='rgb',
            opacity=1,
            bold=True,
            italic=False,
            padding=None,
            anchor='center',
            name='validate_button'
        )
        
        textbox.reset()
        # setup some python lists for storing info about the mouse
        mouse.x = []
        mouse.y = []
        mouse.leftButton = []
        mouse.midButton = []
        mouse.rightButton = []
        mouse.time = []
        gotValidClick = False  # until a click is received
        # Run 'Begin Routine' code from LSL_recall
        send_marker('recall')
        # keep track of which components have finished
        responseComponents = [textbox, mouse]
        for thisComponent in responseComponents:
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
        
        # --- Run Routine "response" ---
        routineForceEnded = not continueRoutine
        while continueRoutine:
            # get current time
            t = routineTimer.getTime()
            tThisFlip = win.getFutureFlipTime(clock=routineTimer)
            tThisFlipGlobal = win.getFutureFlipTime(clock=None)
            frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
            # update/draw components on each frame
            # Run 'Each Frame' code from DynamicTextBoxes
            # Activate Mouse
            event.Mouse(visible=True)
            
            # Draw the text boxes
            for text_box in text_boxes:
                text_box.draw()
            
            # Draw the validate button
            validate_button.draw()
            
            # Check for mouse clicks on the validate button
            if mouse.isPressedIn(validate_button):
                continueRoutine = False  # End the routine when the button is clicked
            
            
            # *textbox* updates
            
            # if textbox is starting this frame...
            if textbox.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
                # keep track of start time/frame for later
                textbox.frameNStart = frameN  # exact frame index
                textbox.tStart = t  # local t and not account for scr refresh
                textbox.tStartRefresh = tThisFlipGlobal  # on global time
                win.timeOnFlip(textbox, 'tStartRefresh')  # time at next scr refresh
                # add timestamp to datafile
                thisExp.timestampOnFlip(win, 'textbox.started')
                # update status
                textbox.status = STARTED
                textbox.setAutoDraw(True)
            
            # if textbox is active this frame...
            if textbox.status == STARTED:
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
                prevButtonState = [0, 0, 0]  # if now button is down we will treat as 'new' click
            if mouse.status == STARTED:  # only update if started and not finished!
                buttons = mouse.getPressed()
                if buttons != prevButtonState:  # button state changed?
                    prevButtonState = buttons
                    if sum(buttons) > 0:  # state changed to a new click
                        pass
                        x, y = mouse.getPos()
                        mouse.x.append(x)
                        mouse.y.append(y)
                        buttons = mouse.getPressed()
                        mouse.leftButton.append(buttons[0])
                        mouse.midButton.append(buttons[1])
                        mouse.rightButton.append(buttons[2])
                        mouse.time.append(mouse.mouseClock.getTime())
            if thisExp.status == FINISHED or endExpNow:
                endExperiment(thisExp, win=win)
                return
            
            # check if all components have finished
            if not continueRoutine:  # a component has requested a forced-end of Routine
                routineForceEnded = True
                break
            continueRoutine = False  # will revert to True if at least one component still running
            for thisComponent in responseComponents:
                if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                    continueRoutine = True
                    break  # at least one component has not yet finished
            
            # refresh the screen
            if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
                win.flip()
        
        # --- Ending Routine "response" ---
        for thisComponent in responseComponents:
            if hasattr(thisComponent, "setAutoDraw"):
                thisComponent.setAutoDraw(False)
        thisExp.addData('response.stopped', globalClock.getTime(format='float'))
        # Run 'End Routine' code from DynamicTextBoxes
        # Clear the text boxes
        for text_box in text_boxes:
            text_box.setAutoDraw(False)
        
        # Save the responses
        responses = {}
        for i, text_box in enumerate(text_boxes):
            responses[f'category_{i}'] = text_box.text
        
        # Save the responses in the experiment data
        thisExp.addData('responses', responses)
        
        # Run 'End Routine' code from check_block_counter_practice
        # Check if the block is test and block_n is to skip the loop
        #if is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique()):
        #    practiceblocks.finished = True  # Skip the loop
        
        # Check if the block is practice or test and if block_index exceeds the number of available blocks to skip the loop
        if (is_practice and block_index >= len(scenario_df[scenario_df['block'] == 'practice']['block_n'].unique())) or (is_test and block_index >= len(scenario_df[scenario_df['block'] == 'test']['block_n'].unique())):
            if is_practice:
                print("All practice blocks completed.")
                practiceblocks.finished = True  # Skip the practice loop
            elif is_test:
                print("All test blocks completed.")
                testblocks.finished = True  # Skip the test loop
        # store data for testblocks (TrialHandler)
        testblocks.addData('mouse.x', mouse.x)
        testblocks.addData('mouse.y', mouse.y)
        testblocks.addData('mouse.leftButton', mouse.leftButton)
        testblocks.addData('mouse.midButton', mouse.midButton)
        testblocks.addData('mouse.rightButton', mouse.rightButton)
        testblocks.addData('mouse.time', mouse.time)
        # Run 'End Routine' code from LSL_recall
        send_marker('end_recall')
        # the Routine "response" was not non-slip safe, so reset the non-slip timer
        routineTimer.reset()
        
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
    # Run 'Begin Routine' code from code
    # Set the text for the third set of instructions
    InstructionsText4.setText(instructions['text_end_task'])
    
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
    # Run 'End Routine' code from LSL_KeepTrack_end
    send_marker('KeepTrack_end')
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
