from flask import Flask, jsonify ,render_template, request
from flask_cors import CORS
from flask import url_for,redirect
import pymysql

app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False
CORS(app, resources={r"./*":{"origins":["http://127.0.0.1:5500"]}})

db = pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    passwd = '',
    database='login',
    charset='utf8mb4'
)

cursor = db.cursor()

@app.route('/',methods=['GET'])
def home():
    return render_template("./index.html")

# @app.route('/login',methods=['GET'])
# def loginPG():
#     return render_template("./login")

# @app.route('/signup',methods=['GET'])
# def reisterPG():
#     return render_template("./register")

# @app.route('/menu',methods=['GET'])
# def menu():
#     return jsonify(menuData)

# @app.route('/login',methods=['GET'])
# def loginGetAll():
#     res = {"success":False, "info":"查詢失敗"} #先預設是錯的，等try裡面成功了，就會return出來
#     try:
#         sql = 'SELECT * FROM `users`'
#         cursor.execute(sql)

#         if cursor.rowcount > 0:
#             result = cursor.fetchall()
#             res["success"] = True
#             res["info"] = "查詢成功"
#             res["result"] = result
#         else:
#             res["info"] = "查無資料"
        
#         db.commit()

#     except Exception as e:
#         db.rollback() #再做一次
#         res["info"] = f"SQL 執行失敗: {e}"
    
#     return jsonify(res)

# @app.route('/login/<int:id>',methods=['DELETE'])
# def delStudent(id):
#     res = {"success":False, "info":"刪除失敗"} #先預設是錯的，等try裡面成功了，就會return出來
#     try:
#         sql = 'DELETE FROM `users` WHERE `s_id` = %s'
#         cursor.execute(sql, (id))

#         if cursor.rowcount > 0:
#             res["success"] = True
#             res["info"] = "刪除成功"
#             res["result"] = id
#         else:
#             res["info"] = "查無資料"
        
#         db.commit()

#     except Exception as e:
#         db.rollback() #再做一次
#         res["info"] = f"SQL 執行失敗:{e}"
    
#     return jsonify(res)

@app.route('/registration',methods=['GET'])
def page():
    return render_template("./register.html")
@app.route('/registration',methods=['POST'])
def registration():
    res = {"success":False, "info":"註冊失敗"} #先預設是錯的，等try裡面成功了，就會return出來
    try:
        sql = 'INSERT INTO `users`(`Username`, `Email`, `Password`) VALUES (%s, %s, %s)'
        cursor.execute(sql, (request.json["Username"], request.json["Email"], request.json["Password"])) # request.json是保護機制，不讓別人拿到資料
        if cursor.rowcount > 0:
            res["success"] = True
            res["info"] = "註冊成功"
            res["Username"] = request.json["Username"]
            res["Password"] = request.json["Password"]
        else:
            res["info"] = "新增失敗"
        
        db.commit()

    except Exception as e:
        db.rollback() #再做一次
        res["info"] = f"SQL 執行失敗:{e}"
    
    return jsonify(res)
    # return render_template("index.html")



# @app.route('/login',methods=['POST'])
# def LogIn():
#     res = {"success":False, "info":"登入失敗"} #先預設是錯的，等try裡面成功了，就會return出來
#     try:
#         sql = 'SELECT * FROM `users` WHERE `Username` = %s AND `Password` = %s'
#         cursor.execute(sql, (request.json["Username"], request.json["Password"]))

#         if cursor.rowcount > 0:
#             res["success"] = True
#             res["info"] = "登入成功"
#             res["Username"] = request.json["Username"]
#             res["Password"] = request.json["Password"]
#         else:
#             res["info"] = "登入失敗"
        
#         db.commit()

#     except Exception as e:
#         db.rollback() #再做一次
#         res["info"] = f"SQL 執行失敗:{e}"
    
#     return jsonify(res)

# @app.route('/update/<int:id>',methods=['PUT'])
# def update(id):
#     res = {"success":False, "info":"修改失敗"} #先預設是錯的，等try裡面成功了，就會return出來
#     try:
#         sql = 'UPDATE `users` SET `s_id` = %s WHERE `Username` = %s AND `Password` = %s'
#         cursor.execute(sql, (id, request.json["Username"], request.json["Password"]))

#         if cursor.rowcount > 0:
#             res["success"] = True
#             res["info"] = "修改成功"
#             res["id"] = id
#         else:
#             res["info"] = "修改失敗"
        
#         db.commit()

#     except Exception as e:
#         db.rollback() #再做一次
#         res["info"] = f"SQL 執行失敗:{e}"
    
#     return jsonify(res)
app.debug=False
app.run()