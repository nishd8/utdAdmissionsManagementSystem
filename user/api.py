from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
cors = CORS(app)


#utitlity
def retrive_file_content():
    f = open("erik_jonson_graduate.pl","r")
    lines = f.readlines()
    f.close()
    return lines

def write_file_contents(lines):
    f = open("erik_jonson_graduate.pl","w")
    f.writelines(lines)
    f.close()

def run_scasp():
    output = os.popen("scasp erik_jonson_graduate.pl -n0").read().split("\n\n")
    final_output=[]
    for i in output:
        if("BINDINGS" in i):
            final_output.append(i.split("=")[1].strip())
    return final_output

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    print(data)
    user_inputs =[data['gpa'],data['gre'],data['num_lor'],data['has_essay'],data['prev_edu'],"Possible_majors"]
    cmd = "?- is_eligible("+",".join(user_inputs)+")."
    lines = retrive_file_content()
    lines[-1] = cmd
    write_file_contents(lines)
    fo =run_scasp()
    print(fo)
    return jsonify({"majors":fo})

app.run(debug=True)