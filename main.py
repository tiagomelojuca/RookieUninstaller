import time
import pyautogui
import pyperclip

# ---------------------------------------------------------------------------------------
POSITION_SAFE_AREA         = pyautogui.Point(1, 1)
POSITION_DROPDOWN          = pyautogui.Point(735, 60)
POSITION_FIRST_ENTRY       = pyautogui.Point(400, 85)
POSITION_BTN_UNINSTALL_APP = pyautogui.Point(150, 220)
RESOURCE_BTN_YES           = 'res/btnYes.png'
RESOURCE_BTN_NO            = 'res/btnNo.png'
RESOURCE_BTN_OK            = 'res/btnOk.png'
# ---------------------------------------------------------------------------------------

def clickWhenReady(resource):
    pyautogui.moveTo(POSITION_SAFE_AREA) # Garante fidelidade do recurso buscado na tela

    foundResource = False
    resBox = None
    while not foundResource:
        try:
            resBox = pyautogui.locateOnScreen(resource, grayscale=True, confidence=.5)
            foundResource = True
        except pyautogui.ImageNotFoundException:
            pass
    
    resLoc = pyautogui.center(resBox)
    pyautogui.click(resLoc)

# ---------------------------------------------------------------------------------------

def selectFirstEntryInDropdown():
    pyautogui.click(POSITION_DROPDOWN)
    pyautogui.click(POSITION_FIRST_ENTRY)

# ---------------------------------------------------------------------------------------

def uninstallCurrentDropdownEntry():
    pyautogui.click(POSITION_BTN_UNINSTALL_APP)
    clickWhenReady(RESOURCE_BTN_YES)
    clickWhenReady(RESOURCE_BTN_NO)
    clickWhenReady(RESOURCE_BTN_OK)

# ---------------------------------------------------------------------------------------

def uninstallFirstEntryInDropdown():
    selectFirstEntryInDropdown()
    uninstallCurrentDropdownEntry()

# ---------------------------------------------------------------------------------------

def getCurrentDropdownEntry():
    selectFirstEntryInDropdown()
    pyautogui.hotkey('ctrl', 'c')
    return pyperclip.paste()

# ---------------------------------------------------------------------------------------

def uninstallEntriesUntil(lastEntry):
    currentEntry = getCurrentDropdownEntry()
    print("Tentando desinstalar " + currentEntry + " ...")

    while currentEntry != lastEntry:
        print("    Desinstalando " + currentEntry + " ...")
        uninstallFirstEntryInDropdown()

        currentEntry = getCurrentDropdownEntry()
        print("Tentando desinstalar " + currentEntry + " ...")

    print("    Desinstalando " + currentEntry + " ...")
    uninstallFirstEntryInDropdown()

# ---------------------------------------------------------------------------------------

time.sleep(5)
uninstallEntriesUntil("Zombies in your Home")

# ---------------------------------------------------------------------------------------
