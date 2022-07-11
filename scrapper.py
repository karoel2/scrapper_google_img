import argparse

parser = argparse.ArgumentParser(
    description='Download bulk of images from Google Images ')
parser.add_argument('querry', metavar='QUERRY', type=str,
                    help='Google Image querry')
parser.add_argument('amount', metavar='AMOUNT', type=int,
                    help='amount of images to download')
parser.add_argument('-o', '--output', metavar='OUTPUT', type=str,
                    help='output dir', default='data')




args = parser.parse_args()
print(args)
querry = args.querry
amount = args.amount
out = args.output
import os
cmd = f'node google_img_scrp.js {querry} {amount}'
os.system(cmd)
os.system(f'mkdir {out}')
import json
f = open('data.json', encoding='UTF-8')
data = json.load(f)
for idx, item in enumerate(data):
    os.system(f'curl -A "Mozilla/5.0 (X11; Linux x86_64; rv:60.0) Gecko/20100101 Firefox/81.0" --output {out}/image_{idx}.jpg ' + str(item["url"]))
f.close()
