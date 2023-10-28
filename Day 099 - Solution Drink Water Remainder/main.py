import time
import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item(speaker_number).GetAttribute("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)

while True:
    # give remainder after every 5 seconds
    time.sleep(5) 
    spk.Speak("Time to drink water")
    print("hello")
    # 1 hour = 3600 seconds



# pip install pywin32 (run this command first in terminal)