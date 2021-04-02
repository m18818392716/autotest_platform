from appium import webdriver
from androguard.core.bytecodes.apk import APK
import os
import random
apk_path = "您的apk的路径"


def get_devices() -> list:
    all_devices = []
    cmd = "adb devices"
    reslut = os.popen(cmd).readlines()[1:]
    for item in reslut:
        if item != "\n":
            all_devices.append(str(item).split("\t")[0])
    return all_devices


def getPlatForm(dev: str) -> str:
    cmd = 'adb -s {} shell getprop ro.build.version.release'.format(dev)
    reslut = os.popen(cmd).readlines()[0]
    return str(reslut).split("\n")[0]


def get_apkname(apk):
    a = APK(apk, False, "r")
    return a.get_package()


def get_apk_lautc(apk):
    a = APK(apk, False, "r")
    return a.get_main_activity()


def startdevicesApp():
    alldevices=get_devices()
    if len(alldevices)>0:
        for item in alldevices:
            desired_caps = {
                    'platformName': 'Android',
                    'deviceName': item,
                    'platformVersion': getPlatForm(item),
                    'appPackage': get_apkname(apk_path),  # 包名
                    'appActivity': get_apk_lautc(apk_path),  # apk的launcherActivity
                    'skipServerInstallation': True
                }
            port=random.randint(1000,6000)
            driver = webdriver.Remote('http://127.0.0.1:{}/wd/hub'.format(str(port)), desired_caps)
