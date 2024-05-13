#!/data/data/com.termux/files/usr/bin/bash
: "Name: MEMORANDUM (v0.01), Created by: Luis Adha (c) (2024) GNU/GPLv3"
function main() {
  eval "cd ~/storage/downloads"
  eval "libmemorandum-unzip.py $(fd memo.zip | shuf -n1)"
  eval "libmemorandum-parser.py"
}
main;
