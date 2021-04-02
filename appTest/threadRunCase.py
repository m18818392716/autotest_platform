from appium import webdriver
from androguard.core.bytecodes.apk import APK
import os
import random
apk_path = "TNAOT_Android_v5.2.0_gtest_20210323_new.apk"


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

import  platform
from multiprocessing import Process,Pool
import time,urllib.request
import threading
class RunServer(threading.Thread):#启动服务的线程
    def __init__(self, cmd):
        threading.Thread.__init__(self)
        self.cmd = cmd
    def run(self):
        os.system(self.cmd)
def start(port_list:list):
    def __run(url):
        time.sleep(10)
        response = urllib.request.urlopen(url, timeout=5)
        if str(response.getcode()).startswith("2"):
            return True
    for i in range(0, len(port_list)):
        cmd = "appium  -p %s  " % (
            port_list[i])
        if platform.system() == "Windows":  # windows下启动server
            t1 =RunServer(cmd)
            p = Process(target=t1.start())
            p.start()
            while True:
                time.sleep(4)
                if __run("http://127.0.0.1:" + port_list[i]+ "/wd/hub/status"):
                    break

def startdevicesApp():
    l_devices_list=[]
    port_list=[]
    alldevices=get_devices()
    if len(alldevices)>0:
        for item in alldevices:
            port=random.randint(1000,6000)
            port_list.append(port)
            desired_caps = {
                    'platformName': 'Android',
                    'deviceName': item,
                    'platformVersion': getPlatForm(item),
                    'appPackage': get_apkname(apk_path),  # 包名
                    'appActivity': get_apk_lautc(apk_path),  # apk的launcherActivity
                    'skipServerInstallation': True,
                "port":port
                }
            l_devices_list.append(desired_caps)
    return  l_devices_list,port_list

def runcase(devics):
    #执行测试用例
    pass
def run(deviceslist:list):
    pool = Pool(len(deviceslist))
    for devices in deviceslist:
        pool.map(runcase, devices)
    pool.close()
    pool.join()
if  __name__=="__main__":
    l_devices_list,port_list=startdevicesApp()
    start(port_list)
    run(l_devices_list)