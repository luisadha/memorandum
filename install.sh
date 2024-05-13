#!/data/data/com.termux/files/usr/bin/bash

function _install() {
local scripts="$1" dest="$2"

  install ./"$scripts" /data/data/com.termux/files/home/.local/bin/"$scripts"
  chmod +x ./"$scripts" /data/data/com.termux/files/home/.local/bin/"$scripts"

}

_install memorandum.sh
_install libmemorandum-parser.py
_install libmemorandum-unzip.py
