import win32com.client as wincl

speaker_number = 1
spk = wincl.Dispatch("SAPI.SpVoice")
vcs = spk.GetVoices()
SVSFlag = 11
print(vcs.Item (speaker_number) .GetAttribute ("Name")) # speaker name
spk.Voice
spk.SetVoice(vcs.Item(speaker_number)) # set voice (see Windows Text-to-Speech settings)



coders = ["Rahul", "Nishant", "Harry", "Rohan", "Saurav"]

for coder in coders:
    spk.Speak(f'Shoutout to {coder}')


# pip install pywin32 (run this command first in terminal)