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

# cursor = db.cursor()
# cursor.execute('SELECT * FROM `ctee_data1129_1201`')

# if cursor.rowcount > 0:
#     results = cursor.fetchall()

#     news_list = []
#     for i in results:
#         time = i[0]
#         title = i[1]
#         url = i[2]
#         text = i[3]
#         src = i[4]
#         news_list.append({"time": time, "title": title, "url": url, "text": text, "src": src})
# cursor.close()
# ========================================================
cursor = db.cursor()
product_sql = """SELECT*FROM `c5news15_16_data` 
                            INNER JOIN `bert_15_16` ON `bert_15_16`.`title` = `c5news15_16_data`.`title`"""
cursor.execute(product_sql)

if cursor.rowcount > 0:
    results = cursor.fetchall()

    news_list = []
    for i in results:
        time = i[0]
        url = i[1]
        source = i[2]
        title = i[3]
        category=i[5]
        news_list.append({"time": time, "title": title, "url":url,"category": category})
cursor.close()
################
cursor = db.cursor()
DROP_table = "DROP TABLE IF EXISTS collection"
cursor.execute(DROP_table)
CREATE_table = "CREATE TABLE IF NOT EXISTS collection(id CHAR(20) NOT NULL)"
cursor.execute(CREATE_table)
cursor.close()
# ========================================================

@app.route('/',methods=['GET'])
def home():
    return render_template("./home/index.html")

@app.route('/profolio',methods=['GET'])
def profolio():
    return render_template("./admin/profolio.html")

# @app.route('/news',methods=['GET', "POST"])
# def news():
#     if request.method == 'GET':
#         return render_template('./home/news.html', news_list=news_list)

@app.route('/log_in', methods=['GET', 'POST'])
def log_in():
    error = None
    if request.method == 'POST':
        if request.form['username'] != '123456' or request.form['password'] != '123456':
            error = 'Invalid username or password. Please try again!'
        else:
            return redirect(url_for('adminhome')) #return render_template('main_page.html')
    return render_template('./home/login.html', error=error)

# ========================admin===================
@app.route('/admin',methods=['GET'])
def adminhome():
    return render_template("./admin/index.html")

@app.route('/news',methods=['GET', "POST"])
def news():
    if request.method == 'GET':
        return render_template('./admin/news.html', news_list=news_list)

    if request.method == 'POST':
        # cat_list = ['', 'up','down','unchange']

        cursor = db.cursor()
        collection_insert = """INSERT INTO `collection` VALUES (%s);"""
        c_id = request.values.get('c_id') # 用 form 的方法
        # cursor.execute(cllection_insert, (c_id))
        try:
            # cursor.execute(collection_insert, (request.json["title"])) # 用 js 的方法
            cursor.execute(collection_insert, (c_id))
            db.commit()
        except:
            print('selection process')

        selection_sql = f"""SELECT*FROM `c5news15_16_data` 
                            INNER JOIN `bert_15_16` ON `bert_15_16`.`title` = `c5news15_16_data`.`title`
                            WHERE `bert_15_16`.`category`= '{c_id}'"""
        cursor.execute(selection_sql)

        news_list1 = []
        if cursor.rowcount > 0:
            results = cursor.fetchall()

            news_list1 = []
            for i in results:
                time=i[0]
                url = i[1]
                source = i[2]
                title = i[3]
                category=i[5]
                news_list1.append({"time": time, "title": title, "url":url,"category": category,"source":source})

        cursor.close()
        return render_template('./admin/news.html', news_list=news_list1)

@app.route('/collection_page',methods=['GET', 'POST'])
def collection_page():
    if request.method == 'GET':
        collection_list = []
        cursor = db.cursor()
        collection_sql = """SELECT*FROM `c5news15_16_data` 
                            INNER JOIN `bert_15_16` ON `bert_15_16`.`title` = `c5news15_16_data`.`title`"""
        cursor.execute(collection_sql)

        if cursor.rowcount > 0:
            results = cursor.fetchall()

            for i in results:
                time = i[0]
                # names = " ".join(re.findall("\w+\s+", i[2]))
                title = i[1]
                url = i[2]
                collection_list.append({"time": time, "title": title, "url": url})

        cursor.close()
        return render_template('./admin/collection_page.html', collection_list = collection_list)

    if request.method == 'POST':
        collection_list = []

        cursor = db.cursor()

        p_id = request.values.get('p_id')
        deletion_sql = f"""DELETE FROM `collection` WHERE `title` = '{p_id}'"""
        cursor.execute(deletion_sql)

        collection_sql = """SELECT DISTINCT(`collection`.`title`), `c5news15_16_data` 
                            INNER JOIN `bert_15_16` ON `bert_15_16`.`title` = `c5news15_16_data`.`title`
                            WHERE `c5news15_16_data`.`source`"""
        cursor.execute(collection_sql)

        if cursor.rowcount > 0:
            results = cursor.fetchall()

            for i in results:
                ids = i[0]
                # names = " ".join(re.findall("\w+\s+", i[2]))
                names = i[1]
                url = i[2]
                collection_list.append({"id": ids, "name": names, "url": url})

        db.commit()
        cursor.close()
        return render_template('collection_page.html', collection_list=collection_list)
# =================登入/註冊=======================
@app.route('/login',methods=['GET'])
def LogIn():
    return render_template("./home/login.html")
@app.route('/logi',methods=['POST'])
def LogIN():
    res = {"success":False, "info":"登入失敗"} #先預設是錯的，等try裡面成功了，就會return出來
    try:
        sql = 'SELECT * FROM `students` WHERE `s_name` = %s AND `s_nickname` = %s'
        cursor.execute(sql, (request.json["name"], request.json["nickname"]))

        if cursor.rowcount > 0:
            res["success"] = True
            res["info"] = "登入成功"
            res["name"] = request.json["name"]
            res["nickname"] = request.json["nickname"]

        else:
            res["info"] = "登入失敗"
        
        db.commit()

    except Exception as e:
        db.rollback() #再做一次
        res["info"] = f"SQL 執行失敗:{e}"
    
    return jsonify(res)

@app.route('/register',methods=['GET'])
def register():
    return render_template("./home/register.html")

@app.route('/newStudent',methods=['POST'])
def newStudent():
    res = {"success":False, "info":"註冊失敗"} #先預設是錯的，等try裡面成功了，就會return出來
    try:
        sql = 'INSERT INTO `students`(`s_name`, `s_gender`, `s_nickname`) VALUES (%s, %s, %s)'
        cursor.execute(sql, (request.json["name"], request.json["gender"], request.json["nickname"])) # request.json是保護機制，不讓別人拿到資料

        if cursor.rowcount > 0:
            res["success"] = True
            res["info"] = "註冊成功"
            res["name"] = request.json["name"]
            res["nickname"] = request.json["nickname"]
        else:
            res["info"] = "新增失敗"
        
        db.commit()

    except Exception as e:
        db.rollback() #再做一次
        res["info"] = f"SQL 執行失敗:{e}"
    
    return jsonify(res)




# @app.route('/log_in', methods=['GET', 'POST'])
# def log_in():
#     error = None
#     if request.method == 'POST':
#         if request.form['username'] != 'itri' or request.form['password'] != 'itri':
#             error = 'Invalid username or password. Please try again!'
#         else:
#             return redirect(url_for('main_page')) #return render_template('main_page.html')
#     return render_template('./home/login.html', error=error)




# @app.route('/registration',methods=['POST'])
# def registration():
#     res = {"success":False, "info":"註冊失敗"} #先預設是錯的，等try裡面成功了，就會return出來
#     try:
#         sql = 'INSERT INTO `users`(`Username`, `Email`, `Password`) VALUES (%s, %s, %s)'
#         cursor.execute(sql, (request.json["Username"], request.json["Email"], request.json["Password"])) # request.json是保護機制，不讓別人拿到資料
#         if cursor.rowcount > 0:
#             res["success"] = True
#             res["info"] = "註冊成功"
#             res["Username"] = request.json["Username"]
#             res["Password"] = request.json["Password"]
#             # return render_template("./admin/index.html")
#         else:
#             res["info"] = "新增失敗"
        
#         db.commit()

#     except Exception as e:
#         db.rollback() #再做一次
#         res["info"] = f"SQL 執行失敗:{e}"
    
#     return jsonify(res)

# ===============================================
if __name__ == '__main__':
    app.debug=True
    app.run()