from flask import Flask, request, send_file;
from flaskext.mysql import MySQL;
import json;
import os;

UPLOAD_FOLDER = "./image/"

app = Flask(__name__);
mysql = MySQL();

app.config['MYSQL_DATABASE_USER'] = 'root';
app.config['MYSQL_DATABASE_PASSWORD'] = 'take2010';
app.config['MYSQL_DATABASE_DB'] = 'nextagram';

mysql.init_app(app);

@app.route("/")
def helloWorld():
    return "helloWorld";

@app.route("/loadData", methods = ["GET", "POST"])
def loadData():
	req = request.args.get("ArticleNumber");
	cursor = mysql.connect().cursor();
	if req is None:
		cursor.execute("select * from next_android_nextagram")
	else:
		cursor.execute("select * from next_android_nextagram where ArticleNumber > " + req)

	result = []
	columns = tuple( [d[0] for d in cursor.description])

	for row in cursor:
		result.append(dict(zip(columns,row)))

	print(result);

	return json.dumps(result);

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
def allowedFile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

@app.route("/upload", methods = ["POST"])
def upload():
    if request.method == 'POST':
        title = request.form['title']
        writerName = request.form['writerName']
        writerId = request.form['writerId']
        content = request.form['content']
        writeDate = request.form['writeDate']
        imgName = request.form['imgName']

        file = request.files['uploadedfile']
        path = UPLOAD_FOLDER + file.filename;

        if file and allowedFile(file.filename):
            file.save(path)

            con = mysql.connect()
            cursor = con.cursor()

            query = "insert into next_android_nextagram \
            (Title, WriterName, WriterID, Content, WriteDate, ImgName) values \
            ('" + title + "', '" + writerName + "','" + writerId + "', '" + content + "', \
                '" + writeDate + "', '" + imgName + "');";

            #print(query);
            cursor.execute(query);
            con.commit();

            return "ok";

    return "error";

@app.route("/image/<fileName>", methods = ["GET", "POST"])
def loadImage(fileName):
    print("fileName: " + fileName);
    return send_file(UPLOAD_FOLDER+"/"+fileName, mimetype='image');


if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port = 7646);