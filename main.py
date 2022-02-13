import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
from time import sleep
#from spotifyConnection import spotifyConnection

# INIT libs instances
reader = SimpleMFRC522()
# spotifyConnectionInstance = spotifyConnection()


# INIT state variables
currentAlbumID = None
flagPlay = False

# id, text = reader.read()

print('Inicializando...')
sleep(0.5)
print('Esperando album RF')

try: 
  while True :

    id, albumID = reader.read()

    if albumID[0:8] == "spotify:" :
      print(albumID)

      # if albumID is currentAlbumID:
      #   pass

      # else:
      if albumID != currentAlbumID :
        print("PLAY nuevo album")
        flagPlay = True
        currentAlbumID = albumID

      else :
        if flagPlay:
          print("PAUSE")
          flagPlay = False

        else : 
          print("RESUME")
          flagPlay = True
    
    sleep(2)

except :
  GPIO.cleanup()