from appium import webdriver
from androguard.core.bytecodes.apk import APK
import os

desired_caps = {
                'platformName': 'Android',
                'deviceName': 'Google Nexus 6',#adb  deivces
                'platformVersion': '7', #从设置中可以获取
                'appPackage': 'com.tnaot.newspro',#包名
                'appActivity': 'com.tnaot.news.mctnews.detail.activity.MainActivity' # apk的launcherActivity
                }

# 获取app的包名
def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()
# 获取APP的启动activity
def get_apk_lautc(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()
# 获取deviceName
def get_devices():
    cmd="adb devices"
    reslut=os.popen(cmd).readlines()
    print(reslut)

def get_devices1():
    cmd="adb devices"
    reslut = os.popen(cmd).readlines()[2:]
    for item in reslut:
        if item != "\n":
            return str(item).split("\t")[0]
# 获取plafFormName
def getPlatForm():
    cmd='adb shell getprop ro.build.version.release'
    result = os.popen(cmd).readlines()[0]
    print(str(result))
    print(str(result).split("\n")[0])

if  __name__=="__main__":
    apkname = get_apkname(r"TNAOT_Android_v5.2.0_gtest_20210323_new.apk")
    apk_lautc = get_apk_lautc(r"TNAOT_Android_v5.2.0_gtest_20210323_new.apk")
    print(apkname)
    print(apk_lautc)
    get_devices()
    rselut = get_devices1()
    print(rselut)
    getPlatForm()
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)