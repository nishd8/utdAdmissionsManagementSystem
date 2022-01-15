#include '../databases/major_wise_seats_db.pl'.

essay(yes).

background(mechanical,bachelors_in_engineering).
background(mechanical,bachelors_in_science).
background(mechanical,bachelors_in_science_with_calculus).

background(biomedical,bachelors_in_engineering).
background(biomedical,bachelors_in_science).
background(biomedical,bachelors_in_science_with_calculus).

background(computer_engineering,bachelors_in_engineering).
background(computer_engineering,bachelors_in_science).
background(computer_engineering,bachelors_in_science_with_calculus).

background(electrical,bachelors_in_engineering).
background(electrical,bachelors_in_science).
background(electrical,bachelors_in_science_with_calculus).

background(computer,bachelors_in_science_in_computer).
background(computer,bachelors_in_science_with_calculus).



major(computer,GPA,GRE,LOR,Essay,Background):-
    GPA>=3.3, GRE>=308 , LOR>=3 ,essay(Essay), background(computer,Background).

major(mechanical,GPA,GRE,LOR,Essay,Background):-
    GPA>=3.0, GRE>=310 , LOR>=3 ,essay(Essay), background(mechanical,Background).

major(biomedical,GPA,GRE,LOR,Essay,Background):-
    GPA>=3.3, GRE>=308 , LOR>=3 ,essay(Essay), background(biomedical,Background).

major(computer_engineering,GPA,GRE,LOR,Essay,Background):-
    GPA>=3.0, GRE>=310 , LOR>=3 ,essay(Essay), background(computer,Background).

major(electrical,GPA,GRE,LOR,Essay,Background):-
    GPA>=3.0, GRE>=310 , LOR>=3 ,essay(Essay), background(electrical,Background).



check_is_eligible(
    GPA,GRE,LOR,Essay, Background,Possible_major):- 
        major(Possible_major,GPA,GRE,LOR,Essay,Background).

% ?- check_is_eligible(2.9,301,3,yes,bachelors_in_science_in_computer,Possible_majors).
?- seats(biomedical,X).