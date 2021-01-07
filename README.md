# mypkg

#概要
　ランダムに平面座標系を動く質点のROSパッケージになります.

#動作環境

OS:Ubuntu 20.04.1 LTS

ROS VERSION:1

使用言語:Python3

#使用方法

　mypkg/scripts内の各スクリプトをパーミッションしてください.

`$ chmod +x *.py`

　ROS1の環境を作成し,以下のコマンドを入力します.

`$ roscore`

`$ roslaunch mypkg mypkg.launch`

　ログとしてその時点でのx,y座標が出力されます.

　また,トピックとしてx,yの値が出力されます.以下のコマンドで確認できます.

　xの値 ... 

`$ rostopic echo /xplace`

 yの値 ...

`$ rostopic echo /yplace`

#動作

<>

#ライセンス

　ディレクトリ内のLICENSEに則ります.
