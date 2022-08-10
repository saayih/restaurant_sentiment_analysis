import csv

from app import app

from gevent.pywsgi import WSGIServer
http_server = WSGIServer(('', 5001), app)
http_server.serve_forever()

with open('feature_review_summary.csv', 'r') as csvFile:
	reader = csv.reader(csvFile)
	for row in reader:
		print(row)

csvFile.close()
