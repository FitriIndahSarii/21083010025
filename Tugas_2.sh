printf "Operasi apa yang ingin kamu lakukan?\n"
printf "pengurangan?\n"
printf "penjumlahan?\n"
printf "mod?\n"
printf "perkalian?\n"
printf "pembagian?\n"

read operasi_mtk
printf "Operasi yang akan saya lakukan adalah operasi $operasi_mtk\n"

printf "angka pertama?\n"
read x
printf "angka pertama adalah $x\n"
printf "angka kedua?\n"
read y
printf "angka kedua adalah $y\n"

let kurang=$x-$y
let jumlah=$x+$y
mod=$(($x % $y))
let kali=$x*$y
bagi=`expr $x / $y`

case "$operasi_mtk" in
  "pengurangan")
  echo "Pengurangan $x dengan $y adalah $kurang"
  ;;
  "penjumlahan")
  echo "Penjumlahan $x dengan $y adalah $jumlah"
  ;;
  "mod")
  echo "Mod $x dengan $y adalah $mod"
  ;;
  "perkalian")
  echo "Perkalian $x dengan $y adalah $kali"
  ;;
  "pembagian")
  echo "Pembagian $x dengan $y adalah $bagi"
  ;;
  *)
   echo "Operasi yang kamu pilih tidak tersedia"
   ;;
esac
