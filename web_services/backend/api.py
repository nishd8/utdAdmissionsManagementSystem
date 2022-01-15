import json
from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin
import os
app = Flask(__name__)
cors = CORS(app)


#utitlity
def retrive_file_content(file_path):
    f = open(file_path,"r")
    lines = f.readlines()
    f.close()
    return lines

def write_file_contents(file_path,lines):
    f = open(file_path,"w")
    f.writelines(lines)
    f.close()

def run_scasp():
    output = os.popen("scasp erik_jonson_graduate.pl -n0").read().split("\n\n")
    final_output=[]
    for i in output:
        if("BINDINGS" in i):
            final_output.append(i.split("=")[1].strip())
    return final_output

def append_to_admissions(utd_school,major,student_name):
    f =open("../../databases/student_admissions_db.pl","a")
    f.write("student("+",".join([utd_school,major,student_name])+").\n")
    f.close()


def reduce_seat_number(major):
    f = open("../../databases/major_wise_seats_db.pl","r")
    all_seats = f.readlines()
    for i in range(len(all_seats)):
        if(major in all_seats[i]):
            current_count = int(all_seats[i].split(",")[1].replace(").",""))
            all_seats[i] = "seats("+major+","+str(current_count-1)+").\n"
    f.close()
    f = open("../../databases/major_wise_seats_db.pl","w")
    f.writelines(all_seats)
    f.close()

@app.route('/check_eligibility', methods=['POST'])
def check_eligibility():
    data = request.get_json()
    print(data)
    user_inputs =[data['gpa'],data['gre'],data['num_lor'],data['has_essay'],data['prev_edu'],"Possible_majors"]
    cmd = "?- is_eligible("+",".join(user_inputs)+")."
    lines = retrive_file_content("erik_jonson_graduate.pl")
    lines[-1] = cmd
    write_file_contents("erik_jonson_graduate.pl",lines)
    fo =run_scasp()
    print(fo)
    return jsonify({"majors":fo})

@app.route('/get_schools', methods=['GET'])
def get_schools():
    lines = retrive_file_content("../../databases/schools_db.pl")
    for i in range(len(lines)):
        lines[i] = lines[i].replace("school(","").replace(")","").replace("\n","")
    return jsonify({"schools":lines})

@app.route('/get_majors', methods=['POST'])
def get_majors():
    school = request.get_json()['school']
    lines = retrive_file_content("../../databases/majors_db.pl")
    result = []
    for i in lines:
        if(school in i):
            result.append(i.split(",")[0].replace("major(",""))
    return jsonify({"majors":result})

@app.route('/grant_admission', methods=['POST'])
def grant_admission():
    data = request.get_json()
    append_to_admissions(data['school'],data['major'],data['name'].replace(" ","_").lower())
    reduce_seat_number(data['major'])
    return "LOL"


app.run(debug=True)