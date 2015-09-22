#JRE REQUIRED!!!
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
            s=rom_dir+secret
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
rom_dir=os.path.dirname(path_rom)
if len (sys.argv[1]) > 3:
	#Распаковываем прошивку
	print ("\nРаспаковка прошивки...\n")	
	unzip(path_rom, rom_dir+'/miui_rom_tmp')
	
	#Удаляем китайщину
	print ("Немного магии...\n")
	os.remove(rom_dir+'/miui_rom_tmp/system/app/BrowserProviderProxy.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/fastdormancy.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/app/BugReport.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/CellBroadcastReceiver.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/CloudService.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/Email.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/GoogleCalendarSyncAdapter.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/GoogleContactsSyncAdapter.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/GoogleKeyboard.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/KingSoftCleaner.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/LiveWallpapersPicker.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/MiAssistant.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/MiLinkService.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/MiWallpaper.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/NVItem.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/PaymentService.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/qcrilmsgtunnel.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/app/TSMClient.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/XiaomiServiceFramework.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/app/XiaomiVip.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/app/PicoTts.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/BarcodeScanner.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/Browser.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/CleanMaster.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/CloudBackup.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/com.qualcomm.location.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/com.qualcomm.msapm.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/GoogleBackupTransport.apk')	
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/MiuiVoip.apk')		
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/Weather.apk')
	os.remove(rom_dir+'/miui_rom_tmp/system/priv-app/WeatherProvider.apk')

	os.remove(rom_dir+'/miui_rom_tmp/system/xbin/su')
	os.remove(rom_dir+'/miui_rom_tmp/system/lib/egl/libGLES_android.so')	
	
	os.remove(rom_dir+'/miui_rom_tmp/system/media/theme/default/gadgets/weather_4x1.mtz')
	os.remove(rom_dir+'/miui_rom_tmp/system/media/theme/default/gadgets/weather_4x4.mtz')
	os.remove(rom_dir+'/miui_rom_tmp/system/media/theme/default/gadgets/weather_clock.mtz')	

	shutil.rmtree(rom_dir+'/miui_rom_tmp/system/tts')	
	
	#Блобсы
	print ("Грузим blobs...\n")
	url = 'https://raw.githubusercontent.com/mironoff111/mi4_rom_patcher/master/src/miui_blobs.zip'
	urlretrieve(url, rom_dir+'/miui_blobs.zip')
	unzip(rom_dir+'/miui_blobs.zip', rom_dir+'/miui_blobs')
	
	#SuperSu
	shutil.copyfile(rom_dir+'/miui_blobs/su', rom_dir+'/miui_rom_tmp/system/xbin/su')
	shutil.copyfile(rom_dir+'/miui_blobs/Superuser.apk', rom_dir+'/miui_rom_tmp/system/app/Superuser.apk')
	
	#Xperia Keyboard
	shutil.copyfile(rom_dir+'/miui_blobs/textinput-tng.apk', rom_dir+'/miui_rom_tmp/system/app/textinput-tng.apk')
	shutil.copyfile(rom_dir+'/miui_blobs/libswiftkeysdk-java.so', rom_dir+'/miui_rom_tmp/system/lib/libswiftkeysdk-java.so')
	
	#Google VoiceSearch
	shutil.copyfile(rom_dir+'/miui_blobs/VoiceSearch.apk', rom_dir+'/miui_rom_tmp/system/app/VoiceSearch.apk')	
	shutil.copyfile(rom_dir+'/miui_blobs/libvoicesearch.so', rom_dir+'/miui_rom_tmp/system/lib/libvoicesearch.so')
	
	#Патч ntp 
	PatchString(rom_dir+'/miui_rom_tmp/system/etc/gps.conf', 'time.gpsonextra.net', '194.190.168.1')
	
	#Патч громкости
	PatchString(rom_dir+'/miui_rom_tmp/system/etc/mixer_paths_3_2_forte.xml', '<ctl name="TI PA Gain" value="36" />', '<ctl name="TI PA Gain" value="53" />')
	
	#Патч графики
	PatchString(rom_dir+'/miui_rom_tmp/system/lib/egl/egl.cfg', '0 0 android\n', '')
	
	#Расширенное меню перезагрузки
	shutil.copyfile(rom_dir+'/miui_blobs/powermenu', rom_dir+'/miui_rom_tmp/system/media/theme/default/powermenu')	
	unzip(rom_dir+'/miui_rom_tmp/system/framework/android.policy.jar', rom_dir+'/miui_policy_jar')	
	os.system("java -jar "+rom_dir+"/miui_blobs/baksmali-2.0.6.jar -o "+rom_dir+'/miui_policy_out/ '+rom_dir+'/miui_policy_jar/classes.dex')	
	shutil.copyfile(rom_dir+'/miui_blobs/MiuiGlobalActions$1.smali', rom_dir+'/miui_policy_out/com/android/internal/policy/impl/MiuiGlobalActions$1.smali')	
	#Удаляем старый classes.dex
	os.remove(rom_dir+'/miui_policy_jar/classes.dex')
	#Создаем новый classes.dex
	os.system("java -Xmx128M -jar "+rom_dir+"/miui_blobs/smali-2.0.6.jar "+rom_dir+'/miui_policy_out/ -o '+rom_dir+'/miui_policy_jar/classes.dex')
	#Архивируем
	zipf = zipfile.ZipFile(rom_dir+'/android.policy.jar', 'w')
	zipdir(rom_dir+'/miui_policy_jar', zipf, "/miui_policy_jar")
	zipf.close()	
	shutil.copyfile(rom_dir+'/android.policy.jar', rom_dir+'/miui_rom_tmp/system/framework/android.policy.jar')
	
	#Эффект телевизора
	unzip(rom_dir+'/miui_rom_tmp/system/framework/services.jar', rom_dir+'/miui_services_jar')
	os.system("java -jar "+rom_dir+"/miui_blobs/baksmali-2.0.6.jar -o "+rom_dir+'/miui_services_out/ '+rom_dir+'/miui_services_jar/classes.dex')
	PatchString(rom_dir+'/miui_services_out/com/android/server/power/DisplayPowerController.smali', 'ELECTRON_BEAM_OFF_ANIMATION_DURATION_MILLIS:I = 0x0', 'ELECTRON_BEAM_OFF_ANIMATION_DURATION_MILLIS:I = 0x190')	
	PatchString(rom_dir+'/miui_services_out/com/android/server/power/DisplayPowerController.smali', 'const-wide/16 v1, 0x0', 'const-wide/16 v1, 0x190')
	#Удаляем старый classes.dex
	os.remove(rom_dir+'/miui_services_jar/classes.dex')
	#Создаем новый classes.dex
	os.system("java -Xmx128M -jar "+rom_dir+"/miui_blobs/smali-2.0.6.jar "+rom_dir+'/miui_services_out/ -o '+rom_dir+'/miui_services_jar/classes.dex')
	#Архивируем
	zipf = zipfile.ZipFile(rom_dir+'/services.jar', 'w')
	zipdir(rom_dir+'/miui_services_jar', zipf, "/miui_services_jar")
	zipf.close()	
	shutil.copyfile(rom_dir+'/services.jar', rom_dir+'/miui_rom_tmp/system/framework/services.jar')
	
	#Архивируем прошику
	name = os.path.basename(path_rom)
	name = name.replace("miuisu", "admort")
	zipf = zipfile.ZipFile(rom_dir+'/'+name, 'w', mode)
	zipdir(rom_dir+'/miui_rom_tmp', zipf, "/miui_rom_tmp")
	zipf.close()
	
	#Подписываем прошивку
	print ("Подписываем прошивку...\n")
	os.system("java -Xmx256M -jar "+rom_dir+"/miui_blobs/s.jar "+rom_dir+"/miui_blobs/testkey.x509.pem "+rom_dir+"/miui_blobs/testkey.pk8 "+rom_dir+'/'+name+' '+rom_dir+'/'+"signed_"+name)
	
	#Прибираемся	
	print ("Прибираемся...\n")
	shutil.rmtree(rom_dir+'/miui_rom_tmp')
	shutil.rmtree(rom_dir+'/miui_blobs')
	shutil.rmtree(rom_dir+'/miui_services_jar')
	shutil.rmtree(rom_dir+'/miui_services_out')	
	os.remove(rom_dir+'/miui_blobs.zip')
	os.remove(rom_dir+'/services.jar')	
	os.remove(path_rom)
	os.remove(rom_dir+'/'+name)
	print ("Всё готово!\n")
	sys.exit(0)
else:
    sys.exit("MIUI Firmware isn't specified!")