export SETUP_SCRIPT=true
rm -f victims.db
rm -f ../victims.db
rm -f ./chargerblue/encrypted*.enc
cd ../hacknet 
pip install -e .
cd ../chrometokenmanager
go build
mv chrometokenmanager ../setuptools
cd ../setuptools
python -m hacknet.app &
sleep 5
python create-db.py
cp victims.db ../
cp chargerblue/*.enc ../../dist/
pkill python
