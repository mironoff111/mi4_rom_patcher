#Oracle JRE REQUIRED!!!!
import os
import sys
import zipfile
try:
    import zlib
    mode= zipfile.ZIP_DEFLATED
except:
    mode= zipfile.ZIP_STORED
import shutil
import re
from urllib.request import urlretrieve

def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)
		
def zipdir(path, ziph, secret):
    # ziph is zipfile handle
    for root, dirs, files in os.walk(path):
        for file in files:
            s=path_rom_dir+secret
            s = s.replace("\\", "\\\\")
            zippath = os.path.join(root, file)
            zippath = re.sub(s, "", zippath)
            ziph.write(os.path.join(root, file), zippath)

def PatchString(fileName, sourceText, replaceText):
    print ('Патчим '+fileName+'\n')
    file = open(fileName, 'r') #Opens the file in read-mode
    text = file.read() #Reads the file and assigns the value to a variable
    file.close() #Closes the file (read session)
    file = open(fileName, 'w') #Opens the file again, this time in write-mode
    file.write(text.replace(sourceText, replaceText)) #replaces all instances of our keyword
    # and writes the whole output when done, wiping over the old contents of the file
    file.close() #Closes the file (write session)

			
print ('MIUI v7 (Mi3W/4) firmware patcher\n')	
print ('---by mironoff (2015)---\n\n------------------------\n')

path_rom=sys.argv[1]
path_rom_dir=os.path.dirname(path_rom)
if len (sys.argv[1]) > 3:
	#Распаковываем прошивку
	print ("\nРаспаковка прошивки...\n")	
	firmpath = path_rom_dir+'/miui_rom_tmp'
	unzip(path_rom, firmpath)
	
	#Удаляем китайщину
	print ("Немного магии...\n")
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/BrowserProviderProxy.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/BugReport.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/CellBroadcastReceiver.apk')
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
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/NVItem.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/app/PaymentService.apk')
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
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/Weather.apk')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/priv-app/WeatherProvider.apk')

	os.remove(path_rom_dir+'/miui_rom_tmp/system/xbin/su')
	os.remove(path_rom_dir+'/miui_rom_tmp/system/lib/egl/libGLES_android.so')	
	
	#Блобсы
	print ("Грузим blobs...\n")
	url = 'https://github.com/mironoff111/mi4_rom_patcher/blob/master/src/miui_blobs.zip?raw=true'
	urlretrieve(url, path_rom_dir+'/miui_blobs.zip')
	unzip(path_rom_dir+'/miui_blobs.zip', path_rom_dir+'/miui_blobs')
	
	#SuperSu
	shutil.copyfile(path_rom_dir+'/miui_blobs/su', path_rom_dir+'/miui_rom_tmp/system/xbin/su')
	shutil.copyfile(path_rom_dir+'/miui_blobs/Superuser.apk', path_rom_dir+'/miui_rom_tmp/system/app/Superuser.apk')
	#Xperia Keyboard
	shutil.copyfile(path_rom_dir+'/miui_blobs/textinput-tng.apk', path_rom_dir+'/miui_rom_tmp/system/app/textinput-tng.apk')
	shutil.copyfile(path_rom_dir+'/miui_blobs/libswiftkeysdk-java.so', path_rom_dir+'/miui_rom_tmp/system/lib/libswiftkeysdk-java.so')
	#Google VoiceSearch
	shutil.copyfile(path_rom_dir+'/miui_blobs/VoiceSearch.apk', path_rom_dir+'/miui_rom_tmp/system/app/VoiceSearch.apk')	
	
	#Патч ntp 
	PatchString(path_rom_dir+'/miui_rom_tmp/system/etc/gps.conf', 'time.gpsonextra.net', '194.190.168.1')
	#Патч громкости
	PatchString(path_rom_dir+'/miui_rom_tmp/system/etc/mixer_paths_3_2_forte.xml', '<ctl name="TI PA Gain" value="36" />', '<ctl name="TI PA Gain" value="53" />')
	#Патч графики
	PatchString(path_rom_dir+'/miui_rom_tmp/system/lib/egl/egl.cfg', '0 0 android\n', '')
	
	#Эффект телевизора
	unzip(path_rom_dir+'/miui_rom_tmp/system/framework/services.jar', path_rom_dir+'/miui_services_jar')
	os.system("java -jar "+path_rom_dir+"/miui_blobs/baksmali-2.0.6.jar -o "+path_rom_dir+'/miui_services_out/ '+path_rom_dir+'/miui_services_jar/classes.dex')
	PatchString(path_rom_dir+'/miui_services_out/com/android/server/power/DisplayPowerController.smali', 'ELECTRON_BEAM_OFF_ANIMATION_DURATION_MILLIS:I = 0x0', 'ELECTRON_BEAM_OFF_ANIMATION_DURATION_MILLIS:I = 0x190')	
	PatchString(path_rom_dir+'/miui_services_out/com/android/server/power/DisplayPowerController.smali', 'const-wide/16 v1, 0x0', 'const-wide/16 v1, 0x190')
	#Удаляем старый classes.dex
	os.remove(path_rom_dir+'/miui_services_jar/classes.dex')
	#Создаем новый classes.dex
	os.system("java -Xmx128M -jar "+path_rom_dir+"/miui_blobs/smali-2.0.6.jar "+path_rom_dir+'/miui_services_out/ -o '+path_rom_dir+'/miui_services_jar/classes.dex')
	#Архивируем
	zipf = zipfile.ZipFile(path_rom_dir+'/services.jar', 'w')
	zipdir(path_rom_dir+'/miui_services_jar', zipf, "/miui_services_jar")
	zipf.close()
	os.remove(path_rom_dir+'/miui_rom_tmp/system/framework/services.jar')	
	shutil.copyfile(path_rom_dir+'/services.jar', path_rom_dir+'/miui_rom_tmp/system/framework/services.jar')
	
	print ("Архивируем...\n")
	zipf = zipfile.ZipFile(path_rom_dir+'/miui_rom_patched.zip', 'w', mode)
	zipdir(path_rom_dir+'/miui_rom_tmp', zipf, "/miui_rom_tmp")
	zipf.close()
	print ("Прибираемся...\n")
	shutil.rmtree(path_rom_dir+'/miui_rom_tmp')
	shutil.rmtree(path_rom_dir+'/miui_blobs')
	shutil.rmtree(path_rom_dir+'/miui_services_jar')
	shutil.rmtree(path_rom_dir+'/miui_services_out')	
	os.remove(path_rom_dir+'/miui_blobs.zip')
	os.remove(path_rom_dir+'/services.jar')	
	print ("Всё готово!\n")
	sys.exit(0)
else:
    sys.exit("MIUI Firmware isn't specified!")