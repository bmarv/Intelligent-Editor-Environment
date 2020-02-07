"author: Marvin Beese"

from Basic_Gui import WindowInstance as WinInstance
from Basic_Gui import AnalysisFrame

global instance

if __name__ == "__main__":
    print("Starting IEE")
    instance = WinInstance.WindowInstance()
    instance.newInstance()

    # test = AnalysisFrame.AnalysisFrame()
    # test.launchAnalysis()