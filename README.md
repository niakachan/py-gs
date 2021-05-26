# python-gs

Python からスプレッドシートを操作するテスト用のアプリ。
開発テスト用であり実用的な何かではありません。

## Example for .env

環境変数設定のために`.env`を用意してください。

```env
# .jsonを除いたキーファイルの名前
GOOGLE_JSON_KEY="{filename}"
# キーファイルが保存されているディレクトリ
SECRETS_DIRECTORY="./secrets"
```

`SECRETS_DIRECTORY`を変更した場合は`.gitignore`の書き換えを忘れずに

## 参考 URL

このリポジトリは以下の資料を参考にして作られています。

- [【もう迷わない】Python でスプレッドシートに読み書きする初期設定まとめ](https://tanuhack.com/operate-spreadsheet/)
- [gspread ライブラリの使い方まとめ！Python でスプレッドシートを操作する](https://tanuhack.com/library-gspread/)
