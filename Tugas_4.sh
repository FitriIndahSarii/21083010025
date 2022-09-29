echo -n "Masukkan angka ganjil: ";
read a
mod=$(($a % 2 ))

if [ $mod == 0 ]
then
 echo "ANGKA HARUS GANJIL!"
 echo -n "Masukkan angka baru: ";
read a
fi

echo "Angka yang diinputkan adalah $a";

while [ $a -gt 0 ]
do
  echo $a
  a=$((a - 2))
done
