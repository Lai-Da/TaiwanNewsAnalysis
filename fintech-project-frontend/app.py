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
    database='taiwannewsanalysis',
    charset='utf8mb4'
)

cursor = db.cursor()
cursor.execute('SELECT * FROM `ctee_data1129_1201`')

if cursor.rowcount > 0:
    results = cursor.fetchall()

    news_list = []
    for i in results:
        time = i[0]
        title = i[1]
        url = i[2]
        text = i[3]
        src = i[4]
        news_list.append({"time": time, "title": title, "url": url, "text": text, "src": src})
# cursor.close()


@app.route('/',methods=['GET'])
def home():
    return render_template("./home/index.html")

@app.route('/profolio',methods=['GET'])
def profolio():
    return render_template("./home/profolio.html")

@app.route('/news',methods=['GET', "POST"])
def news():
    if request.method == 'GET':
        return render_template('./home/news.html', news_list=news_list)



@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'itri' or request.form['password'] != 'itri':
            error = 'Invalid username or password. Please try again!'
        else:
            return redirect(url_for('main_page')) #return render_template('main_page.html')
    return render_template('./home/login.html', error=error)

@app.route('/register',methods=['GET'])
def register():
    return render_template("./home/register.html")


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
            # return render_template("./admin/index.html")
        else:
            res["info"] = "新增失敗"
        
        db.commit()

    except Exception as e:
        db.rollback() #再做一次
        res["info"] = f"SQL 執行失敗:{e}"
    
    return jsonify(res)




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
if __name__ == '__main__':
    app.debug=True
    app.run()