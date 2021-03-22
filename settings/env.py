"""
.envに設定された環境を読む
"""
import os
from dotenv import load_dotenv
import dotenv


# .envをロード
dotenv_path = dotenv.find_dotenv()
load_dotenv(dotenv_path, verbose=True)

# GOOGLE_JSON_KEY を置いとくディレクトリ
JSON_KEY_DIRECTORY = os.environ.get('SECRETS_DIRECTORY')

# .envからの読み込み項目設定
GOOGLE_JSON_KEY = '{0}/{1}.json'.format(JSON_KEY_DIRECTORY, os.environ.get('GOOGLE_JSON_KEY'))
BOOK_ID = os.environ.get('BOOK_ID')
