#!/bin/bash

# deklarasi array indirect declaration
distroLinuxDesktop[0]=Blank0n
distroLinuxDesktop[1]=Ubuntu
distroLinuxDesktop[2]=Debian
distroLinuxDesktop[3]=ArchLinux
distroLinuxDesktop[4]=LinuxMint

distroLinuxServer[0]=UbuntuServer
distroLinuxServer[1]=Cent0S
distroLinuxServer[2]=FedoraServer

# cara mengambil nilai array
echo ${distroLinuxDesktop[*]}
echo ${distroLinuxServer[*]}
