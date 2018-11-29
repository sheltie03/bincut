# Binary Cutter
Binary Cutter v0.0.1 by Aki

## 1. Installation

```
$ git clone https://github.com/sheltie03/bincut/
$ cd bincut
$ sudo python setup.py install
```

## 2. Usage

```
$ bincut -h
usage: bincut [-h] [-b BYTES] TARGET

Binary Cutter v0.0.1 by GONDA, Akihiko

positional arguments:
  TARGET                a target binary file

optional arguments:
  -h, --help            show this help message and exit
  -b BYTES, --bytes BYTES
                        split the target by bytes list
```


## 3. Sample
### 3.1 Get address by Binwalk

```
$ binwalk ./sample/raw.dat

DECIMAL       HEXADECIMAL     DESCRIPTION
--------------------------------------------------------------------------------
102           0x66            PNG image, 266 x 36, 8-bit/color RGB, non-interlaced
195           0xC3            Zlib compressed data, default compression
2296          0x8F8           PNG image, 260 x 28, 8-bit/color RGB, non-interlaced
2389          0x955           Zlib compressed data, default compression
4920          0x1338          PNG image, 242 x 28, 8-bit/color RGB, non-interlaced
5013          0x1395          Zlib compressed data, default compression

```

### 3.2 Split by Bincut

```
$ bincut --bytes 0x66,0x8F8,0x1338 raw.dat
$ ls
0  1  2  3  raw.dat
```


## 4. Another
### 4.1 Split by Foremost

```
$ foremost raw.dat
Processing: raw.dat
|*|
$ ls ./output/png/
00000000.png  00000004.png  00000009.png
```
