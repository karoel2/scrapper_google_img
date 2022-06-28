import os
cmd = 'node google_img_scrp.js'
os.system(cmd)

# #to na windowsie
#
# # a to na linuxie
# import json
#
# # Opening JSON file
# f = open('data.json', encoding='UTF-8')
#
# # returns JSON object as
# # a dictionary
# data = json.load(f)
#
# # Iterating through the json
# # list
# for idx, item in enumerate(data):
#     # print(item['url'])
#     # break
#     os.system("curl "+ str(item["url"]) + " > data/image_{idx}.jpg")
#     # print(['url'])
# # Closing file
# f.close()
