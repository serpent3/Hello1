#include "headers.h"

Course::Course(array<Student, 3> &a_Students, Teacher *Teacher1)
{
    //this->ar_Students = a_Students;
    //this->Teacher1 = Teacher1;
    cout << "/* Учитель в классе */" << endl;
    Teacher1->GradeStudent();
    Teacher1->SitInClass();
    for (int i=0; i < 3; i++)
    {
         cout << "/* Студенты в классе */" << endl;
         a_Students[i].SitInClass();
    };
};
Course::~Course()
{
};
// Course::addStudents()
// {
// };
// Course::addTeacher
