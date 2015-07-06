#!/usr/bin/python2.7

from flask.ext.testing import TestCase
import json
import unittest

from app import app

existing_bird_id_url = "/birds/55998cde25d367352eea628f"

class FlaskTestCase(unittest.TestCase):
	def test_index(self):
		print "-> Test: Index /, expects 200 OK"
		tester = app.test_client(self)
		response = tester.get('/')
		self.assertEqual(response.status_code, 200)
		
	def test_all_birds(self):
		print "-> Test: /birds, expects 200 OK"
		tester = app.test_client(self)
		response = tester.get('/birds', content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_one_bird(self):
		print "-> Test: /birds/5599583225d36778ed478464, expects 200 OK"
		tester = app.test_client(self)
		response = tester.get(existing_bird_id_url, content_type='application/json')
		self.assertEqual(response.status_code, 200)

	def test_insert_bird(self):
		print "-> Test: Inserting bird, expects 200 OK"

		jsonpost = {
			"name": "test-birdie",
			"family": "public",
			"continents": ["europe","asia"],
			"visible": True
		}

		tester = app.test_client(self)
		response = tester.post(
						'/birds',
						data=json.dumps(jsonpost),
						content_type='application/json'
					)

		self.assertEqual(response.status_code, 200)

	def test_delete_bird(self):
		print "-> Test: Deletes bird, 5599583225d36778ed478464, expects 200 OK"
		tester = app.test_client(self)
		response = tester.get(existing_bird_id_url, data="", content_type='application/json', method='DELETE')
		self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
	unittest.main()