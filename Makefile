install:
	virtualenv venv
	pwd
	. venv/bin/activate
	pip install -r requirements.txt

run:
	if [ ! -d venv ] ; then make install ; fi 
	if [ ! -f data.json ] ; then cp data.json.example data.json ; fi
	python main.py