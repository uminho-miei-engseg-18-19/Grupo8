python init-app.py --init init.txt
cat init.txt
pRDashComponents=`cat init.txt | egrep -e '(pRDashComponents).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python ofusca-app.py --msg "Ola" --RDash ${pRDashComponents} --out ofusca.txt
bmsg=`cat ofusca.txt | egrep -e '(Blind message).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
echo "1234" | python blindSignature-app.py --key key.pem --bmsg ${bmsg} --inputFile init.txt  > blind.txt
s=`cat blind.txt | egrep -e '(Blind signature).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python desofusca-app.py -s ${s} --RDash ${pRDashComponents} --in ofusca.txt > sdash.txt
cat sdash.txt
sDash=`cat sdash.txt | egrep -e '(Signature).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python verify-app.py --cert key.crt --msg "Ola" --sDash ${sDash} -f ofusca.txt

echo "-------------------------------------"
cat init.txt ofusca.txt
echo "pRDashComponents: $pRDashComponents"
echo "Blind message $bmsg"
echo "Signature $sDash"
rm *.txt
