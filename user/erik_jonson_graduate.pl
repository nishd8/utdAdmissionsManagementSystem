#include '../databases/major_wise_seats_db.pl'.

% search in array utitlity
member(E,[E|_]).
member(E,[_|R]):- member(E,R).


%db for erik jonson
major(biomedical).
major(computer).
major(computer_engineering).
major(electrical).
major(mechanical).

gpa(biomedical,3.3).
gpa(computer,3.3).
gpa(computer_engineering,3.0).
gpa(electrical,3.0).
gpa(mechanical,3.0).

gre(biomedical,308).
gre(computer,315).
gre(computer_engineering,310).
gre(electrical,312).
gre(mechanical,310).

lors(biomedical,3).
lors(computer,3).
lors(computer_engineering,3).
lors(electrical,3).
lors(mechanical,3).

essay(biomedical,yes).
essay(computer,yes).
essay(computer_engineering,yes).
essay(electrical,yes).
essay(mechanical,yes).

previous_education(biomedical,['bachelors_in_engineering', 'bachelors_in_science', 'bachelors_in_science_with_calculus']).
previous_education(computer,['bachelors_in_engineering', 'bachelors_in_science', 'bachelors_in_science_with_calculus', 'bachelors_in_science_computer_science']).
previous_education(computer_engineering,['bachelors_in_science_with_calculus', 'bachelors_in_science_computer_science']).
previous_education(electrical,['bachelors_in_engineering', 'bachelors_in_science', 'bachelors_in_science_with_calculus']).
previous_education(mechanical,['bachelors_in_engineering', 'bachelors_in_science', 'bachelors_in_science_with_calculus']).

is_eligible(GPA, GRE, LOR,Essay, Prev_education, Possible_major):-
    gpa(Possible_major,Y),GPA>=Y,
    gre(Possible_major,Z),GRE>=Z,
    lors(Possible_major,X),LOR>=X,
    essay(Possible_major,L),Essay=L,
    previous_education(Possible_major,M),member(Prev_education,M),
    seats(Possible_major,N),N>0.


?- is_eligible(3.5,310,3,yes,bachelors_in_science_with_calculus,Possible_majors).