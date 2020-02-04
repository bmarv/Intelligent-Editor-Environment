from Basic_Gui import WindowInstance as WinInstance

global instance

if __name__ == "__main__":
    print("Starting IEE")
    instance = WinInstance.WindowInstance()
    instance.newInstance()