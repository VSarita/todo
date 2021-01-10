import pymongo

from settings import MONGO_URL

database = "todo"

def get_db():
    conn = pymongo.MongoClient(MONGO_URL)
    return conn[database]

def get_rows(collection, query, fields={}, sort={}, skip=0, limit=1000000):
	"""
	:param collection:
	:param query:
	:param fields:
	:param sort:
	:param skip:
	:param limit:
	:return: list
	"""

	db = get_db()
	rows = []
	if sort == {}:
		if fields == {}:
			cursor = db[collection].find(query).skip(skip).limit(limit)
		else:
			cursor = db[collection].find(query, fields).skip(skip).limit(limit)
	else:
		if fields == {}:
			cursor = db[collection].find(query).sort(sort["key"], sort["direction"]).skip(skip).limit(limit)
		else:
			cursor = db[collection].find(query, fields).sort(sort["key"], sort["direction"]).skip(skip).limit(limit)

	# print("cursor get data rows", cursor)
	for item in cursor:
		if "_id" in item:
			item['_id'] = str(item['_id'])
		rows.append(item)
	return rows



def get_row(collection, query, fields={}, sort={}):
	"""

	:param collection:
	:param query:
	:param fields:
	:param sort:
	:return: dict
	"""
	if fields is None:
		fields = {}
	db = get_db()
	if fields == {}:
		row = db[collection].find_one(query)
	else:
		row = db[collection].find_one(query, fields)
	if row is not None:
		if "_id" in row:
			row['_id'] = str(row['_id'])
	return row

def insert(collection, data):
	db = get_db()
	insert_id = db[collection].insert(data, check_keys=False)
	return str(insert_id)

def remove(collection,query):
	db=get_db()
	return db[collection].remove(query)


def update(collection, update_data, query):
	db = get_db()
	return db[collection].update(query, update_data, multi=True)