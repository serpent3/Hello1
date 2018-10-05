#include "headers.h"

Teacher::Teacher(string name, string lastname)
{
    this->name = name;
    this->lastname = lastname;
};
Teacher::~Teacher()
{
};
void Teacher::GradeStudent()
{
    cout << this->name << "Student graded" << endl;
};
void Teacher::SitInClass()
{
    cout << this->name << " sitting at front of class" << endl;
};
