#!/usr/bin/python

import urllib2, base64, urllib, csv

pathToSimFile = "/Users/bpopejoy/Documents/Inventory.csv"
username = ""
passowrd = ""

def importBarcode(inventoryID, barcode):
	# Updates the invetory item with the specified ID...
	request = urllib2.Request("https://oncampuslivingtest.sdsu.edu/StarRezRESTtest/services/update/RoomSpaceInventory.RoomSpaceInventoryID/" + inventoryID)
	base64string = base64.encodestring('%s:%s' % (username, passowrd)).replace('\n', '')
	request.add_header("Authorization", "Basic %s" % base64string)
	# ...with the data in barcode.
	data = urllib.urlencode({'code' : barcode})
	try:
		handler = urllib2.urlopen(request, data)
	except urllib2.HTTPError, e:
		print "HTTPError 1 = " + str(e.code)
	except urllib2.URLError, e:
		print "URLError = " + str(e.reason)
	except httplib.HTTPException, e:
		print 'HTTPException'
	except Exception:
		import traceback
		print 'generic exception: ' + traceback.format_exc()
	else:
		print inventoryID + " - Success"

# Opens data file from path above and updates database with barcodes.
with open(pathToSimFile, 'rb') as csvfile:
	reader = csv.reader(csvfile, delimiter=',', quotechar='|')
	firstLine =  True
	for row in reader:
		if not firstLine:
			inventoryID = row[3]
			barcode = row[4]
			importBarcode(inventoryID, barcode)
		else:
			firstLine = False
