import db

def fetch_buckets():
    buckets = db.get_rows(collection="buckets", query={})
    print "_---------------------------------------------------------------", buckets
    return {"data":buckets}