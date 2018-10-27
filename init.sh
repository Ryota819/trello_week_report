#!/bin/bash
SCRIPT_DIR=$(cd $(dirname $0); pwd)
echo ${SCRIPT_DIR}

echo "トレロAPIを取得します。"
echo "https://trello.com/app-key にアクセスしてください"
echo "キーを入力してください"
read appkey

echo "https://trello.com/1/authorize?key=${appkey}&name=&expiration=never&response_type=token&scope=read,write にアクセスしてください"
echo "トークンを入力してください"
read token
{
echo "[py-trello]"
echo "api=${appkey}"
echo "token=${token}"
} > ${SCRIPT_DIR}/config.ini

rtn=`curl --request GET \
  --url "https://api.trello.com/1/search?query=query&key=${appkey}&token=${token}" \
  -o /dev/null -w '%{http_code}\n' -s`

if [ ${rtn} -eq 200 ] ; then
	echo "完了です。"
else
	echo "認証がうまくいきませんでした。もう一度やり直してください。"
	rm -r ${SCRIPT_DIR}/config.ini
fi
python 
