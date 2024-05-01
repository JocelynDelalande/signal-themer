import os 
import platform
import sys


# returns path of signal-desktop
def app_path():
    match platform.system():
        case "Linux":
            return "/usr/lib/signal-desktop/resources/app.asar"
        case "Windows":
            return os.path.join(os.getenv("LOCALAPPDATA"), r"Programs\signal-desktop\resources\app.asar")

# returns temp directory depending on os in order to temporily store extracted asar
def temp_path():
    match platform.system():
        case "Linux":
            return "/temp/signal-themer/"
        case "Windows":
            return os.path.join(os.getenv("LOCALAPPDATA"), r"temp\signal-themer")

# reads user argument to read theme path
def selected_theme():
    if(len(sys.argv) != 1):
        sys.exit("Wrong number of argument, try `signal-themer <path-to-theme.css>`")
    elif(os.path.isfile(sys.argv[1])):
        sys.exit("The theme you entered doesn't exist")
    elif(!sys.argv[1].endswith(".css")):
        sys.exit("The theme must be a css file.")
    return sys.argv[1]
