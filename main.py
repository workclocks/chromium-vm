import PySimpleGUI as sg
import sys, os
print("Welcome to the OddGames chrome VM.")
sg.theme('dark grey 9')
layout = [[sg.Text("Welcome to the OddGames chrome VM. PLEASE NOTE THAT CHROME IS A LOT LESS STABLE, FOR A MORE STABLE EXPERIENCE SEARCH firefox IN THE SEARCH BAR")],
         [sg.Button("Open Chromium")]]
window = sg.Window('Unblocker+', layout, icon="u.png")
event, values = window.read()
window.close()
if event == "Open Chromium":
  print("Launching Browser...")
  os.system('chromium-browser --no-sandbox --disable-dinosaur-easter-egg --start-maximized --disable-file-system --disable-extensions --force-device-scale-factor=0.8 --deny-permission-prompts --start-in-incognito 2> ./logs.txt')
  print("Browser launched!")

if event == "Open Firefox":
  print("Launching Browser...")
  os.system('firefox -private > ./logs.txt 2> ./logs.txt')
  print("Browser launched!")
