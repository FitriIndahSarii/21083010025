printf "Input : "
read semester

declare -a IPSMahasiswa

i=0
let banyak=$semester-1

while [ $i -le $banyak ];
do
  let nilai=$i+1
  printf "Semester %.1i: " $nilai;
  read nilaisemester;
  IPSMahasiswa[$i]=$nilaisemester;
  let jumlah=jumlah+$nilaisemester;
  let i=$i+1;
done

let IPK=$jumlah/$semester
echo "IPS mhs = " $jumlah "/" $semester
echo "IPK mhs = " $IPK
