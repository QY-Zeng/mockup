# Dynamic Mockup Server

## 如何使用
  - 下載後，移動到對應資料夾後，輸入python app.py 即可使用mockup server，然後url可以看說執行python app.py後跑出來的資訊，有一個會是自己電腦的ip，另外一個是http://127.0.0.1:5000 ，不過想要用手機連線的話要連電腦的ip的那一個，然後手機跟電腦要連同一個網路，另外一個http://127.0.0.1:5000 的用手機的app就連線不到了，但是用筆電的是都可以。

## 參考的mockup server 
  - Simple Rack-mounted Server
    - A typical 1U or 2U server intended for scale-out deployments.  
    - https://redfish.dmtf.org/redfish/mockups/v1/1819
    - 但是目前還缺不少分支


## 目前有的分支(還未寫完這邊的readme)(ok代表目前有寫、not是還沒寫)
  - redfish/v1
    - redfish/v1/Systems (ok)
      - redfish/v1/Systems/System1 (ok)
        - /redfish/v1/Systems/System1/Bios (not)
          - /redfish/v1/Systems/System1/Bios/Settings (not)
        - /redfish/v1/Systems/System1/SecureBoot (not)
        - /redfish/v1/Systems/System1/Processors (ok)
          - /redfish/v1/Systems/System1/Processors/CPU1 (ok)
        - /redfish/v1/Systems/System1/Memory (ok)
          - /redfish/v1/Systems/System1/Memory/DIMM1 (ok) 
          - /redfish/v1/Systems/System1/Memory/DIMM2 (ok)
        - /redfish/v1/Systems/System1/EthernetInterfaces (not)
        - /redfish/v1/Systems/System1/SimpleStorage (not)
        - /redfish/v1/Systems/System1/GraphicsControllers (not)
        - /redfish/v1/Systems/System1/USBControllers (not)
        - /redfish/v1/Systems/System1/Certificates (not)
        - /redfish/v1/Systems/System1/VirtualMedia (not)
        - /redfish/v1/Systems/System1/LogServices (ok)
    - redfish/v1/Chassis (ok)
      - /redfish/v1/Chassis/Chassis1 (ok)
        - /redfish/v1/Chassis/Chassis1/Thermal (ok)
        - /redfish/v1/Chassis/Chassis1/Power (ok)
        - /redfish/v1/Chassis/Chassis1/Sensors (ok)
        - /redfish/v1/Chassis/Chassis1/ThermalSubsystem (not)
        - /redfish/v1/Chassis/Chassis1/PowerSubsystem (not)
        - /redfish/v1/Chassis/Chassis1/EnvironmentMetrics (not)
        - /redfish/v1/Chassis/Chassis1/Controls (not)
        - /redfish/v1/Chassis/Chassis1/TrustedComponents (not)
    - redfish/v1/Managers (ok)
        - /redfish/v1/Managers/BMC
        - /redfish/v1/Managers/BMC/LogServices
          - /redfish/v1/Managers/BMC/LogServices/EventLog
            - /redfish/v1/Managers/BMC/LogServices/EventLog/Entries
        - /redfish/v1/Managers/BMC/EthernetInterfaces
          - /redfish/v1/Managers/BMC/EthernetInterfaces/eth0

## 功能
 - Simulator 會讓 CPU Usage 自動波動，不是一個固定值
 - CPU Temperature 變化，會根據CPU Utilization、Fan RPM 動態改變
 - Fan PWM 自動調速，會根據CPU溫度而改變轉速
 - System Power 變化
 - PSU Input/Output Power會跟系統耗電同步
 - Fan Failure(Recovery) 風扇失效(恢復)後Fan RPM = 0(跟溫度有關)，同時：Fan failure detected(Fan Recover)寫進 Event Log
 - Thermal Shutdown 當cpu_temp > 100 會：system.power_state = "Off" 並產生：Thermal shutdown triggered
 - Power Off Cooling 系統關機後：CPU 溫度會自動下降
 - System Health 自動變化
 - Event Log 自動產生，會自動記錄一些事件的發生


# 接下來要做的事情
  - 把前面的分支補完
  - 然後看教授的建議有什麼，後面的評分有一部份會根據這邊的東西
  - 7/1 有pre-domo(根據這邊的東西去做評分)
    - Slides(or design document)
    - Preliminary-Demo or Analysis
    - Review meeting and Suggestion















