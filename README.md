# Dynamic Mockup Server

## 如何使用
  - 下載後，移動到對應資料夾後，輸入python app.py 即可使用mockup server，然後url可以看說執行python app.py後跑出來的資訊，有一個會是自己電腦的ip，另外一個是http://127.0.0.1:5000 ，不過想要用手機連線的話要連電腦的ip的那一個，然後手機跟電腦要連同一個網路，另外一個http://127.0.0.1:5000 的用手機的app就連線不到了，但是用筆電的是都可以。

## 參考的mockup server 
  - Simple Rack-mounted Server
    - A typical 1U or 2U server intended for scale-out deployments.  
    - https://redfish.dmtf.org/redfish/mockups/v1/1819
    - 但是目前還缺不少分支


## 目前有的分支(還未寫完這邊的readme)
  - redfish/v1
    - redfish/v1/Systems (ok)
      - redfish/v1/Systems/System1 (ok)
        - /redfish/v1/Systems/System1/Bios (not)
        - /redfish/v1/Systems/System1/SecureBoot (not)
        - /redfish/v1/Systems/System1/Processors (ok)
          - /redfish/v1/Systems/System1/Processors/CPU1 (ok)
        - /redfish/v1/Systems/System1/Memory (ok)
          - /redfish/v1/Systems/System1/Memory/DIMM1 (ok) 
          - /redfish/v1/Systems/System1/Memory/DIMM2 (ok)
        - /redfish/v1/Systems/System1/EthernetInterfaces (not)    
    - redfish/v1/Chassis
    - redfish/v1/Managers






















