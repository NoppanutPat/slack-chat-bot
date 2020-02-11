from __future__ import print_function
from flask import Flask, escape, request
import sys
import json
import os

app = Flask(__name__)
work_list = ['<@ULY3LHGEQ>','P jay']

@app.route('/webhook-end-point',methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
	print(request.get_json() , file=sys.stderr)
	data = request.get_json()
	if "challenge" in data:
		print(data["challenge"] , file=sys.stderr)
		challenge = data["challenge"]
		send_data = {}
		send_data.setdefault("challenge",challenge)
		response = app.response_class(
        		response=json.dumps(send_data),
        		status=200,
        		mimetype='application/json'
    		)
    		return response
	else:
		text = data["event"]["blocks"][0]["elements"][0]["elements"][0]["text"]
		link = "https://hooks.slack.com/services/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"
		if text == "findcom":
			global work_list
			os.system('''curl -X POST -H 'Content-type: application/json' --data '{"text":"'''+work_list[0]+" !! Please send computer to "+work_list[1]+'''"}' '''+link)		
		elif text == "com-now":
			os.system('''curl -X POST -H 'Content-type: application/json' --data '{"text":" Now computer is at '''+work_list[0]+'''"}' '''+link)
	return "Hello"

if __name__ == '__main__':
      app.run(debug=True ,host='0.0.0.0', port=80)
