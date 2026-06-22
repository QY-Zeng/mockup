"""
service_root.py 
    它只負責這個 API：GET /redfish/v1 也就是 Redfish 的入口。  
    Client 第一次連進來一定會先查：GET /redfish/v1 
    然後從這裡找到：Systems、Chassis、Managers、SessionService、UpdateService在哪裡。


06/22 今天把一些東西補上去，然後修改了排序，原本是用英文首字母的順序排序，把她修改成說是用原本的樣子
然後目前還缺少TaskService、SectionService、AccountService、EventService、Registries、UpdateService、
CertificateService、KeyService、ServiceConditions、ComponentIntegrity
目前還缺少很多東，但是主要的3個都有了
    
"""

from flask import Blueprint
from flask import jsonify

# Blueprint(...) -> 建立 Flask Blueprint。可以理解成：一組 API 的集合

bp = Blueprint(
    "service_root",
    __name__
) #這個 Blueprint 專門管理 Service Root


@bp.route("/redfish/v1", methods=["GET"])  #當收到 GET /redfish/v1時執行下面的函式
def service_root():
    #return jsonify 自動回傳 JSON。
    return jsonify({

        "@odata.type":"#ServiceRoot.v1_15_0.ServiceRoot",
        
        "Id":"RootService",
        
        "Name":"Root Service",

        "RedfishVersion":"1.15.0",

        "UUID":"92384634-2938-2342-8820-489239905423",
        "ProtocolFeaturesSupported":{
            "ExpandQuery": {
                "ExpandAll": True,
                "Levels": True,
                "MaxLevels": 6,
                "Links": True,
                "NoLinks": True} ,
            "SelectQuery": False,
            "FilterQuery": False,
            "OnlyMemberQuery": True,
            "ExcerptQuery": True
        } ,

        "Systems": {
            "@odata.id":"/redfish/v1/Systems"
        },
        
        "Chassis": {
            "@odata.id":"/redfish/v1/Chassis"
        },

        "Managers": {
            "@odata.id":"/redfish/v1/Managers"
        },

        "@odata.id":"/redfish/v1"
        
        
    })
