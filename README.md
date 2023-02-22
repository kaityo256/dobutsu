# どうぶつ将棋の棋譜コードサンプル

* マスの情報
	* 0 空白
	* 1 ライオン(先手) L
	* 2 ぞう(先手) E
	* 3 きりん(先手) G
	* 4 ひよこ(先手) C
	* 5 にわとり(先手) H
	* 6 ライオン(後手) l
	* 7 ぞう(後手) e 
	* 8 きりん(後手) g
	* 9 ひよこ(後手) c
	* 10 にわとり(後手) l

* 持ち駒 (ライオンとニワトリは持ち駒にならず、2つまで取る可能性がある)
* 例えば`captured[0]`は、先手が何個「ぞう」を持っているかの数を表す
	* 0 ぞう (先手の持ち駒)
	* 1 きりん (先手の持ち駒)
	* 2 ひよこ (先手の持ち駒)
	* 3 ぞう (後手の持ち駒)
	* 4 きりん (後手の持ち駒)
	* 5 ひよこ (後手の持ち駒)

## Usage

使い方

```sh
$ python3 dobutsu.py
[]
-------
|g|l|e|
-------
| |c| |
-------
| |C| |
-------
|E|L|G|
-------
[]

[eg]
-------
| |H|l|
-------
| | | |
-------
|E| | |
-------
| |L| |
-------
[GC]
```

## LICENSE

MIT