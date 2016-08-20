#!/usr/bin/env python
#coding=utf8
 
import urllib2
import json
import os
 
page = 1
token = raw_input("输入账户token,如果没有token请到https://github.com/settings/tokens设置: ");
dir = raw_input("请输入文件夹");
cloneUrls = []
existDir = []
if os.path.exists(dir):
    for d in os.listdir(dir):
        path = os.path.join(dir, d)
        if os.path.isdir(path):
            existDir.append(d)
else :
    os.makedirs(dir)
while True :
    url = "https://api.github.com/user/starred?per_page=2000&access_token=" + token + "&page="+str(page);

    try:
        f = urllib2.urlopen(url)
        buf = f.read()
        f.close()
        repos = json.loads(buf)
        if len(repos) == 0:
            break
        else:
            for repo in repos:
                cloneUrl = repo["clone_url"]
                repoName = repo["name"]
                if repoName not in existDir:
                    cloneUrls.append(repo["clone_url"])
                    print repoName
            page = page + 1
    except Exception, e:
        print e

for cloneUrl in cloneUrls:
    os.system("cd " + dir +";git clone " + cloneUrl);
