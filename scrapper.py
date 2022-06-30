import argparse

parser = argparse.ArgumentParser(
    description='Download bulk of images from Google Images ')
parser.add_argument('querry', metavar='QUERRY', type=str,
                    help='Google Image querry')
parser.add_argument('amount', metavar='AMOUNT', type=int,
                    help='amount of images to download')

args = parser.parse_args()
print(args)
querry = args.querry
amount = args.amount

import os
cmd = f'node google_img_scrp.js {querry} {amount}'
os.system(cmd)

import json
f = open('data.json', encoding='UTF-8')
data = json.load(f)
for idx, item in enumerate(data):
    os.system(f'curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --output data/image_{idx}.jpg ' + str(item["url"]))
f.close()
