#include "headers.h"

int main()
{
    Student *Student1 = new Student{"Name1", "Lastname1"};
    Student *Student2 = new Student{"Name2", "Lastname2"};
    Student *Student3 = new Student{"Name3", "Lastname3"};

    array<Student, 3> a_Students = {*Student1,*Student2, *Student3};

    Teacher *Teacher1 = new Teacher{"Teacher1", "Teacher1lastname"};
    // Teacher1->GradeStudent();
    // Teacher1->SitInClass();


    Course *IntermediateCpp = new Course{a_Students, Teacher1};

    //
    // IntermediateCpp.addStudents(a_Students);
    // IntermediateCpp.addTeacher(Teacher1);

};
