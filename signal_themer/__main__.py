import os 
import platform


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
