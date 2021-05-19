#ipfs daemon

if [ ! -e ${HOME}/.ipfs/api ]
then 
    ipfs daemon &
else
   echo "IPFS already started"
fi
while [ ! -e ${HOME}/.ipfs/api ]
do 
   echo "Waiting for IPFS to start";
   sleep 1
done

