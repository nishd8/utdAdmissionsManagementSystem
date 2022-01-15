import os

def retrive_file_content():
    f = open("erik_jonson_graduate.pl","r")
    lines = f.readlines()
    f.close()
    return lines

def write_file_contents(lines):
    f = open("erik_jonson_graduate.pl","w")
    f.writelines(lines)
    f.close()

def take_user_inputs():
    gpa = input("Provide your Bachelor's GPA\n")
    gre = input("Provide your GRE score\n")
    num_lor = input("Enter number of LORs you have\n")
    has_essay = input("Do you have a essay prepared?(yes/no)\n")
    bachelors_degree_option = int(input('''Select Your Bachelor's Degree option\n
    1: Bachelor's in Engineering\n
    2: Bachelor's in Science\n
    3: Bachelor's in Science (With Caclulus)\n
    4: Bachelor's in Computer Science\n'''))

    bachelors_degree = ""
    if(bachelors_degree_option==1):
        bachelors_degree="bachelors_in_engineering"
    if(bachelors_degree_option==2):
        bachelors_degree="bachelors_in_science"
    if(bachelors_degree_option==3):
        bachelors_degree="bachelors_in_science_with_calculus"
    if(bachelors_degree_option==4):
        bachelors_degree="bachelors_in_science_in_computer"

    user_inputs =[gpa,gre,num_lor,has_essay,bachelors_degree,"Possible_majors"]
    cmd = "?- check_is_eligible("+",".join(user_inputs)+")."

    return cmd

def run_scasp():
    output = os.popen("scasp erik_jonson_graduate.pl -n0").read().split("\n\n")
    final_output=[]
    for i in output:
        if("BINDINGS" in i):
            final_output.append(i.split("=")[1].strip())
    if(len(final_output)>0):
        print("\nAccording to the inputs given by the following departments may be interest in having you as a student:\n"+",\n".join(final_output)+"\n")
    else:
        print("\nUnfortunately, the inputs given by you suggest that you are not eligible to be a student at UTD.\nContact 'engineering@utdallas.edu' for more info.\n")
    

lines = retrive_file_content()
lines[-1] = take_user_inputs()
write_file_contents(lines)
run_scasp()