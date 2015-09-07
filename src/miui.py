import os
import sys
import zipfile
import shutil
import re
from urllib.request import urlretrieve

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)
		
def zipdir(path, ziph):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            s=path_rom_dir+"/miui_rom_tmp"
            s = s.replace("\\", "\\\\")
            zippath = os.path.join(root, file)
            zippath = re.sub(s, "", zippath)
            ziph.write(os.path.join(root, file), zippath)

def ReplaceLineInFile(fileName, sourceText, replaceText):
    file = open(fileName, 'r') #Opens the file in read-mode
    text = file.read() #Reads the file and assigns the value to a variable
    file.close() #Closes the file (read session)
    file = open(fileName, 'w') #Opens the file again, this time in write-mode
    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
    # and writes the whole output when done, wiping over the old contents of the file
    file.close() #Closes the file (write session)
    print ('Патчим '+fileName+'\n')
			
print ('MIUI v7 (Mi3W/Mi4) firmware patcher\n')	
print ('---by mironoff (2015)---\n\n------------------------\n')

path_rom=input('Введите путь до прошивки:\n\n')
path_rom_dir=os.path.dirname(path_rom)
if len (path_rom) > 3:
	print ("\nРаспаковка прошивки...\n")	
	firmpath = path_rom_dir+'/miui_rom_tmp'
	unzip(path_rom, firmpath)
	print ("Немного магии...\n")
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/AntHalService.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/AntiSpam.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/BrowserProviderProxy.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/BugReport.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/CellBroadcastReceiver.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/Cit.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/CloudService.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/Email.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/FileExplorer.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/GoogleCalendarSyncAdapter.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/GoogleContactsSyncAdapter.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/GoogleKeyboard.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/GuardProvider.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/InterfacePermissions.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/KingSoftCleaner.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/LiveWallpapersPicker.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/MiAssistant.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/MiLinkService.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/MiWallpaper.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/NetworkAssistant2.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/Nfc.apk')		
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/NVItem.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/PaymentService.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/Phonesky.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/PicoTts.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/qcrilmsgtunnel.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/TSMClient.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/WAPPushManager.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/XiaomiAccount.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/XiaomiServiceFramework.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/XiaomiVip.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/BarcodeScanner.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/Browser.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/CleanMaster.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/CloudBackup.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/com.qualcomm.location.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/com.qualcomm.msapm.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/GoogleBackupTransport.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/Mipub.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/MiuiVoip.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/OneTimeInitializer.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/SharedStorageBackup.apk')	
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/SmartcardService.apk')		
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/Tag.apk')		
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/Weather.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/WeatherProvider.apk')

	os.remove(path_rom_dir+'/miui_rom_tmp/system/xbin/su')
	
	#BLOBS
	print ("Грузим blobs...\n")
	url = 'https://github.com/mironoff111/mi4_rom_patcher/blob/master/src/miui_blobs.zip?raw=true'
	urlretrieve(url, path_rom_dir+'/miui_blobs.zip')
	unzip(path_rom_dir+'/miui_blobs.zip', path_rom_dir+'/miui_blobs')
	
	shutil.copyfile(path_rom_dir+'/miui_blobs/su', path_rom_dir+'/miui_rom_tmp/system/xbin/su')
	shutil.copyfile(path_rom_dir+'/miui_blobs/Superuser.apk', path_rom_dir+'/miui_rom_tmp/system/app/Superuser.apk')
	shutil.copyfile(path_rom_dir+'/miui_blobs/textinput-tng.apk', path_rom_dir+'/miui_rom_tmp/system/app/textinput-tng.apk')
	shutil.copyfile(path_rom_dir+'/miui_blobs/libswiftkeysdk-java.so', path_rom_dir+'/miui_rom_tmp/system/lib/libswiftkeysdk-java.so')
	
	ReplaceLineInFile(path_rom_dir+'/miui_rom_tmp/system/etc/gps.conf', 'time.gpsonextra.net', '194.190.168.1')
	
	print ("Архивируем...\n")
	
	zipf = zipfile.ZipFile(path_rom_dir+'/miui_rom_patched.zip', 'w')
	zipdir(path_rom_dir+'/miui_rom_tmp', zipf)
	zipf.close()
	print ("Прибираемся...\n")
	shutil.rmtree(path_rom_dir+'/miui_rom_tmp')
	shutil.rmtree(path_rom_dir+'/miui_blobs')
	os.remove(path_rom_dir+'/miui_blobs.zip')
	print ("Всё готово, можно шить!\n")
else:
    print ("Путь не введен!")
os.system("pause")	