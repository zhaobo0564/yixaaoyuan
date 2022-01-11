import requests
import setting



def DoDetail(json, name):
     # 输入打卡信息
    data = json
    # 添加打卡信息
    data['address'] = setting.ADDRESS
    # 填写Tokan信息
    data['uuToken'] = setting.UNTOKEN[name]
    # 填写Userid
    data['loginUserId'] = setting.USER_ID[name]
    # 填写学校id
    data['loginSchoolCode'] = setting.LOGINSCHOOLCODE
    # 填写学校名称
    data['loginSchoolName'] = setting.LOGINSCHOOLNAME
    # 填写体温信息
    data['temperature'] = setting.TEMPERATURE
    # 打卡地址
   # data['locationInfo'] = setting.LOCATIONINFO
    # 经纬度
   # data['longitudeAndLatitude'] = setting.LONGITUDEANDLATITUDE
    
    requests.packages.urllib3.disable_warnings()
    #请求易校园接口
    response = requests.post("https://h5.xiaofubao.com/marketing/health/doDetail",headers=headers,data=data,verify=False)
    print(name + ": ")
    print(response.json())

    #获取userid 
def GetDetail(userid):
    data1 = {'userId':userid}
    requests.packages.urllib3.disable_warnings()
    response = requests.post("https://h5.xiaofubao.com/marketing/health/getDetail",headers=headers,data=data1,verify=False)
    return response.json()
    
    #伪造请求头
if __name__ == '__main__':
    headers = {'User-Agent':'Mozilla/5.0 (Linux; Android 10; LRA-AL00 Build/HONORLRA-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/83.0.4103.106 Mobile Safari/537.36 Html5Plus/1.0 (Immersed/26.0) ZJYXYwebviewbroswer ZJYXYAndroid tourCustomer /yunmaapp.NET/2.2.3/yunma6c73a2ed-6791-4c24-92f2-64c4530509fb',
               'Cookie':'shiroJID=c62ef8b2-42e9-4d81-a172-fd3867c15da4'}
      # 填写Userid
    #print(setting.USER_ID)
    for it in setting.USER_ID:
        json = GetDetail(setting.USER_ID[it])
        print(json)
        if(json['success']==True):
            DoDetail(json['data'], it)

