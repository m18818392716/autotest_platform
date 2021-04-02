from flask import Flask, request, json
from flask import jsonify, g
import copy
'''
Flask的socket是基于Werkzeug 实现的，模板语言依赖jinja2模板，在使用Flask之前需要安装一下；

pip install flask
'''
'''
知识补充:
flask之g对象
1.在flask中，有一个专门用来存储用户信息的g对象，g的全称的为global。
2.g对象在一次请求中的所有的代码的地方，都是可以使用的。

Flask 的 jsonify
Flask 框架里，可以用 jsonify 返回 json 数据
'''

app = Flask(__name__)

@app.before_request
def set_up_data():
    g.data = [
        {'id': 1, 'title': 'task 1', 'desc': 'this is task 1'},
        {'id': 2, 'title': 'task 2', 'desc': 'this is task 2'},
        {'id': 3, 'title': 'task 3', 'desc': 'this is task 3'},
        {'id': 4, 'title': 'task 4', 'desc': 'this is task 4'},
        {'id': 5, 'title': 'task 5', 'desc': 'this is task 5'}
    ]
    g.task_does_not_exist = {"msg": "task does not exist"}

@app.route("/") # 路由
def hello(): # handler
    return "Hello World!"

@app.route('/mock', methods=['POST'])
def mock():
    """ 模拟运营商系统
    :param mobile:用户手机号
    :param password:运营商密码
    :return:性别、身份证号、话费
    """
    mobile = request.form['mobile']
    password = request.form['password']

    try:
        assert password == 'a123456', u'运营商密码错误'

        if mobile == "12345678901":
            data = {'sex': 'man', 'Id number': '111111111111111111', 'charge': 105}
        elif mobile == "12345678902":
            data = {'sex': 'woman', 'Id number': '1111111111111112', 'charge': 120}
        elif mobile == "12345678903":
            data = {'sex': 'man', 'Id number': '111111111111111113', 'charge': 135}
        else:
            data = {'msg': 'mobile number not found'}
    except:
        data = {'msg': 'password error'}

    return json.dumps(data)

@app.route('/api/tasks')
def get_all_tasks():
    return jsonify(g.data)

@app.route('/api/tasks/')
def get_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        return jsonify(g.data[task_id])
    else:
        return jsonify(g.task_does_not_exist)

@app.route('/api/tasks/', methods=['PUT'])
def complete_task(task_id):
    if task_id > 0 and task_id <= len(g.data):
        tmp = copy.deepcopy(g.data[task_id])
        tmp['done'] = True
        return jsonify(tmp)
    else:
        return jsonify(g.task_does_not_exist)


if __name__ == '__main__':
    app.run()