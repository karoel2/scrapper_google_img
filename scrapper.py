import os
cmd = 'node google_img_scrp.js'
os.system(cmd)


import json
f = open('data.json', encoding='UTF-8')
data = json.load(f)
for idx, item in enumerate(data):
    os.system("curl "+ str(item["url"]) + " > data/image_{idx}.jpg")
f.close()
