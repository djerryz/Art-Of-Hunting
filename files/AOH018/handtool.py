#https://mp.weixin.qq.com/s/pBkJW1_Vpf_suH50e8K9kg

import requests
import json
requests.packages.urllib3.disable_warnings()


url = "https://projects.registry.vmware.com/"

# test old version
r = requests.get(url + "/api/search?q=",headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
}, allow_redirects=False, verify=False, timeout=20)
try:
    print(json.dumps(r.json(), indent=4))
except:
    pass

# test new version
all_ = {}
for i in "-.abcdefghijklmnopqrstuvwxyz":
    print("current check:", i)
    r = requests.get(url + "/api/v2.0/search?q={}".format(i),headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36"
    }, allow_redirects=False, verify=False, timeout=20, )
    _this = r.json()["repository"]
    
    print(json.dumps(_this, indent=4))
    for repo in _this:
        all_[repo["repository_name"]] = repo
print(json.dumps(all_, indent=4))

# to do: collect sha256 to dict object
# proxies={"https":"http://127.0.0.1:1080"}