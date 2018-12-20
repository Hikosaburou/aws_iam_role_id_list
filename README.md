# aws_iam_role_id_list
IAM Roleと aws:userid を一覧で表示するやつ


# Install

```
pip install -e .
```

# Usage

あらかじめ環境変数を設定する。[Direnv](https://direnv.net/) 推奨

```
export AWS_ACCESS_KEY_ID=xxxxxxxxxxxxxxxxxxx
export AWS_SECRET_ACCESS_KEY=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

以下の通りコマンドを実行する。

```
$ iamrolelist
| RoleName              | RoleId                                                           |
|:----------------------|:-----------------------------------------------------------------|
| AROXXXXXXXXXXXXXXXXXX | RoleNameXXXXXX                                                   |
...
```
