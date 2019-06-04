import glob
import os
import json


#   jq '. | map(select( .user.screen_name == "paseri_Hades")) | .[] | { text: .text, id: .id_str }' log/convert.json
if __name__ == '__main__':
    convert = {}
    for file_path in sorted(glob.glob('./log/2019*.json'), reverse=True):
        with open(file_path) as f:
        	data = json.load(f)
        	appneds = [
        	    tweet for tweet in data['statuses'] 
        	    if not tweet['text'].startswith('RT ') 
        	    and not 'bot' in tweet['user']['screen_name'] 
        	    and tweet['id_str'] not in convert
        	]
        	
        	convert.update({ item['id_str']: item for item in appneds})
        	
    save_path = './log/convert.json'
    if os.path.isfile(save_path):
        os.remove(save_path)    
    with open(save_path, 'a') as f:
        json.dump(list(convert.values()), f, indent=4, ensure_ascii=False, )
        	