from flask import Flask, jsonify, request
import json
import traceback
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba325'

from api.task import fetch_tasks, add_new_task, remove_task, mark_task_completed
from api.bucket import fetch_buckets

@app.route("/")
@app.route("/api/todo", methods=['GET', 'POST'])
def todo():

    try:
        return jsonify(fetch_tasks({"bucket":"all"})),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501

@app.route("/api/tasks", methods=['GET', 'POST'])
def tasks():

    try:
        return jsonify(fetch_tasks({"bucket":"all"})),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501


@app.route("/api/buckets", methods=['GET', 'POST'])
def buckets():
    try:
        return jsonify(fetch_buckets()),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501

@app.route("/api/add_task", methods=['GET', 'POST'])
def add_task():
    try:
        return jsonify(add_new_task(json.loads(request.data))),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501

@app.route("/api/delete_task", methods=['GET', 'POST'])
def delete_task():
    try:
        return jsonify(remove_task(json.loads(request.data))),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501

@app.route("/api/mark_completed", methods=['GET', 'POST'])
def mark_completed():
    try:
        return jsonify(mark_task_completed(json.loads(request.data))),200
    except Exception as e:
        print e
        print traceback.format_exc()
        return jsonify({"success": False}), 501
