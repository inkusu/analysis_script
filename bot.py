import urllib.parse
import urllib.error
import json
import subprocess
from time import sleep
from datetime import datetime

BASE_SAVE_PATH = './'


def res_cmd(cmd):
    print('twurlコマンドの実行: {0}'.format(cmd))
    return subprocess.Popen(
        cmd, stdout=subprocess.PIPE,
        shell=True).communicate()[0]


SLEEP_TIME = 0.1


def main():
    count = 1
    max_id = 0

    while True:
        print('----------------------------------------------------')
        request = 'twurl "/1.1/search/tweets.json?q=%e3%82%ad%e3%83%83%e3%83%88%e3%82%ab%e3%83%83%e3%83%88&lang=ja&locale=ja&count=100&result_type=recent&max_id={0}"'
        write_data = json.loads(res_cmd(request.format(max_id)))
        max_id = urllib.parse.parse_qs(write_data['search_metadata']['next_results'])['?max_id'][0]

        time = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
        print('{0}回目 - {1}'.format(count, time))
        print('{0}秒間隔でデータを取得します。'.format(SLEEP_TIME))
        print('終了するにはコントロールキーで')
        with open('./log/{0}.json'.format(time), 'w') as f:
            json.dump(write_data,f , indent=4, ensure_ascii=False, )

        count = count + 1
        sleep(SLEEP_TIME)


if __name__ == "__main__":
    main()
