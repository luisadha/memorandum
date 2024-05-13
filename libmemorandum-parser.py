#!/data/data/com.termux/files/usr/bin/python3
# "Name: LIBMEMORANDUM-PARSER (v0.01), Created by: Luis Adha (c) (2024) GNU/GPLv3"
import os
from bs4 import BeautifulSoup
import xml.sax.saxutils as saxutils
import subprocess
import glob
import sys
import shutil

home_dir = os.getcwd() # Sama seperti pwd
memo_files = glob.glob("*.memo") # Mencari pola file dengan ektensi .memo

# Merename semua file dengan ektensi .memo ke .zip
for memo_file in memo_files:
    zip_file = memo_file.replace('.memo', '.memo.zip')
    shutil.move(memo_file, zip_file)
    print(f"File '{memo_file}' berhasil diubah menjadi '{zip_file}'")

subprocess.run(['fd', 'memo'], stdout=subprocess.DEVNULL) # print menampilkan file dengan ektensi .memo.zip

xml_file_path = os.path.join(home_dir, "memo_content.xml") # Jalur beserta nama filenya

with open(xml_file_path, 'r') as file:
    xml_content = file.read() # Membaca file xml

# Mengonversi karakter khusus XML ke karakter biasa
xml_content_unescaped = saxutils.unescape(xml_content, entities={})

# Membuat objek BeautifulSoup
soup = BeautifulSoup(xml_content_unescaped, 'xml')
# Mendapatkan teks dari seluruh dokumen dengan karakter baris baru sebagai pemisah
plain_text = soup.get_text(separator='\n')
# Hasil akhir program
print(f"Body of your memo:", plain_text) # Membuat format yang mudah dibaca atau plain text
