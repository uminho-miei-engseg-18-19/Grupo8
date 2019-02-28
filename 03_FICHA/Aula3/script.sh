python init-app.py --init init.txt
pRDashComponents=`cat init.txt | egrep -e '(pRDashComponents).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python ofusca-app.py --msg "Ola" --RDash ${pRDashComponents} --out ofusca.txt > blindMessage.txt
bmsg=`cat blindMessage.txt | egrep -e '(Blind message).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
echo "1234" | python blindSignature-app.py --key key.pem --bmsg ${bmsg} --inputFile init.txt  > blind.txt
s=`cat blind.txt | egrep -e '(Blind signature).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python desofusca-app.py -s ${s} --RDash ${pRDashComponents} --in ofusca.txt > sdash.txt
sDash=`cat sdash.txt | egrep -e '(Signature).*' | awk -F ":" '{print $2}' | awk -F " " '{print $1}'`
python verify-app.py --cert key.crt --msg "Ola" --sDash ${sDash} -f ofusca.txt
# 
echo "\n---  ASSINANTE  ---"
cat init.txt 
echo "\n---  REQUERENTE  ---"
cat ofusca.txt
echo "\n--- PARAMETROS USADOS  ---"
echo "pRDashComponents: $pRDashComponents"
echo "Blind message $bmsg"
echo "Blind signature $s"
echo "Signature $sDash"
echo ""
rm sdash.txt blind.txt blindMessage.txt
