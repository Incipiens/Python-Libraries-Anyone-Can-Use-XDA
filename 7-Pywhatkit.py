import pywhatkit as kit

#kit.sendwhatmsg("+123456789", "Hello from Python!", 11, 50)  # Sends a WhatsApp message at 3:30 PM

searchparam = "XDA"
try:
  # it will perform the Google search
  kit.search(searchparam)
  print("Searching for {}".format(searchparam))
 
except:
   
  # Printing Error Message
  print("An unknown error occurred")

kit.image_to_ascii_art("xda-logo.png", "pywhatkitascii")