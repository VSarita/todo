import db
from bson.objectid import ObjectId
import traceback
def fetch_tasks(request):
    try:
        tasks_list = []
        completed_tasks = []
        query = {}
        tasks = db.get_rows(collection="tasks", query=query)
        for task in tasks:
            bucket_id = task.get("bucket_id")
            if bucket_id:
                bucket = db.get_row(collection="buckets",query={"_id":ObjectId(bucket_id)})
                task["bucket_name"] = bucket.get("name","")
            if task.get("is_completed"):
                completed_tasks.append(task)
            else:
                tasks_list.append(task)

        return {"data": {"tasks_list":tasks_list,"completed_tasks":completed_tasks}}
    except:
        print traceback.format_exc()
        return {"data":[]}

def add_new_task(request):
    try:
        if request.get("_id"):
            if request.get("new_bucket") not in ["", None]:
                bucket_id = db.insert(collection="buckets", data={"name": request.get("new_bucket")})
                task = {
                    "title": request.get("title", ""),
                    "description": request.get("description", ""),
                    "bucket_id": bucket_id
                }
                task_inserted = db.update(collection="tasks", query={"_id":ObjectId(request.get("_id"))}, update_data={"$set":task})
            else:

                task = {
                    "title": request.get("title", ""),
                    "description": request.get("description", ""),
                    "bucket_id": request.get("bucket_id")
                }
                print db.update(collection="tasks", query={"_id": ObjectId(request.get("_id"))},
                                          update_data={"$set":task})
        else:
            if request.get("new_bucket") not in ["",None]:
                bucket_id = db.insert(collection="buckets", data={"name":request.get("new_bucket")})
                task = {
                    "title":request.get("title",""),
                    "description": request.get("description",""),
                    "bucket_id": bucket_id
                }
                task_inserted = db.insert(collection="tasks",data=task)
            else:
                task = {
                    "title": request.get("title", ""),
                    "description": request.get("description", ""),
                    "bucket_id": request.get("bucket_id")
                }
                task_inserted = db.insert(collection="tasks", data=task)

        return {"success":True}
    except:
        traceback.format_exc()
        return {"success":False}

def remove_task(request):
    task_id = request.get("_id")
    try:
        task_remove = db.remove(collection="tasks", query={"_id":ObjectId(task_id)})
        return {"success": True}
    except:
        return {"success": False}

def mark_task_completed(request):
    task_id = request.get("_id")
    print "task_id",task_id
    try:
        print db.update(collection="tasks", query={"_id":ObjectId(task_id)}, update_data={"$set":{"is_completed":True}})
        return {"success": True}
    except:
        return {"success": False}






