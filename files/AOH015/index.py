from flask import Flask, Response, request
app = Flask(__name__)

all_upload = {}

@app.route('/', methods = ['GET'])
def index():
    with open("index.html","rb") as f:
        return f.read()

@app.route('/upload_file', methods = ['POST'])
def upload_file():
    f = request.files['file']
    upload_ = f.read()
    upload_header = upload_[:8]
    if upload_header != b'\x89PNG\r\n\x1a\n':
        return "上传失败"
    else:
        if f.filename[:-4] == ".php":
            return "flag{牛逼}"
        else:
            return "上传成功"

@app.route('/upload_checker', methods = ['POST'])
def upload_checker():
    f = request.files['file']
    upload_ = f.read()
    upload_list = upload_.split(b"A0A")
    all_upload[f.filename] = upload_list
    return '上传成功'

@app.route('/getfuzzfile', methods = ['GET'])
def getfuzzfile():
    fuzzbytes = []
    for i in range(0,255+1):
        fuzzbytes += [65, 48, 65] # A0A
        fuzzbytes.append(i)
    fuzzbytes = bytes(fuzzbytes)
    resp = Response(fuzzbytes, mimetype="application/octet-stream")
    resp.headers["Content-Length"] = str(len(fuzzbytes))
    resp.headers["Content-Disposition"] = "attachment; filename=fuzzfile"
    return resp
    
@app.route('/compare', methods = ['GET'])
def compare():
    result = []
    result_str = ""
    name1 = request.args.get('name1')
    name2 = request.args.get('name2')
    for index, char_1 in enumerate(all_upload[name1]):
        char_2 = all_upload[name2][index]
        is_diff = 0
        if char_1 != char_2:
            is_diff = 1
        compare_this = [char_1, char_2, is_diff]
        result.append(compare_this)
        result_str += str(compare_this) +"\n"
    return result_str

if __name__ == '__main__':
   app.run(host="0.0.0.0",debug = True)