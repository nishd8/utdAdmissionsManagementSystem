# UTD Admissions Management System


## Inspiration
We were a little confused after attending Dr. Gupta's workshops because it was the first time we were exposed to this type of programming. We looked at the previous projects and drew inspiration from the challenges we had as prospective UTD students trying to determine our eligibility for the various majors offered. Finally, we determined that the process of advising students majors based on their qualifications should be automated.

## What it does
It has two functionalities currently:
1) To recommend what majors a student is qualified for based on admission requirements and a student's own qualifications.
2) An administrative component that enables you to dynamically issue admissions to students and adjust the number of seats available for each major.

Note: We've only developed it for the Erik Jonsson School of Engineering and Computer Science's Graduate Programs thus far.

## How we built it

1) Clearly defined limits to keep the project's scope in check.
2) Looked into the criteria for a variety of graduate programs at ECSS.
3) Established a clear distinction between facts and rules.
4) We developed a Python wrapper program to provide responsiveness to the sCASP execution.
5) Designed an HTML/JS-based UI to accept user inputs and display the outcomes of the sCASP model's predictions.

## Challenges we ran into
1) At first, we tried to correlate our traditional understanding of programming with this purely logical language, prolog. I.E, we tried to mutate facts, use if-else loops etc. 
2) The new syntax and the way prolog/ciao returns data in the form of a function argument was confusing at the start.
3) We wanted to build a system where it was easy for a user to run queries and not indulge in the prolog/ciao code, and the lack of dynamic datatypes made it difficult.
4) We even felt like giving up.

## Accomplishments that we're proud of
1) We didn't give up after tallking with one of the mentors and reading the challenges faced by previous years winners, we were happy to know that we are not alone.
2) We learned a new way of thinking in a short time.
3) We successfully added a level of a abstraction and interactivity to the sCASP system.
 
## What we learned
1) Answer Set Programming and Prolog. This is the first time anyone in our team has used prolog/sCASP or any kind of answer set programming.
2) Running a Linux machine. This hackathon, being the first one for 2 of our 3 members, taught us how to operate a linux machine on windows.

## What's next for UTD Admission Management System
1) Include graduate and undergraduate programs from other schools at UTD.
2) Collect proper data from the admmisions team to accurately recommend programs to students.
3) Expand on the admin side and provide predictions like how many students may get admits this year etc.
4) Using common sense reasoning in the future: Add a student preference weight to adjust recommendations to fit student's preferance if qualified; Adjust majors based on how competitive they are to allow the more competitive majors be recommended first (if a student qualifies).
