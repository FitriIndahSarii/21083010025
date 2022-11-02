#!/bin/bash

# Mendeklarasikan fungsi
panjang() {
     echo "Masukkan Panjang :"
     read panjang
}
lebar() {
     echo "Masukkan Lebar :"
     read lebar
}
luas() {
     let luas=$panjang*$lebar
     echo "Luas Persegi :"
     echo $luas
}

#Memanggil fungsi
panjang
lebar
luas
