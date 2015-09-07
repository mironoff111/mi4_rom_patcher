import os
import sys
import zipfile
import shutil
import re

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)
		
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            zippath = os.path.join(root, file)
            zippath = re.sub(r"miui_rom_tmp", "", zippath)
            ziph.write(os.path.join(root, file), zippath)

def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r') #Opens the file in read-mode
    text = file.read() #Reads the file and assigns the value to a variable
    file.close() #Closes the file (read session)
    file = open(fileName, 'w') #Opens the file again, this time in write-mode
    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
    # and writes the whole output when done, wiping over the old contents of the file
    file.close() #Closes the file (write session)
    print ('Патчим '+fileName)
			
print ('MIUI v7 (Mi3W/Mi4) firmware patcher')	
print ('by mironoff (2015)')
print ('')

if len (sys.argv) > 1:
	print ("Распаковка прошивки...")	
	firmpath = 'miui_rom_tmp'
	unzip(sys.argv[1], firmpath)
	print ("Немного магии...")
	os.remove('miui_rom_tmp/system/app/AntHalService.apk')
	os.remove('miui_rom_tmp/system/app/AntiSpam.apk')
	os.remove('miui_rom_tmp/system/app/BrowserProviderProxy.apk')
	os.remove('miui_rom_tmp/system/app/BugReport.apk')
	os.remove('miui_rom_tmp/system/app/CellBroadcastReceiver.apk')
	os.remove('miui_rom_tmp/system/app/Cit.apk')
	os.remove('miui_rom_tmp/system/app/CloudService.apk')
	os.remove('miui_rom_tmp/system/app/Email.apk')
	os.remove('miui_rom_tmp/system/app/FileExplorer.apk')
	os.remove('miui_rom_tmp/system/app/GoogleCalendarSyncAdapter.apk')
	os.remove('miui_rom_tmp/system/app/GoogleContactsSyncAdapter.apk')
	os.remove('miui_rom_tmp/system/app/GoogleKeyboard.apk')
	os.remove('miui_rom_tmp/system/app/GuardProvider.apk')
	os.remove('miui_rom_tmp/system/app/InterfacePermissions.apk')
	os.remove('miui_rom_tmp/system/app/KingSoftCleaner.apk')
	os.remove('miui_rom_tmp/system/app/LiveWallpapersPicker.apk')
	os.remove('miui_rom_tmp/system/app/MiAssistant.apk')
	os.remove('miui_rom_tmp/system/app/MiLinkService.apk')
	os.remove('miui_rom_tmp/system/app/MiWallpaper.apk')
	os.remove('miui_rom_tmp/system/app/NetworkAssistant2.apk')
	os.remove('miui_rom_tmp/system/app/Nfc.apk')		
	os.remove('miui_rom_tmp/system/app/NVItem.apk')
	os.remove('miui_rom_tmp/system/app/PaymentService.apk')
	os.remove('miui_rom_tmp/system/app/Phonesky.apk')	
	os.remove('miui_rom_tmp/system/app/PicoTts.apk')
	os.remove('miui_rom_tmp/system/app/qcrilmsgtunnel.apk')	
	os.remove('miui_rom_tmp/system/app/TSMClient.apk')
	os.remove('miui_rom_tmp/system/app/WAPPushManager.apk')
	os.remove('miui_rom_tmp/system/app/XiaomiAccount.apk')
	os.remove('miui_rom_tmp/system/app/XiaomiServiceFramework.apk')	
	os.remove('miui_rom_tmp/system/app/XiaomiVip.apk')
	os.remove('miui_rom_tmp/system/priv-app/BarcodeScanner.apk')	
	os.remove('miui_rom_tmp/system/priv-app/Browser.apk')
	os.remove('miui_rom_tmp/system/priv-app/CleanMaster.apk')
	os.remove('miui_rom_tmp/system/priv-app/CloudBackup.apk')
	os.remove('miui_rom_tmp/system/priv-app/com.qualcomm.location.apk')
	os.remove('miui_rom_tmp/system/priv-app/com.qualcomm.msapm.apk')	
	os.remove('miui_rom_tmp/system/priv-app/GoogleBackupTransport.apk')	
	os.remove('miui_rom_tmp/system/priv-app/Mipub.apk')	
	os.remove('miui_rom_tmp/system/priv-app/MiuiVoip.apk')	
	os.remove('miui_rom_tmp/system/priv-app/OneTimeInitializer.apk')	
	os.remove('miui_rom_tmp/system/priv-app/SharedStorageBackup.apk')	
	os.remove('miui_rom_tmp/system/priv-app/SmartcardService.apk')		
	os.remove('miui_rom_tmp/system/priv-app/Tag.apk')		
	os.remove('miui_rom_tmp/system/priv-app/Weather.apk')
	os.remove('miui_rom_tmp/system/priv-app/WeatherProvider.apk')

	os.remove('miui_rom_tmp/system/xbin/su')
	
	shutil.copyfile('miui_blobs/su', 'miui_rom_tmp/system/xbin/su')
	shutil.copyfile('miui_blobs/Superuser.apk', 'miui_rom_tmp/system/app/Superuser.apk')
	shutil.copyfile('miui_blobs/textinput-tng.apk', 'miui_rom_tmp/system/app/textinput-tng.apk')
	shutil.copyfile('miui_blobs/libswiftkeysdk-java.so', 'miui_rom_tmp/system/lib/libswiftkeysdk-java.so')
	
	ReplaceLineInFile('miui_rom_tmp/system/etc/gps.conf', 'time.gpsonextra.net', '194.190.168.1')
	
	zipf = zipfile.ZipFile('miui_rom_patched.zip', 'w')
	zipdir('miui_rom_tmp', zipf)
	zipf.close()
	print ("Прибираемся...")
	shutil.rmtree('miui_rom_tmp')
else:
    print ("Введите имя прошивки!!!!")
os.system("pause")	