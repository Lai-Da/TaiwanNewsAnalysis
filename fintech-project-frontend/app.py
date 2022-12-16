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
    return render_template("./home/index.html")
@app.route('/profolio',methods=['GET'])
def profolio():
    return render_template("./home/profolio.html")

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'itri' or request.form['password'] != 'itri':
            error = 'Invalid username or password. Please try again!'
        else:
            return redirect(url_for('main_page')) #return render_template('main_page.html')
    return render_template('./home/login.html', error=error)

# @app.route('/news',methods=['GET', "POST"])
# def news():
#     if request.method == 'GET':
#         return render_template('news.html', product_list=product_list)

#     if request.method == 'POST':
#         cat_list = ['', 'OZWEEGO', 'Superstar', 'Stan', 'Smith', 'others', 'Retropy', 'Forum', 'Campus', 'Puffylette']

#         cursor = db.cursor()
#         cllection_insert = """INSERT INTO `collection` VALUES (%s);"""
#         # p_id = request.values.get('p_id') # 用 form 的方法
#         # cursor.execute(cllection_insert, (p_id))
#         try:
#             cursor.execute(cllection_insert, (request.json["id"])) # 用 js 的方法
#             db.commit()
#         except:
#             print('selection process')

#         selection_sql = f"""SELECT `category`.`id`, `category`.`name`, `productid_imgurl`.`imgURL` FROM `category` 
#                             INNER JOIN `productid_imgurl` ON `category`.`id` = `productid_imgurl`.`id`
#                             WHERE `category`.`category` = '{request.values.get('c_id')}'"""
#         cursor.execute(selection_sql)

#         product_list1 = []
#         if cursor.rowcount > 0:
#             results = cursor.fetchall()

#             product_list1 = []
#             for i in results:
#                 ids = i[0]
#                 # names = " ".join(re.findall("\w+\s+", i[2]))
#                 names = i[1]
#                 url = i[2]
#                 product_list1.append({"id": ids, "name": names, "url": url})

#         cursor.close()
#         return render_template('product_page.html', product_list=product_list1)
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
            return render_template("./admin/index.html")
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
app.debug=True
app.run()