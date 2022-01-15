majors ={
    "engineering":["biomedical","computer","computer_engineering","electrical","mechanical"],
    "management":["accounting","business_analytics","business_administration","energy management","executive_systems_engineering_and_management","finance",
    "financial_engineering_and_risk_management","healthcare_leadership_and_management","information_technology_and_management",
    "innovation_and_entrepreneurship","international_management","management_science","marketing",
    "supply_chain_management","systems_engineering_and_management"]
}


def append_to_admissions(utd_school,major,student_name):
    f =open("../databases/student_admissions_db.pl","a")
    f.write("student("+",".join([utd_school,major,student_name])+").\n")
    f.close()


def reduce_seat_number(major):
    f = open("../databases/major_wise_seats_db.pl","r")
    all_seats = f.readlines()
    for i in range(len(all_seats)):
        if(major in all_seats[i]):
            current_count = int(all_seats[i].split(",")[1].replace(").",""))
            all_seats[i] = "seats("+major+","+str(current_count-1)+").\n"
    f.close()
    f = open("../databases/major_wise_seats_db.pl","w")
    f.writelines(all_seats)
    f.close()

def render_major_option_list(school):
    lst=""
    majors_acc_school = majors[school]
    for i in range(len(majors_acc_school)):
        lst+=str(i+1)+": "+majors_acc_school[i]+",\n"
    return lst

def grant_admit():
    print("Welcome to the admission's granter portal\n")
    utd_school_option = int(input('''Select the school from the list below:\n
    1: Erik Jonsson School of Engineering and Computer Science\n
    2: Naveen Jindal School of Management\n'''))

    utd_school = ""
    if(utd_school_option==1):
        utd_school = "engineering"
    if(utd_school_option==2):
        utd_school = "management"

    major = majors[utd_school][int(input("Select a major:\n"+render_major_option_list(utd_school)))-1]
    student = input("Enter Students Name\n").replace(" ","_").lower()

    append_to_admissions(utd_school,major,student)
    reduce_seat_number(major)

grant_admit()